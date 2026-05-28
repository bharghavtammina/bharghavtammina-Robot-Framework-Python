# Logging And Debug Keywords

### Log
**Syntax**
```robot
Log    message
```
**Example**
```robot
Log    Status: ${response.status_code}
```

### Log Many
**Syntax**
```robot
Log Many    value1    value2    value3
```
**Example**
```robot
Log Many    ${response.status_code}    ${response.headers}    ${response.text}
```

### Log To Console
**Syntax**
```robot
Log To Console    message
```
**Example**
```robot
Log To Console    Running API test
```

### Comment
**Syntax**
```robot
Comment    text
```
**Example**
```robot
Comment    Create booking and validate response
```

### Fail
**Syntax**
```robot
Fail    message
```
**Example**
```robot
Fail    API returned unexpected data
```
