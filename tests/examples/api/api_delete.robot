*** Settings ***
Resource    ../../../resources/api_booker.resource

*** Test Cases ***
DELETE Example - Delete Booking
    Create Booker API Session
    ${headers}=    Authenticate Booker And Get Headers
    ${booking_id}=    Create Booking And Return Id    Delete    User    120    2026-08-10    2026-08-12    Dinner
    ${response}=    DELETE On Session    api    /booking/${booking_id}    headers=${headers}
    Log    Status: ${response.status_code}
    Should Be True    ${response.status_code} == 200 or ${response.status_code} == 201
