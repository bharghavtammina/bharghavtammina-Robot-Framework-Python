*** Settings ***
Resource    ../../../resources/api_booker.resource

*** Test Cases ***
POST Example - Create Booking
    Create Booker API Session
    ${body}=    Create Dictionary    firstname=Lokesh    lastname=QA    totalprice=999    depositpaid=${True}
    ${dates}=    Create Dictionary    checkin=2026-06-01    checkout=2026-06-05
    Set To Dictionary    ${body}    bookingdates=${dates}    additionalneeds=Lunch
    ${response}=    POST On Session    api    /booking    json=${body}
    Log    Status: ${response.status_code}
    Log    Body: ${response.text}
    Should Be True    ${response.status_code} == 200 or ${response.status_code} == 201
    Should Be True    ${response.json()}[bookingid] > 0
    Should Be Equal    ${response.json()}[booking][firstname]    Lokesh
