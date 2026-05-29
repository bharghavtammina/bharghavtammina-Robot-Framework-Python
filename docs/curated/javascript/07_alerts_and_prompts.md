# Alerts, Confirm, Prompt (JavaScript)

Usually handled by Selenium keyword `Handle Alert`, but JS can also trigger them.

## Trigger alert

```robot
Execute Javascript    alert('Test alert');
Handle Alert    action=ACCEPT
```

## Trigger confirm and accept

```robot
Execute Javascript    confirm('Continue?');
Handle Alert    action=ACCEPT
```

## Trigger confirm and dismiss

```robot
Execute Javascript    confirm('Continue?');
Handle Alert    action=DISMISS
```

## Trigger prompt

```robot
Execute Javascript    prompt('Enter name:');
Handle Alert    action=ACCEPT
```

## Return value from prompt (browser dependent)

```robot
Execute Javascript    var n=prompt('Name?'); return n;
```

## Best practice
Use Selenium `Handle Alert` / `Alert Should Be Present` for stable automation.
