*** Settings ***
Documentation    Keywords and variables for the local POC site in /site.
Resource         browser.resource

*** Variables ***
${SITE_HOST}       http://127.0.0.1:8080
${HOME_URL}        ${SITE_HOST}/index.html
${LOGIN_URL}       ${SITE_HOST}/login.html
${DASHBOARD_URL}    ${SITE_HOST}/dashboard.html
${CONTACT_URL}     ${SITE_HOST}/contact.html
${DEMO_USER}       demo
${DEMO_PASS}       secret123

*** Keywords ***
Open POC Site Home
    [Documentation]    Opens Chrome on the local demo home page.
    Set Global Variable    ${BASE_URL}    ${HOME_URL}
    Open Automation Browser

Go To POC Login Page
    Go To    ${LOGIN_URL}

Go To POC Contact Page
    Go To    ${CONTACT_URL}

Login With Demo User
    [Documentation]    Fills login form and submits with demo credentials.
    Input Text    id=username    ${DEMO_USER}
    Input Text    id=password    ${DEMO_PASS}
    Click Button    id=login-button

Submit Contact Form
    [Arguments]    ${name}    ${email}    ${message}
    Input Text    id=contact-name    ${name}
    Input Text    id=contact-email    ${email}
    Input Text    id=contact-message    ${message}
    Click Button    id=contact-submit
