# sessionStorage Commands

Same API as localStorage, but data clears when browser tab/window closes.

## Set value

```robot
Execute Javascript    sessionStorage.setItem('sessionId', 'sess-001');
Execute Javascript    sessionStorage.setItem('cartCount', '3');
```

## Get value

```robot
${session_id}=    Execute Javascript    return sessionStorage.getItem('sessionId');
Log               ${session_id}
```

## Remove one key

```robot
Execute Javascript    sessionStorage.removeItem('sessionId');
```

## Clear all sessionStorage

```robot
Execute Javascript    sessionStorage.clear();
```

## Check key exists

```robot
${exists}=    Execute Javascript    return sessionStorage.getItem('sessionId') !== null;
```

## Store and read JSON

```robot
Execute Javascript    sessionStorage.setItem('order', JSON.stringify({id:101, total:999}));
${order}=            Execute Javascript    return sessionStorage.getItem('order');
Log                  ${order}
```
