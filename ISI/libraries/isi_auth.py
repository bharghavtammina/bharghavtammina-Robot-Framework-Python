import os
from configparser import ConfigParser
from datetime import datetime, timezone
from pathlib import Path
from time import monotonic, sleep

from robot.libraries.BuiltIn import BuiltIn


def _get_credentials():
    username = os.environ.get("ISI_USERNAME", "").strip()
    password = os.environ.get("ISI_PASSWORD", "")

    credentials_path = Path(__file__).resolve().parents[1] / "local_credentials.ini"
    if credentials_path.exists():
        credentials = ConfigParser(interpolation=None)
        credentials.read(credentials_path, encoding="utf-8")
        username = username or credentials.get(
            "credentials", "username", fallback=""
        ).strip()
        password = password or credentials.get(
            "credentials", "password", fallback=""
        )
    return username, password


def enter_isi_credentials_if_login_required():
    builtin = BuiltIn()
    selenium = builtin.get_library_instance("SeleniumLibrary")
    if not selenium.find_elements("id=usernameId"):
        return False

    username, password = _get_credentials()
    if not username:
        raise AssertionError(
            "ISI login is required. Add your username to the local, git-ignored "
            "file ISI/local_credentials.ini."
        )
    if not password:
        raise AssertionError(
            "ISI login is required. Add your password to the local, git-ignored "
            "file ISI/local_credentials.ini."
        )

    login_started_at = datetime.now(timezone.utc).isoformat()
    previous_log_level = builtin.set_log_level("NONE")
    try:
        selenium.input_text("id=usernameId", username)
        selenium.input_password("id=passwordId", password)
        selenium.click_element("id=btnLogin")
    finally:
        builtin.set_log_level(previous_log_level)
    return login_started_at


def prepare_isi_download():
    download_directory = Path.home() / "Downloads"
    download_directory.mkdir(parents=True, exist_ok=True)
    return str(download_directory)


def get_isi_download_snapshot(download_directory):
    directory = Path(download_directory)
    return [path.name for path in directory.iterdir() if path.is_file()]


def wait_for_isi_download(download_directory, existing_files, timeout=120):
    directory = Path(download_directory)
    deadline = monotonic() + float(timeout)
    previous_sizes = {}

    while monotonic() < deadline:
        candidates = [
            path
            for path in directory.iterdir()
            if path.is_file()
            and path.name not in existing_files
            and not path.name.endswith(".crdownload")
        ]
        for candidate in candidates:
            size = candidate.stat().st_size
            if size > 0 and previous_sizes.get(candidate.name) == size:
                return str(candidate)
            previous_sizes[candidate.name] = size
        sleep(1)

    raise AssertionError(
        f"No completed report download appeared in '{directory}' "
        f"within {timeout} seconds."
    )
