# Variables Section Commands

Use these only under `*** Variables ***`.

## Variable Declarations

### Scalar
```robot
${BASE_URL}       https://restful-booker.herokuapp.com
${VERIFY_SSL}     ${True}
${USERNAME}       admin
${PASSWORD}       password123
```

### List
```robot
@{BOOKING_IDS}    101    102    103
```

### Dictionary
```robot
&{AUTH}    username=admin    password=password123
```

## Variable Keywords (used in steps, not in Variables table)

These are keyword calls and should be used in `*** Test Cases ***` or `*** Keywords ***`:

```robot
${id}=          Set Variable         1001
Set Test Variable    ${TOKEN}        abc123
Set Suite Variable   ${BASE_URL}     https://restful-booker.herokuapp.com
${value}=       Get Variable Value   ${USERNAME}    admin
```
