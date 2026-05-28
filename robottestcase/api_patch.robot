*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    https://restful-booker.herokuapp.com
${VERIFY_SSL}    ${True}
${USERNAME}    admin
${PASSWORD}    password123

*** Test Cases ***
PATCH Example - Partial Update Booking
    Create Session    api    ${BASE_URL}    verify=${VERIFY_SSL}
    ${auth_body}=    Create Dictionary    username=${USERNAME}    password=${PASSWORD}
    ${auth_response}=    POST On Session    api    /auth    json=${auth_body}
    Log    Auth Status: ${auth_response.status_code}
    Log    Auth Headers: ${auth_response.headers}
    Log    Auth Body: ${auth_response.text}
    Log    Auth JSON: ${auth_response.json()}
    ${token}=    Set Variable    ${auth_response.json()}[token]
    ${headers}=    Create Dictionary    Cookie=token=${token}
    ${create_body}=    Create Dictionary    firstname=Patch    lastname=User    totalprice=150    depositpaid=${False}
    ${create_dates}=    Create Dictionary    checkin=2026-07-01    checkout=2026-07-02
    Set To Dictionary    ${create_body}    bookingdates=${create_dates}    additionalneeds=Tea
    ${create_response}=    POST On Session    api    /booking    json=${create_body}
    ${booking_id}=    Set Variable    ${create_response.json()}[bookingid]
    ${body}=    Create Dictionary    firstname=Patched
    ${response}=    PATCH On Session    api    /booking/${booking_id}    json=${body}    headers=${headers}
    Log    Status: ${response.status_code}
    Log    Headers: ${response.headers}
    Log    Body: ${response.text}
    Log    JSON: ${response.json()}
    Should Be Equal As Integers    ${response.status_code}    200
    Should Be Equal    ${response.json()}[firstname]    Patched
