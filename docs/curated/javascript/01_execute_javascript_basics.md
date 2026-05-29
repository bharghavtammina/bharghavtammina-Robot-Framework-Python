# Execute Javascript Basics

Robot keyword (SeleniumLibrary):

```robot
Execute Javascript    <code>
${result}=          Execute Javascript    return <expression>;
```

## Run simple JS

```robot
Execute Javascript    alert('Hello from Robot');
```

## Return a value to Robot

```robot
${title}=    Execute Javascript    return document.title;
Log          ${title}
```

## Pass Robot variable into JS

```robot
${name}=    Set Variable    Lokesh
Execute Javascript    localStorage.setItem('username', '${name}');
```

## Pass element into JS (Selenium special args)

```robot
Execute Javascript    arguments[0].click();    ARGUMENTS    id=submit-btn
```

## Multiple arguments

```robot
Execute Javascript    arguments[0].value=arguments[1];    ARGUMENTS    id=username    demo
```

## Async Javascript keyword

```robot
Execute Async Javascript    callback(arguments[0]);    ARGUMENTS    done
```

Use when script must call callback before finishing.
