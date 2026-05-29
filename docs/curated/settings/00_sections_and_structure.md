# Sections And Structure Keywords

## *** Settings ***

### Library
**Syntax**
```robot
Library    LibraryName
Library    LibraryName    arg1    arg2
```
**Example**
```robot
Library    RequestsLibrary
Library    Collections
```

### Resource
**Syntax**
```robot
Resource    path/to/file.resource
```
**Example**
```robot
Resource    ../../../resources/common.resource
```

### Variables (file import)
**Syntax**
```robot
Variables    path/to/variables.py
```
**Example**
```robot
Variables    ../resources/env.py
```

## *** Variables ***

### Scalar variable
**Syntax**
```robot
${NAME}    value
```
**Example**
```robot
${BASE_URL}    https://restful-booker.herokuapp.com
```

### List variable
**Syntax**
```robot
@{NAMES}    a    b    c
```
**Example**
```robot
@{CITIES}    Delhi    Chennai    Pune
```

### Dictionary variable
**Syntax**
```robot
&{USER}    first=Lokesh    last=K
```
**Example**
```robot
&{AUTH}    username=admin    password=password123
```
