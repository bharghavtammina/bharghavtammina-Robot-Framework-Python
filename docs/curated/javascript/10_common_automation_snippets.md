# Common Automation Snippets

Ready-to-use JavaScript patterns in Robot tests.

## Hide/show element (debug)

```robot
Execute Javascript    document.getElementById('banner').style.display='none';
Execute Javascript    document.getElementById('banner').style.display='block';
```

## Remove overlay blocking clicks

```robot
Execute Javascript    var o=document.querySelector('.overlay'); if(o){o.remove();}
```

## Force click when normal click fails

```robot
Execute Javascript    document.getElementById('save-btn').click();
```

## Read table row count

```robot
${rows}=    Execute Javascript    return document.querySelectorAll('table tbody tr').length;
```

## Get all links on page

```robot
${links}=    Execute Javascript
...    return Array.from(document.querySelectorAll('a')).map(a=>a.href);
Log    ${links}
```

## Copy text to clipboard (browser support varies)

```robot
Execute Javascript    navigator.clipboard.writeText('copied text');
```

## Mock API response in browser (advanced)

```robot
Execute Javascript
...    window.fetch = () => Promise.resolve({json:()=>({status:'ok'})});
```

## Save auth token after login

```robot
${token}=    Execute Javascript    return localStorage.getItem('authToken');
Set Test Variable    ${AUTH_TOKEN}    ${token}
```

## Inject token before opening protected page

```robot
Go To    https://example.com
Execute Javascript    localStorage.setItem('authToken', 'test-token-123');
Go To    https://example.com/dashboard
```

## Print full page HTML (debug)

```robot
${html}=    Execute Javascript    return document.documentElement.outerHTML;
Log       ${html}
```
