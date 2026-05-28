# Collections Keywords

### Create Dictionary
**Syntax**
```robot
${dict}=    Create Dictionary    key1=value1    key2=value2
```
**Example**
```robot
${body}=    Create Dictionary    firstname=Lokesh    lastname=QA
```

### Set To Dictionary
**Syntax**
```robot
Set To Dictionary    ${dict}    key=value
```
**Example**
```robot
Set To Dictionary    ${body}    additionalneeds=Breakfast
```

### Get From Dictionary
**Syntax**
```robot
${value}=    Get From Dictionary    ${dict}    key
```
**Example**
```robot
${token}=    Get From Dictionary    ${auth_json}    token
```

### Dictionary Should Contain Key
**Syntax**
```robot
Dictionary Should Contain Key    ${dict}    key
```
**Example**
```robot
Dictionary Should Contain Key    ${response.json()}    bookingid
```

### Create List
**Syntax**
```robot
${list}=    Create List    item1    item2
```
**Example**
```robot
${ids}=    Create List    10    20    30
```

### Append To List
**Syntax**
```robot
Append To List    ${list}    item
```
**Example**
```robot
Append To List    ${ids}    40
```
