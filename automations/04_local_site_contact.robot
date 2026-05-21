*** Settings ***
Documentation    POC: fill and submit the contact form on the local site.
Resource         ../resources/site.resource
Library          ../libraries/helpers.py

*** Tasks ***
Send Contact Message
    ${when}=    Get Run Timestamp
    Log    Contact form automation at ${when}    console=yes
    Open POC Site Home
    Click Element    id=btn-go-contact
    Submit Contact Form
    ...    Robot User
    ...    robot@poc.local
    ...    Hello from Robot Framework automation!
    Element Should Be Visible    id=contact-success
    Page Should Contain    Message sent!
    Close Automation Browser
