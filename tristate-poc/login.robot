*** Settings ***
Documentation    Tristate POC: log in to Traumasoft Transunit.
Library          SeleniumLibrary

*** Variables ***
${BASE_URL}     https://transunit.traumasoft.com
${USERNAME}     rbane
${PASSWORD}     Jmi@2026
${BROWSER}      chrome

*** Tasks ***
Login To Transunit
    Open Transunit Login Page
    Login With Transunit User
    Wait Until Location Is Not    ${BASE_URL}/
    Wait Until Location Is Not    ${BASE_URL}
    Click Reporting Header Menu
    Click Reporting Home Menu Item
    Click Reporting Sidebar Billing
    Click Aging By Current Payor Report
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

Click Reporting Header Menu
    [Documentation]    Opens the Reporting dropdown in the top header navigation.
    Wait Until Element Is Visible    xpath=//button[contains(@class,'top_menu_button')][normalize-space()='Reporting']
    Click Element    xpath=//button[contains(@class,'top_menu_button')][normalize-space()='Reporting']
    Wait Until Element Is Visible    xpath=//div[contains(@class,'v-overlay--active')]//a[contains(@href,'reporting:home')]

Click Reporting Home Menu Item
    [Documentation]    Clicks Reporting inside the header Reporting dropdown.
    Click Element    xpath=//div[contains(@class,'v-overlay--active')]//a[contains(@href,'reporting:home')]
    Wait Until Location Contains    reporting:home
    Wait Until Element Is Visible    css=#application_Tree_Container_QuickSearch

Click Reporting Sidebar Billing
    [Documentation]    Expands the Billing section in the Reporting sidebar tree.
    Wait Until Element Is Visible    xpath=//span[contains(@class,'reporting_tree_module_header')][normalize-space()='Billing']
    Click Element    xpath=//span[contains(@class,'reporting_tree_module_header')][normalize-space()='Billing']
    Wait Until Element Is Visible    xpath=//span[normalize-space()='Aging By Current Payor']

Click Aging By Current Payor Report
    [Documentation]    Selects the Aging By Current Payor report from the Billing sidebar list.
    Click Element    xpath=//span[normalize-space()='Aging By Current Payor']
    Wait Until Element Contains    id=application_Header_CurrentReport    Aging By Current Payor

Close Automation Browser
    [Documentation]    Closes all open browser windows.
    Close All Browsers
