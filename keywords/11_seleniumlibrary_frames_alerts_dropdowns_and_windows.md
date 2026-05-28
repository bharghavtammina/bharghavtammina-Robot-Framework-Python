# SeleniumLibrary Frames, Alerts, Dropdowns, And Windows Keywords

### Select Frame
**Syntax**
```robot
Select Frame    locator
```
**Example**
```robot
Select Frame    id=payment-frame
```

### Unselect Frame
**Syntax**
```robot
Unselect Frame
```
**Example**
```robot
Unselect Frame
```

### Handle Alert
**Syntax**
```robot
Handle Alert    action=ACCEPT    timeout=5s
```
**Example**
```robot
Handle Alert    action=ACCEPT
```

### Alert Should Be Present
**Syntax**
```robot
Alert Should Be Present    text=None    action=ACCEPT
```
**Example**
```robot
Alert Should Be Present    text=Are you sure?    action=ACCEPT
```

### Select From List By Label
**Syntax**
```robot
Select From List By Label    locator    label
```
**Example**
```robot
Select From List By Label    id=country    India
```

### Select From List By Value
**Syntax**
```robot
Select From List By Value    locator    value
```
**Example**
```robot
Select From List By Value    id=role    admin
```

### Unselect From List By Label
**Syntax**
```robot
Unselect From List By Label    locator    label
```
**Example**
```robot
Unselect From List By Label    id=tags    smoke
```

### Get List Items
**Syntax**
```robot
@{items}=    Get List Items    locator
```
**Example**
```robot
@{countries}=    Get List Items    id=country
```

### Select Window
**Syntax**
```robot
Select Window    locator
```
**Example**
```robot
Select Window    title=Payment
```

### Switch Window
**Syntax**
```robot
Switch Window    locator
```
**Example**
```robot
Switch Window    NEW
```
