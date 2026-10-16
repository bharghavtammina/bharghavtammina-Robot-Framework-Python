*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${ISI_LOGIN_URL}    %{ISI_BASE_URL=https://www.isicentral.net/login.jsp}
${ISI_CHROME_DEBUGGER_ADDRESS}    %{ISI_CHROME_DEBUGGER_ADDRESS=127.0.0.1:9222}

*** Keywords ***
Open ISI Login Page
    Open Browser    ${ISI_LOGIN_URL}    chrome
    ...    options=add_experimental_option("debuggerAddress", "${ISI_CHROME_DEBUGGER_ADDRESS}")
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

Close ISI Browser
    Close All Browsers
