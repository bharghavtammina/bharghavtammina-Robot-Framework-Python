*** Settings ***
Documentation       Anonymous smoke test for the ISI Central login page.
Resource            ../resources/isi.resource
Suite Setup         Open ISI Login Page
Suite Teardown      Close ISI Browser

*** Test Cases ***
Login Page Shows Expected Fields
    Title Should Be    ISI Central Login
    Element Should Be Visible    id=usernameId
    Element Should Be Visible    id=passwordId
    Element Should Be Visible    id=btnLogin
    ${email_type}=    Get Element Attribute    id=usernameId    type
    ${password_type}=    Get Element Attribute    id=passwordId    type
    Should Be Equal    ${email_type}    email
    Should Be Equal    ${password_type}    password
