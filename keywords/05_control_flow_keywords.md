# Control Flow Keywords

### IF / ELSE / END
**Syntax**
```robot
IF    ${condition}
    Keyword    arg
ELSE
    Another Keyword
END
```
**Example**
```robot
IF    ${response.status_code} == 200
    Log    Request success
ELSE
    Fail    Request failed
END
```

### FOR / END
**Syntax**
```robot
FOR    ${item}    IN    @{list}
    Keyword    ${item}
END
```
**Example**
```robot
FOR    ${id}    IN    1    2    3
    ${resp}=    GET On Session    api    /booking/${id}
    Log    ${resp.status_code}
END
```

### WHILE / END
**Syntax**
```robot
WHILE    ${condition}
    Keyword
END
```
**Example**
```robot
WHILE    ${retry} < 3
    Log    Retrying
    ${retry}=    Evaluate    ${retry}+1
END
```

### Run Keyword If
**Syntax**
```robot
Run Keyword If    ${condition}    Keyword    arg
```
**Example**
```robot
Run Keyword If    ${response.status_code} != 200    Fail    Unexpected status
```
