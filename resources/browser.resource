*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:8080/index.html
${BROWSER}     chrome

*** Keywords ***
Open Automation Browser
    [Documentation]    Opens Chrome and navigates to the target page.
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

Close Automation Browser
    [Documentation]    Closes all open browser windows.
    Close All Browsers
