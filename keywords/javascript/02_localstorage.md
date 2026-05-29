# localStorage Commands

Used inside `Execute Javascript`.

## Set (store) value

```robot
Execute Javascript    localStorage.setItem('token', 'abc123');
Execute Javascript    localStorage.setItem('username', 'Lokesh');
Execute Javascript    localStorage.setItem('isLoggedIn', 'true');
```

## Get value

```robot
${token}=    Execute Javascript    return localStorage.getItem('token');
Log          ${token}
```

## Check if key exists

```robot
${exists}=    Execute Javascript    return localStorage.getItem('token') !== null;
```

## Remove one key

```robot
Execute Javascript    localStorage.removeItem('token');
```

## Clear all localStorage

```robot
Execute Javascript    localStorage.clear();
```

## Get number of keys

```robot
${count}=    Execute Javascript    return localStorage.length;
```

## Get key name by index

```robot
${key}=    Execute Javascript    return localStorage.key(0);
```

## Store JSON object

```robot
Execute Javascript    localStorage.setItem('user', JSON.stringify({name:'Lokesh', role:'QA'}));
${json}=             Execute Javascript    return localStorage.getItem('user');
Log                  ${json}
```

## Read JSON object field

```robot
${name}=    Execute Javascript    return JSON.parse(localStorage.getItem('user')).name;
```
