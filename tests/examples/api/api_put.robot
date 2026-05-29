*** Settings ***
Resource    ../../../resources/api_booker.resource

*** Test Cases ***
PUT Example - Full Update Booking
    Create Booker API Session
    ${headers}=    Authenticate Booker And Get Headers
    ${booking_id}=    Create Booking And Return Id    Initial    User    200    2026-06-10    2026-06-12    None
    ${body}=    Create Dictionary    firstname=Updated    lastname=User    totalprice=350    depositpaid=${True}
    ${dates}=    Create Dictionary    checkin=2026-06-15    checkout=2026-06-20
    Set To Dictionary    ${body}    bookingdates=${dates}    additionalneeds=Breakfast
    ${response}=    PUT On Session    api    /booking/${booking_id}    json=${body}    headers=${headers}
    Log    Status: ${response.status_code}
    Should Be Equal As Integers    ${response.status_code}    200
    Should Be Equal    ${response.json()}[firstname]    Updated
