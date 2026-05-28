# Test Cases Section Commands

Use these inside `*** Test Cases ***` steps.

## API Keywords (RequestsLibrary)

```robot
Create Session    api    ${BASE_URL}    verify=${VERIFY_SSL}
${resp}=    GET On Session       api    /booking/${booking_id}
${resp}=    POST On Session      api    /booking    json=${body}
${resp}=    PUT On Session       api    /booking/${booking_id}    json=${body}    headers=${headers}
${resp}=    PATCH On Session     api    /booking/${booking_id}    json=${body}    headers=${headers}
${resp}=    DELETE On Session    api    /booking/${booking_id}    headers=${headers}
```

## Data Build Keywords (Collections)

```robot
${body}=     Create Dictionary    firstname=Lokesh    lastname=QA
${dates}=    Create Dictionary    checkin=2026-06-01    checkout=2026-06-05
Set To Dictionary    ${body}    bookingdates=${dates}    additionalneeds=Breakfast
${token}=    Get From Dictionary    ${auth_json}    token
```

## Assertion Keywords

```robot
Should Be Equal As Integers    ${resp.status_code}    200
Should Be Equal                ${resp.json()}[firstname]    Lokesh
Should Be True                 ${resp.status_code} == 200 or ${resp.status_code} == 201
Should Not Be Empty            ${resp.text}
```

## Logging Keywords

```robot
Log    Status: ${resp.status_code}
Log    Headers: ${resp.headers}
Log    Body: ${resp.text}
Log To Console    Test finished
```

## Selenium Keywords (UI)

```robot
Open Browser    https://example.com    chrome
Input Text      id=username    demo
Click Button    id=login
Wait Until Element Is Visible    id=dashboard
Capture Page Screenshot
Close Browser
```
