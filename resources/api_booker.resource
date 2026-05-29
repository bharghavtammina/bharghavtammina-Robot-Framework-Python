*** Settings ***
Documentation    Shared keywords for restful-booker.herokuapp.com API examples.
Library          RequestsLibrary
Library          Collections

*** Variables ***
${BOOKER_BASE_URL}    https://restful-booker.herokuapp.com
${BOOKER_VERIFY_SSL}    ${True}
${BOOKER_USERNAME}    admin
${BOOKER_PASSWORD}    password123

*** Keywords ***
Create Booker API Session
    Create Session    api    ${BOOKER_BASE_URL}    verify=${BOOKER_VERIFY_SSL}

Authenticate Booker And Get Headers
    ${auth_body}=    Create Dictionary    username=${BOOKER_USERNAME}    password=${BOOKER_PASSWORD}
    ${auth_response}=    POST On Session    api    /auth    json=${auth_body}
    ${token}=    Set Variable    ${auth_response.json()}[token]
    ${headers}=    Create Dictionary    Cookie=token=${token}
    RETURN    ${headers}

Create Booking And Return Id
    [Arguments]    ${firstname}    ${lastname}    ${totalprice}    ${checkin}    ${checkout}    ${additionalneeds}=${EMPTY}    ${depositpaid}=${False}
    ${body}=    Create Dictionary    firstname=${firstname}    lastname=${lastname}    totalprice=${totalprice}    depositpaid=${depositpaid}
    ${dates}=    Create Dictionary    checkin=${checkin}    checkout=${checkout}
    Set To Dictionary    ${body}    bookingdates=${dates}    additionalneeds=${additionalneeds}
    ${response}=    POST On Session    api    /booking    json=${body}
    RETURN    ${response.json()}[bookingid]
