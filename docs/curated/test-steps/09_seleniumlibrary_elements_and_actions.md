# SeleniumLibrary Element And Action Keywords

### Click Element
**Syntax**
```robot
Click Element    locator
```
**Example**
```robot
Click Element    id=login-btn
```

### Click Button
**Syntax**
```robot
Click Button    locator
```
**Example**
```robot
Click Button    xpath=//button[@type='submit']
```

### Click Link
**Syntax**
```robot
Click Link    locator
```
**Example**
```robot
Click Link    link=Forgot Password?
```

### Input Text
**Syntax**
```robot
Input Text    locator    text
```
**Example**
```robot
Input Text    id=username    demo
```

### Input Password
**Syntax**
```robot
Input Password    locator    password
```
**Example**
```robot
Input Password    id=password    secret123
```

### Clear Element Text
**Syntax**
```robot
Clear Element Text    locator
```
**Example**
```robot
Clear Element Text    id=email
```

### Press Keys
**Syntax**
```robot
Press Keys    locator    keys
```
**Example**
```robot
Press Keys    id=search-box    ENTER
```

### Submit Form
**Syntax**
```robot
Submit Form    locator
```
**Example**
```robot
Submit Form    id=login-form
```

### Double Click Element
**Syntax**
```robot
Double Click Element    locator
```
**Example**
```robot
Double Click Element    id=row-1
```

### Open Context Menu
**Syntax**
```robot
Open Context Menu    locator
```
**Example**
```robot
Open Context Menu    css=.card
```

### Drag And Drop
**Syntax**
```robot
Drag And Drop    source_locator    target_locator
```
**Example**
```robot
Drag And Drop    id=item-1    id=drop-area
```

### Drag And Drop By Offset
**Syntax**
```robot
Drag And Drop By Offset    locator    xoffset    yoffset
```
**Example**
```robot
Drag And Drop By Offset    id=slider    40    0
```

### Mouse Over
**Syntax**
```robot
Mouse Over    locator
```
**Example**
```robot
Mouse Over    css=.menu-item
```

### Scroll Element Into View
**Syntax**
```robot
Scroll Element Into View    locator
```
**Example**
```robot
Scroll Element Into View    id=footer
```
