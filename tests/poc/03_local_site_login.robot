*** Settings ***
Documentation    POC: login on the local site and reach the dashboard.
Resource         ../resources/site.resource
Library          ../libraries/helpers.py

*** Tasks ***
Login And Open Dashboard
    ${when}=    Get Run Timestamp
    Log    Login flow started at ${when}    console=yes
    Open POC Site Home
    Click Element    id=btn-go-login
    Login With Demo User
    Location Should Be    ${DASHBOARD_URL}
    Title Should Be    POC Demo Site — Dashboard
    Page Should Contain    You are signed in
    Close Automation Browser
