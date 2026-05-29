# User Defined Keywords

### Keyword Definition
**Syntax**
```robot
*** Keywords ***
Keyword Name
    [Arguments]    ${arg1}    ${arg2}
    Keyword    ${arg1}
```
**Example**
```robot
*** Keywords ***
Create Booking
    [Arguments]    ${first}    ${last}
    ${body}=    Create Dictionary    firstname=${first}    lastname=${last}    totalprice=100    depositpaid=${True}
    ${dates}=    Create Dictionary    checkin=2026-06-01    checkout=2026-06-02
    Set To Dictionary    ${body}    bookingdates=${dates}
    ${resp}=    POST On Session    api    /booking    json=${body}
    [Return]    ${resp}
```

### [Arguments]
**Syntax**
```robot
[Arguments]    ${arg}
```
**Example**
```robot
[Arguments]    ${booking_id}
```

### [Return]
**Syntax**
```robot
[Return]    ${value}
```
**Example**
```robot
[Return]    ${token}
```

### Keyword Call
**Syntax**
```robot
${result}=    Keyword Name    arg1    arg2
```
**Example**
```robot
${create_resp}=    Create Booking    Lokesh    QA
```
