*** Settings ***
Documentation    Tristate POC: log in to Traumasoft Transunit.
Library          SeleniumLibrary
Library          ../libraries/helpers.py

*** Variables ***
${BASE_URL}     https://transunit.traumasoft.com
${USERNAME}     rbane
${PASSWORD}     Jmi@2026
${BROWSER}      chrome

*** Tasks ***
Login To Transunit
    ${when}=    Get Run Timestamp
    Log    Transunit login started at ${when}    console=yes
    Open Transunit Login Page
    Login With Transunit User
    Wait Until Location Is Not    ${BASE_URL}/
    Wait Until Location Is Not    ${BASE_URL}
    Open All Menus
    Click Billing Menu Item
    Click Workflow Menu Item
    Sleep    10s
    Close Automation Browser

*** Keywords ***
Open Transunit Login Page
    [Documentation]    Opens Chrome on the Transunit login page.
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    css=[data-testid="login-username"]

Login With Transunit User
    [Documentation]    Fills the login form and submits with configured credentials.
    Input Text    css=[data-testid="login-username"]    ${USERNAME}
    Input Text    css=[data-testid="login-password"]    ${PASSWORD}
    Click Element    css=[data-testid="login-submit"]

Open All Menus
    [Documentation]    Opens the All Menus navigation panel after login.
    Wait Until Element Is Visible    css=button[title="All Menus"]
    Click Element    css=button[title="All Menus"]
    Wait Until Element Is Visible    xpath=//div[contains(@class,'ts_menu_list_item')][normalize-space()='Billing']

Click Billing Menu Item
    [Documentation]    Clicks Billing in All Menus to open its flyout.
    Click Element    xpath=//div[contains(@class,'ts_menu_list_item')][normalize-space()='Billing']
    Wait Until Element Is Visible    xpath=//a[contains(@href,'billing:workflow')]

Click Workflow Menu Item
    [Documentation]    Clicks Workflow inside the Billing flyout menu.
    Click Element    xpath=//a[contains(@href,'billing:workflow')]

Close Automation Browser
    [Documentation]    Closes all open browser windows.
    Close All Browsers
