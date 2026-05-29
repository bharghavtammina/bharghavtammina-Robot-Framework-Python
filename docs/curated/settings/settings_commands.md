# Settings Section Commands

Use these only under `*** Settings ***`.

## Core Settings

### Library
```robot
Library    RequestsLibrary
Library    Collections
Library    SeleniumLibrary
```

### Resource
```robot
Resource    ../../../resources/common.resource
```

### Variables (import variable file)
```robot
Variables    ../resources/env.py
```

### Suite Setup / Suite Teardown
```robot
Suite Setup       Open Browser    https://example.com    chrome
Suite Teardown    Close All Browsers
```

### Test Setup / Test Teardown
```robot
Test Setup       Create Session    api    ${BASE_URL}
Test Teardown    Log    Test completed
```

### Documentation / Metadata
```robot
Documentation    API automation examples
Metadata         Owner    Lokesh
```
