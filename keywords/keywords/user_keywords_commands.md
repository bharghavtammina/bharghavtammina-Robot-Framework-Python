# Keywords Section Commands

Use these under `*** Keywords ***` (user-defined reusable keywords).

## Define Reusable Keyword

```robot
*** Keywords ***
Create Booking Payload
    [Arguments]    ${first}    ${last}
    ${body}=    Create Dictionary    firstname=${first}    lastname=${last}    totalprice=100    depositpaid=${True}
    ${dates}=   Create Dictionary    checkin=2026-06-01    checkout=2026-06-02
    Set To Dictionary    ${body}    bookingdates=${dates}
    [Return]    ${body}
```

## Keyword With API Calls

```robot
Get Auth Token
    ${auth_body}=    Create Dictionary    username=${USERNAME}    password=${PASSWORD}
    ${auth_resp}=    POST On Session    api    /auth    json=${auth_body}
    ${token}=        Set Variable        ${auth_resp.json()}[token]
    [Return]         ${token}
```

## Keyword With Validation

```robot
Validate Success Status
    [Arguments]    ${response}
    Should Be True    ${response.status_code} == 200 or ${response.status_code} == 201
```
