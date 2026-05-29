# Window And Scroll Commands

## Scroll position

```robot
${y}=    Execute Javascript    return window.scrollY;
${x}=    Execute Javascript    return window.scrollX;
```

## Scroll to top

```robot
Execute Javascript    window.scrollTo(0, 0);
```

## Scroll to bottom

```robot
Execute Javascript    window.scrollTo(0, document.body.scrollHeight);
```

## Scroll element into view

```robot
Execute Javascript    document.getElementById('footer').scrollIntoView();
```

## Window size

```robot
${w}=    Execute Javascript    return window.innerWidth;
${h}=    Execute Javascript    return window.innerHeight;
```

## Open/close window (use carefully in tests)

```robot
Execute Javascript    window.open('https://example.com', '_blank');
Execute Javascript    window.close();
```

## Reload page via JS

```robot
Execute Javascript    location.reload();
```

## Navigate

```robot
Execute Javascript    window.location.href='https://example.com/login';
```

## Get current hostname/path

```robot
${host}=    Execute Javascript    return window.location.hostname;
${path}=    Execute Javascript    return window.location.pathname;
```
