# Wait And Conditions (JavaScript)

Use with Selenium wait keywords or direct checks.

## Wait until document ready

```robot
Wait Until Keyword Succeeds    10s    1s    Execute Javascript    return document.readyState=='complete';
```

## Wait until element exists

```robot
Wait Until Keyword Succeeds    10s    1s
...    Execute Javascript    return document.getElementById('dashboard') !== null;
```

## Wait until element visible

```robot
Wait Until Keyword Succeeds    10s    1s
...    Execute Javascript    var e=document.getElementById('toast'); return e && e.offsetParent !== null;
```

## Wait until text appears

```robot
Wait Until Keyword Succeeds    10s    1s
...    Execute Javascript    return document.body.innerText.includes('Success');
```

## Wait until localStorage key exists

```robot
Wait Until Keyword Succeeds    10s    1s
...    Execute Javascript    return localStorage.getItem('token') !== null;
```

## Poll custom condition

```robot
Wait Until Keyword Succeeds    15s    1s
...    Execute Javascript    return document.querySelectorAll('.row').length > 0;
```
