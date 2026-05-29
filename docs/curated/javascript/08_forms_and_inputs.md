# Forms And Inputs (JavaScript)

## Set input value

```robot
Execute Javascript    document.getElementById('username').value='demo';
Execute Javascript    document.querySelector('#password').value='secret123';
```

## Get input value

```robot
${user}=    Execute Javascript    return document.getElementById('username').value;
```

## Clear input

```robot
Execute Javascript    document.getElementById('email').value='';
```

## Check checkbox

```robot
Execute Javascript    document.getElementById('remember').checked=true;
```

## Uncheck checkbox

```robot
Execute Javascript    document.getElementById('remember').checked=false;
```

## Select radio button

```robot
Execute Javascript    document.getElementById('gender-male').checked=true;
```

## Select dropdown option by value

```robot
Execute Javascript    document.getElementById('country').value='IN';
```

## Select dropdown option by text

```robot
Execute Javascript
...    var s=document.getElementById('country');
...    for(var i=0;i<s.options.length;i++){if(s.options[i].text==='India'){s.selectedIndex=i;break;}}
```

## Submit form

```robot
Execute Javascript    document.getElementById('login-form').submit();
```

## Disable/enable button

```robot
Execute Javascript    document.getElementById('submit-btn').disabled=true;
Execute Javascript    document.getElementById('submit-btn').disabled=false;
```

## Read validation message

```robot
${msg}=    Execute Javascript    return document.getElementById('email').validationMessage;
```
