# SeleniumLibrary Browser And Navigation Keywords

### Open Browser
**Syntax**
```robot
Open Browser    ${url}    ${browser}
```
**Example**
```robot
Open Browser    https://example.com    chrome
```

### Create Webdriver
**Syntax**
```robot
Create Webdriver    Chrome    options=${options}
```
**Example**
```robot
${driver}=    Create Webdriver    Chrome
```

### Go To
**Syntax**
```robot
Go To    ${url}
```
**Example**
```robot
Go To    https://example.com/login
```

### Reload Page
**Syntax**
```robot
Reload Page
```
**Example**
```robot
Reload Page
```

### Go Back
**Syntax**
```robot
Go Back
```
**Example**
```robot
Go Back
```

### Get Location
**Syntax**
```robot
${url}=    Get Location
```
**Example**
```robot
${current_url}=    Get Location
```

### Get Title
**Syntax**
```robot
${title}=    Get Title
```
**Example**
```robot
${page_title}=    Get Title
```

### Maximize Browser Window
**Syntax**
```robot
Maximize Browser Window
```
**Example**
```robot
Maximize Browser Window
```

### Set Window Size
**Syntax**
```robot
Set Window Size    ${width}    ${height}
```
**Example**
```robot
Set Window Size    1366    768
```

### Close Browser
**Syntax**
```robot
Close Browser
```
**Example**
```robot
Close Browser
```

### Close All Browsers
**Syntax**
```robot
Close All Browsers
```
**Example**
```robot
Close All Browsers
```
