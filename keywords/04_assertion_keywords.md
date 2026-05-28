# Assertion Keywords

### Should Be Equal
**Syntax**
```robot
Should Be Equal    ${actual}    ${expected}
```
**Example**
```robot
Should Be Equal    ${response.json()}[firstname]    Lokesh
```

### Should Be Equal As Integers
**Syntax**
```robot
Should Be Equal As Integers    ${actual}    ${expected}
```
**Example**
```robot
Should Be Equal As Integers    ${response.status_code}    200
```

### Should Be True
**Syntax**
```robot
Should Be True    ${expression}
```
**Example**
```robot
Should Be True    ${response.status_code} == 200 or ${response.status_code} == 201
```

### Should Not Be Empty
**Syntax**
```robot
Should Not Be Empty    ${value}
```
**Example**
```robot
Should Not Be Empty    ${response.text}
```

### Should Contain
**Syntax**
```robot
Should Contain    ${container}    ${item}
```
**Example**
```robot
Should Contain    ${response.text}    booking
```

### Should Match Regexp
**Syntax**
```robot
Should Match Regexp    ${value}    ${pattern}
```
**Example**
```robot
Should Match Regexp    ${response.status_code}    ^20[01]$
```
