import imaplib
import os
import re
import ssl
from configparser import ConfigParser
from datetime import datetime, timedelta, timezone
from email import policy
from email.header import decode_header
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from pathlib import Path
from time import monotonic, sleep, time

import msal
from msal_extensions import FilePersistenceWithDataProtection, PersistedTokenCache
from robot.libraries.BuiltIn import BuiltIn

SCOPE = ["https://outlook.office365.com/IMAP.AccessAsUser.All"]
IMAP_SERVER = "outlook.office365.com"
IMAP_PORT = 993
OTP_PATTERN = re.compile(r"(?<!\d)(\d{6})(?!\d)")
OTP_CONTEXT = re.compile(
    r"\b(verification|verify|one[- ]time|security|authentication|mfa|otp|isi central)\b",
    re.IGNORECASE,
)


def _read_settings():
    path = Path(__file__).resolve().parents[1] / "local_outlook.ini"
    settings = ConfigParser(interpolation=None)
    if not path.is_file():
        raise AssertionError(
            "Outlook IMAP settings are missing. Copy "
            "ISI/local_outlook.ini.example to ISI/local_outlook.ini and configure it."
        )
    settings.read(path, encoding="utf-8")
    required = {
        "client_id": "ISI/local_outlook.ini [outlook] client_id",
        "tenant_id": "ISI/local_outlook.ini [outlook] tenant_id",
        "mailbox": "ISI/local_outlook.ini [outlook] mailbox",
    }
    values = {}
    missing = []
    for key, label in required.items():
        value = settings.get("outlook", key, fallback="").strip()
        if not value:
            missing.append(label)
        values[key] = value
    if missing:
        raise AssertionError("Configure " + ", ".join(missing) + ".")

    values["otp_sender_contains"] = settings.get(
        "outlook", "otp_sender_contains", fallback=""
    ).strip().casefold()
    values["otp_subject_contains"] = settings.get(
        "outlook", "otp_subject_contains", fallback=""
    ).strip().casefold()
    values["otp_timeout_seconds"] = settings.getint(
        "outlook", "otp_timeout_seconds", fallback=180
    )
    if values["otp_timeout_seconds"] < 1:
        raise AssertionError("otp_timeout_seconds must be a positive integer.")
    return values


def _decode_header(value):
    decoded = []
    for part, charset in decode_header(value or ""):
        if isinstance(part, bytes):
            decoded.append(part.decode(charset or "utf-8", errors="replace"))
        else:
            decoded.append(part)
    return "".join(decoded)


def _message_text(message):
    chunks = []
    for part in message.walk():
        if part.get_content_maintype() == "multipart":
            continue
        if part.get_content_disposition() == "attachment":
            continue
        if part.get_content_type() not in ("text/plain", "text/html"):
            continue
        try:
            content = part.get_content()
        except (LookupError, UnicodeError):
            payload = part.get_payload(decode=True) or b""
            content = payload.decode(part.get_content_charset() or "utf-8", errors="replace")
        if isinstance(content, str):
            chunks.append(re.sub(r"<[^>]+>", " ", content))
    return "\n".join(chunks)


def _message_otp(raw_message, settings, not_before):
    message = BytesParser(policy=policy.default).parsebytes(raw_message)
    sender = _decode_header(message.get("From", "")).casefold()
    subject = _decode_header(message.get("Subject", ""))
    body = _message_text(message)

    if settings["otp_sender_contains"] and settings["otp_sender_contains"] not in sender:
        return None
    if (
        settings["otp_subject_contains"]
        and settings["otp_subject_contains"] not in subject.casefold()
    ):
        return None

    date_header = message.get("Date")
    if not date_header:
        return None
    try:
        message_date = parsedate_to_datetime(date_header)
        if message_date.tzinfo is None:
            message_date = message_date.replace(tzinfo=timezone.utc)
        if message_date.astimezone(timezone.utc) < not_before - timedelta(seconds=5):
            return None
    except (TypeError, ValueError, OverflowError):
        return None

    searchable = f"{subject}\n{body}"
    if not OTP_CONTEXT.search(searchable):
        return None
    matches = {match.group(1) for match in OTP_PATTERN.finditer(searchable)}
    if len(matches) != 1:
        return None
    return matches.pop()


def _is_device_flow_pending(result):
    error = str(result.get("error", "")).casefold()
    description = str(result.get("error_description", "")).casefold()
    return error in ("authorization_pending", "slow_down") or (
        "aadsts70016" in description and "authorization is pending" in description
    )


def _acquire_access_token(settings):
    token_directory = Path(os.environ.get("LOCALAPPDATA", Path.home())) / "ISI-Robot"
    token_directory.mkdir(parents=True, exist_ok=True)
    cache_path = token_directory / "outlook-msal-cache.bin"
    persistence = FilePersistenceWithDataProtection(str(cache_path))
    cache = PersistedTokenCache(persistence)
    app = msal.PublicClientApplication(
        settings["client_id"],
        authority=f"https://login.microsoftonline.com/{settings['tenant_id']}",
        token_cache=cache,
    )
    accounts = app.get_accounts(username=settings["mailbox"])
    result = None
    if accounts:
        result = app.acquire_token_silent(SCOPE, account=accounts[0])
    if result and "access_token" in result:
        return result["access_token"]

    flow = app.initiate_device_flow(scopes=SCOPE)
    if "user_code" not in flow:
        raise RuntimeError(
            "Microsoft OAuth could not start the device sign-in flow: "
            + flow.get("error_description", flow.get("error", "unknown error"))
        )
    BuiltIn().log_to_console(
        "Authorize Outlook IMAP access in the Microsoft sign-in page. "
        + flow["message"]
    )
    expires_at = flow.get("expires_at")
    if expires_at is None:
        raise RuntimeError("Microsoft device sign-in did not provide an expiration time.")
    deadline = monotonic() + max(0, float(expires_at) - time())

    while monotonic() < deadline:
        result = app.acquire_token_by_device_flow(
            flow, exit_condition=lambda _: True
        )
        if "access_token" in result:
            return result["access_token"]
        if not _is_device_flow_pending(result):
            raise RuntimeError(
                "Microsoft did not authorize Outlook IMAP access: "
                + result.get("error_description", result.get("error", "unknown error"))
            )
        remaining = deadline - monotonic()
        if remaining > 0:
            sleep(min(float(flow.get("interval", 5)), remaining))

    raise RuntimeError(
        "Microsoft Outlook authorization timed out. Complete the device sign-in "
        "before the code expires, then rerun the ISI test."
    )


def _find_recent_otp(settings, not_before):
    token = _acquire_access_token(settings)
    auth_string = (
        f"user={settings['mailbox']}\x01auth=Bearer {token}\x01\x01"
    ).encode("utf-8")
    connection = imaplib.IMAP4_SSL(
        IMAP_SERVER, IMAP_PORT, ssl_context=ssl.create_default_context()
    )
    try:
        connection.authenticate("XOAUTH2", lambda _: auth_string)
        status, _ = connection.select("INBOX", readonly=True)
        if status != "OK":
            raise RuntimeError("Could not open the Outlook inbox for IMAP search.")

        since = not_before.strftime("%d-%b-%Y")
        status, data = connection.search(None, "SINCE", since)
        if status != "OK":
            raise RuntimeError("Could not search the Outlook inbox for new mail.")

        message_ids = data[0].split()
        for message_id in reversed(message_ids):
            status, message_data = connection.fetch(message_id, "(RFC822)")
            if status != "OK":
                raise RuntimeError("Could not retrieve a recent Outlook email for OTP matching.")
            raw_message = next(
                (
                    item[1]
                    for item in message_data
                    if isinstance(item, tuple) and isinstance(item[1], bytes)
                ),
                None,
            )
            if raw_message is None:
                raise RuntimeError("Outlook returned an email without its message content.")
            code = _message_otp(raw_message, settings, not_before)
            if code:
                return code
        return None
    finally:
        try:
            connection.logout()
        except (imaplib.IMAP4.error, OSError):
            pass


def complete_isi_email_otp_if_required(login_started_at, timeout=None):
    builtin = BuiltIn()
    selenium = builtin.get_library_instance("SeleniumLibrary")
    driver = selenium.driver
    otp_locators = (
        "css:input[autocomplete='one-time-code']",
        "css:input[placeholder*='authentication code' i]",
        "css:input[name*='otp' i]",
        "css:input[id*='otp' i]",
        "css:input[name*='verification' i]",
        "css:input[id*='verification' i]",
        "css:input[name*='code' i]",
        "css:input[placeholder*='code' i]",
        "css:input[inputmode='numeric']",
    )

    def find_otp_inputs():
        for locator in otp_locators:
            elements = [
                element
                for element in selenium.find_elements(locator)
                if element.is_displayed() and element.is_enabled()
            ]
            if elements:
                return elements
        return []

    def request_email_code_if_needed():
        send_code_buttons = [
            button
            for button in driver.find_elements(
                "xpath",
                "//button[normalize-space()='Send Code']"
                "|//input[(@type='submit' or @type='button') "
                "and normalize-space(@value)='Send Code']",
            )
            if button.is_displayed() and button.is_enabled()
        ]
        if not send_code_buttons:
            return False

        email_labels = [
            label
            for label in driver.find_elements(
                "xpath",
                "//label[contains(translate(normalize-space(.), 'EMAIL', 'email'), 'email')]",
            )
            if label.is_displayed()
        ]
        if email_labels:
            email_labels[0].click()
        else:
            visible_radios = [
                radio
                for radio in driver.find_elements("xpath", "//input[@type='radio']")
                if radio.is_displayed() and radio.is_enabled()
            ]
            if len(visible_radios) != 1:
                raise AssertionError(
                    "ISI offers email verification, but the Email option could not "
                    "be selected unambiguously."
                )
            if not visible_radios[0].is_selected():
                visible_radios[0].click()

        send_code_buttons[0].click()
        BuiltIn().log_to_console("Requested the ISI email verification code.")
        return True

    request_email_code_if_needed()

    challenge_deadline = monotonic() + 30
    otp_inputs = find_otp_inputs()
    while (
        not otp_inputs
        and monotonic() < challenge_deadline
        and not any(
            element.is_displayed()
            for element in driver.find_elements(
                "xpath", "//*[normalize-space(.)='Reporting']"
            )
        )
    ):
        sleep(0.5)
        otp_inputs = find_otp_inputs()

    if not otp_inputs:
        return False

    settings = _read_settings()
    wait_seconds = (
        settings["otp_timeout_seconds"] if timeout is None else float(timeout)
    )
    if wait_seconds < 1:
        raise AssertionError("OTP wait timeout must be a positive number of seconds.")
    try:
        not_before = datetime.fromisoformat(login_started_at)
        if not_before.tzinfo is None:
            not_before = not_before.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError) as error:
        raise AssertionError("A valid ISI login start timestamp is required.") from error

    BuiltIn().log_to_console("ISI email verification detected; waiting for a new Outlook OTP.")
    deadline = monotonic() + float(wait_seconds)
    code = None
    while monotonic() < deadline:
        code = _find_recent_otp(settings, not_before)
        if code:
            break
        sleep(min(10, max(1, deadline - monotonic())))
    if not code:
        raise AssertionError(
            f"No matching new ISI verification email arrived in Outlook within {wait_seconds} seconds."
        )

    previous_log_level = builtin.set_log_level("NONE")
    try:
        otp_inputs = find_otp_inputs()
        if not otp_inputs:
            raise AssertionError("The ISI verification input disappeared before OTP entry.")
        if len(otp_inputs) > 1:
            if len(otp_inputs) != len(code):
                raise AssertionError(
                    "ISI displayed multiple verification inputs, but their count did not "
                    "match the six-digit code."
                )
            for otp_input, digit in zip(otp_inputs, code):
                otp_input.clear()
                otp_input.send_keys(digit)
        else:
            otp_inputs[0].clear()
            otp_inputs[0].send_keys(code)

        submit_buttons = [
            button
            for button in driver.find_elements(
                "xpath",
                "//button[normalize-space()='Validate' or normalize-space()='Verify' "
                "or normalize-space()='Continue' or normalize-space()='Submit']"
                "|//input[@type='submit' and "
                "(translate(@value,'VALIDATE','validate')='validate' "
                "or translate(@value,'VERIFYCONTINUE','verifycontinue')='verify' "
                "or translate(@value,'SUBMIT','submit')='submit')]",
            )
            if button.is_displayed() and button.is_enabled()
        ]
        if submit_buttons:
            submit_buttons[0].click()
        else:
            otp_inputs[-1].send_keys("\n")
    finally:
        builtin.set_log_level(previous_log_level)
    return True
