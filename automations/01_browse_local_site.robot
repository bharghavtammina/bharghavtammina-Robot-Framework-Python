*** Settings ***
Documentation    POC: open the local demo site home page and check content.
Resource         ../resources/site.resource
Library          ../libraries/helpers.py

*** Tasks ***
Browse Local POC Home Page
    ${when}=    Get Run Timestamp
    Log    Local site automation started at ${when}    console=yes
    Open POC Site Home
    Title Should Be    POC Demo Site — Home
    Page Should Contain    Welcome to your POC site
    Element Should Be Visible    id=btn-go-login
    Click Element    id=nav-login
    Location Should Be    ${LOGIN_URL}
    Close Automation Browser




