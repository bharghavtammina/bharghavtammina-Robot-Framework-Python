*** Settings ***
Documentation       Logs in to ISI Central, opens Invoice_Lastweek, and downloads it as CSV.
Resource            ../resources/isi.resource
Library             ../libraries/isi_auth.py
Library             ../libraries/isi_outlook_otp.py
Suite Setup         Open ISI Login Page

*** Test Cases ***
Download Invoice Last Week Report
    ${login_started_at}=    Enter ISI Credentials If Login Required
    IF    $login_started_at
        Log To Console    Credentials submitted. Checking Outlook automatically if ISI requests email verification.
        Complete ISI Email OTP If Required    ${login_started_at}
    ELSE
        Log To Console    Reusing the current Chrome session.
    END
    Wait Until Page Contains Element
    ...    xpath=//*[normalize-space(.)="Reporting"]
    ...    timeout=%{ISI_AUTH_TIMEOUT=180s}
    Page Should Not Contain Element    id=usernameId
    Click ISI Main Item    Reporting
    Click ISI Main Item    Repository
    Wait Until Page Contains Element
    ...    xpath=//iframe[contains(@src, "/webCentral/app/portal/tab/report")]
    ...    timeout=30s
    Select Frame    xpath=//iframe[contains(@src, "/webCentral/app/portal/tab/report")]
    Expand ISI Report Folder    My Reports
    Log To Console    Selecting Invoice_Lastweek...
    Wait Until Page Contains Element
    ...    xpath=//div[@role="treeitem" and @aria-label="Invoice_Lastweek"]//label[@role="link"]
    ...    timeout=30s
    Click Element
    ...    xpath=//div[@role="treeitem" and @aria-label="Invoice_Lastweek"]//label[@role="link"]
    Wait Until Page Contains Element    css=button[title="Export"]    timeout=60s
    ${download_directory}=    Prepare ISI Download
    ${existing_files}=    Get ISI Download Snapshot    ${download_directory}
    Log To Console    Opening the report export options...
    Click Element    css=button[title="Export"]
    Wait Until Page Contains Element
    ...    xpath=//div[contains(@class,"modal-dialog")]//select
    ...    timeout=20s
    Select From List By Value
    ...    xpath=//div[contains(@class,"modal-dialog")]//select
    ...    CSV
    Click Element
    ...    xpath=//div[contains(@class,"modal-dialog")]//button[normalize-space(.)="Export"]
    Log To Console    Exporting Invoice_Lastweek as CSV...
    ${downloaded_file}=    Wait For ISI Download
    ...    ${download_directory}
    ...    ${existing_files}
    ...    timeout=180
    Should End With    ${downloaded_file}    .csv
    Log To Console    Report downloaded: ${downloaded_file}

*** Keywords ***
Click ISI Main Item
    [Arguments]    ${label}
    Log To Console    Selecting ${label}...
    Wait Until Page Contains Element
    ...    xpath=//*[normalize-space(.)="${label}"]
    ...    timeout=30s
    Click Element    xpath=//*[normalize-space(.)="${label}"]

Expand ISI Report Folder
    [Arguments]    ${label}
    ${folder}=    Set Variable    xpath=//div[@role="treeitem" and @aria-label="${label}"]
    Wait Until Page Contains Element    ${folder}    timeout=30s
    ${expanded}=    Get Element Attribute    ${folder}    aria-expanded
    IF    $expanded == "false"
        Log To Console    Expanding ${label}...
        Click Element    ${folder}//span[@role="button" and @aria-label="Toggle Folder"]
        Wait Until Page Contains Element
        ...    xpath=//div[@role="treeitem" and @aria-label="${label}" and @aria-expanded="true"]
        ...    timeout=15s
    END
