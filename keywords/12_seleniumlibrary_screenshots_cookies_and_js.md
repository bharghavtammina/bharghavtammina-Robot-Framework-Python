# SeleniumLibrary Screenshots, Cookies, And JavaScript Keywords

### Capture Page Screenshot
**Syntax**
```robot
Capture Page Screenshot    filename=page.png
```
**Example**
```robot
Capture Page Screenshot    login-page.png
```

### Capture Element Screenshot
**Syntax**
```robot
Capture Element Screenshot    locator    filename=element.png
```
**Example**
```robot
Capture Element Screenshot    id=profile-card    profile.png
```

### Execute JavaScript
**Syntax**
```robot
${result}=    Execute JavaScript    return document.title;
```
**Example**
```robot
${scroll_y}=    Execute JavaScript    return window.scrollY;
```

### Get Cookie
**Syntax**
```robot
${cookie}=    Get Cookie    name
```
**Example**
```robot
${session}=    Get Cookie    sessionid
```

### Get Cookies
**Syntax**
```robot
${cookies}=    Get Cookies
```
**Example**
```robot
${all_cookies}=    Get Cookies
```

### Add Cookie
**Syntax**
```robot
Add Cookie    name    value
```
**Example**
```robot
Add Cookie    testmode    true
```

### Delete Cookie
**Syntax**
```robot
Delete Cookie    name
```
**Example**
```robot
Delete Cookie    testmode
```

### Delete All Cookies
**Syntax**
```robot
Delete All Cookies
```
**Example**
```robot
Delete All Cookies
```

### Set Selenium Timeout
**Syntax**
```robot
Set Selenium Timeout    10s
```
**Example**
```robot
Set Selenium Timeout    15s
```

### Set Selenium Speed
**Syntax**
```robot
Set Selenium Speed    0.2s
```
**Example**
```robot
Set Selenium Speed    0.1s
```

### Set Selenium Implicit Wait
**Syntax**
```robot
Set Selenium Implicit Wait    5s
```
**Example**
```robot
Set Selenium Implicit Wait    3s
```
