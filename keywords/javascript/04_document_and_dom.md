# Document And DOM Commands

## Page info

```robot
${title}=    Execute Javascript    return document.title;
${url}=      Execute Javascript    return document.URL;
${ready}=    Execute Javascript    return document.readyState;
```

## Find element by id

```robot
${text}=    Execute Javascript    return document.getElementById('username').value;
```

## Query selector (CSS)

```robot
${text}=    Execute Javascript    return document.querySelector('#username').value;
${count}=   Execute Javascript    return document.querySelectorAll('.row').length;
```

## Change element text

```robot
Execute Javascript    document.getElementById('status').innerText='Updated';
```

## Change element HTML

```robot
Execute Javascript    document.getElementById('box').innerHTML='<b>Done</b>';
```

## Click element via JS

```robot
Execute Javascript    document.getElementById('submit-btn').click();
```

## Check element visible

```robot
${visible}=    Execute Javascript    return document.getElementById('modal').offsetParent !== null;
```

## Get attribute

```robot
${href}=    Execute Javascript    return document.querySelector('a.login').getAttribute('href');
```

## Add/remove CSS class

```robot
Execute Javascript    document.getElementById('menu').classList.add('open');
Execute Javascript    document.getElementById('menu').classList.remove('open');
Execute Javascript    return document.getElementById('menu').classList.contains('open');
```
