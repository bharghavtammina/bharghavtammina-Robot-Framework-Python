*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${ISI_LOGIN_URL}    %{ISI_BASE_URL=https://www.isicentral.net/login.jsp}
${ISI_BROWSER}      chrome

*** Keywords ***
Open ISI Login Page
    Open Browser    ${ISI_LOGIN_URL}    ${ISI_BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

Close ISI Browser
    Close All Browsers
