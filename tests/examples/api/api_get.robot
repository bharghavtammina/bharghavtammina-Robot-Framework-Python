*** Settings ***
Resource    ../../../resources/api_booker.resource

*** Test Cases ***
GET Example - Fetch Created Booking
    Create Booker API Session
    ${booking_id}=    Create Booking And Return Id
    ...    Lokesh    Tester    123    2026-05-28    2026-05-30    Breakfast    ${True}
    ${response}=    GET On Session    api    /booking/${booking_id}
    Log    Status: ${response.status_code}
    Log    Body: ${response.text}
    Should Be Equal As Integers    ${response.status_code}    200
    Should Be Equal    ${response.json()}[firstname]    Lokesh
