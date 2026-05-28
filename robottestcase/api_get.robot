*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    https://restful-booker.herokuapp.com
${VERIFY_SSL}    ${True}

*** Test Cases ***
GET Example - Fetch Created Booking
    Create Session    api    ${BASE_URL}    verify=${VERIFY_SSL}
    ${create_body}=    Create Dictionary    firstname=Lokesh    lastname=Tester    totalprice=123    depositpaid=${True}
    ${dates}=    Create Dictionary    checkin=2026-05-28    checkout=2026-05-30
    Set To Dictionary    ${create_body}    bookingdates=${dates}    additionalneeds=Breakfast
    ${create_response}=    POST On Session    api    /booking    json=${create_body}
    Log    Create Status: ${create_response.status_code}
    Log    Create Headers: ${create_response.headers}
    Log    Create Body: ${create_response.text}
    Log    Create JSON: ${create_response.json()}
    ${booking_id}=    Set Variable    ${create_response.json()}[bookingid]
    ${response}=    GET On Session    api    /booking/${booking_id}
    Log    Status: ${response.status_code}
    Log    Headers: ${response.headers}
    Log    Body: ${response.text}
    Log    JSON: ${response.json()}
    Should Be Equal As Integers    ${response.status_code}    200
    Should Be Equal    ${response.json()}[firstname]    Lokesh



