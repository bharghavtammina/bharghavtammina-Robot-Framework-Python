*** Settings ***
Resource    ../../../resources/api_booker.resource

*** Test Cases ***
PATCH Example - Partial Update Booking
    Create Booker API Session
    ${headers}=    Authenticate Booker And Get Headers
    ${booking_id}=    Create Booking And Return Id    Patch    User    150    2026-07-01    2026-07-02    Tea
    ${body}=    Create Dictionary    firstname=Patched
    ${response}=    PATCH On Session    api    /booking/${booking_id}    json=${body}    headers=${headers}
    Log    Status: ${response.status_code}
    Should Be Equal As Integers    ${response.status_code}    200
    Should Be Equal    ${response.json()}[firstname]    Patched
