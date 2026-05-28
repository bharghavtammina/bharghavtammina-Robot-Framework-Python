# SeleniumLibrary Wait, Assertion, And Selector Keywords

### Wait Until Element Is Visible
**Syntax**
```robot
Wait Until Element Is Visible    locator    timeout=10s
```
**Example**
```robot
Wait Until Element Is Visible    id=dashboard    timeout=15s
```

### Wait Until Element Is Enabled
**Syntax**
```robot
Wait Until Element Is Enabled    locator    timeout=10s
```
**Example**
```robot
Wait Until Element Is Enabled    id=submit
```

### Wait Until Element Contains
**Syntax**
```robot
Wait Until Element Contains    locator    expected_text    timeout=10s
```
**Example**
```robot
Wait Until Element Contains    id=toast    Success
```

### Wait Until Page Contains
**Syntax**
```robot
Wait Until Page Contains    text    timeout=10s
```
**Example**
```robot
Wait Until Page Contains    Welcome
```

### Wait Until Location Contains
**Syntax**
```robot
Wait Until Location Contains    expected    timeout=10s
```
**Example**
```robot
Wait Until Location Contains    dashboard
```

### Page Should Contain Element
**Syntax**
```robot
Page Should Contain Element    locator
```
**Example**
```robot
Page Should Contain Element    css=.profile-card
```

### Page Should Not Contain Element
**Syntax**
```robot
Page Should Not Contain Element    locator
```
**Example**
```robot
Page Should Not Contain Element    id=loading-spinner
```

### Element Should Be Visible
**Syntax**
```robot
Element Should Be Visible    locator
```
**Example**
```robot
Element Should Be Visible    id=logout
```

### Element Should Be Enabled
**Syntax**
```robot
Element Should Be Enabled    locator
```
**Example**
```robot
Element Should Be Enabled    id=save-btn
```

### Element Text Should Be
**Syntax**
```robot
Element Text Should Be    locator    expected
```
**Example**
```robot
Element Text Should Be    id=heading    Dashboard
```

### Get Text
**Syntax**
```robot
${text}=    Get Text    locator
```
**Example**
```robot
${msg}=    Get Text    id=success-msg
```

### Get Element Attribute
**Syntax**
```robot
${value}=    Get Element Attribute    locator@attribute
```
**Example**
```robot
${href}=    Get Element Attribute    css=a.help@href
```

### Get WebElements
**Syntax**
```robot
@{elements}=    Get WebElements    locator
```
**Example**
```robot
@{rows}=    Get WebElements    css=table tbody tr
```

### Get Element Count
**Syntax**
```robot
${count}=    Get Element Count    locator
```
**Example**
```robot
${row_count}=    Get Element Count    css=table tbody tr
```
