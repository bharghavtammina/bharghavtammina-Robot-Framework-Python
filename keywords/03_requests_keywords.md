# RequestsLibrary Keywords

### Create Session
**Syntax**
```robot
Create Session    alias    ${base_url}    verify=${True}
```
**Example**
```robot
Create Session    api    ${BASE_URL}    verify=${VERIFY_SSL}
```

### GET On Session
**Syntax**
```robot
${response}=    GET On Session    alias    /path    headers=${headers}
```
**Example**
```robot
${response}=    GET On Session    api    /booking/${booking_id}
```

### POST On Session
**Syntax**
```robot
${response}=    POST On Session    alias    /path    json=${body}    headers=${headers}
```
**Example**
```robot
${response}=    POST On Session    api    /booking    json=${body}
```

### PUT On Session
**Syntax**
```robot
${response}=    PUT On Session    alias    /path    json=${body}    headers=${headers}
```
**Example**
```robot
${response}=    PUT On Session    api    /booking/${booking_id}    json=${body}    headers=${headers}
```

### PATCH On Session
**Syntax**
```robot
${response}=    PATCH On Session    alias    /path    json=${body}    headers=${headers}
```
**Example**
```robot
${response}=    PATCH On Session    api    /booking/${booking_id}    json=${body}    headers=${headers}
```

### DELETE On Session
**Syntax**
```robot
${response}=    DELETE On Session    alias    /path    headers=${headers}
```
**Example**
```robot
${response}=    DELETE On Session    api    /booking/${booking_id}    headers=${headers}
```
