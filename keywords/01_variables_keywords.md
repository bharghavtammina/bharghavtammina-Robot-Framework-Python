# Variable Keywords

### Set Variable
**Syntax**
```robot
${var}=    Set Variable    value
```
**Example**
```robot
${booking_id}=    Set Variable    ${create_response.json()}[bookingid]
```

### Set Test Variable
**Syntax**
```robot
Set Test Variable    ${var}    value
```
**Example**
```robot
Set Test Variable    ${TOKEN}    ${auth_response.json()}[token]
```

### Set Suite Variable
**Syntax**
```robot
Set Suite Variable    ${var}    value
```
**Example**
```robot
Set Suite Variable    ${BASE_URL}    https://restful-booker.herokuapp.com
```

### Set Global Variable
**Syntax**
```robot
Set Global Variable    ${var}    value
```
**Example**
```robot
Set Global Variable    ${ENV}    qa
```

### Get Variable Value
**Syntax**
```robot
${value}=    Get Variable Value    ${var}    default
```
**Example**
```robot
${username}=    Get Variable Value    ${USERNAME}    admin
```
