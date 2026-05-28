# SeleniumLibrary Keywords - Cookies Screenshots And Javascript

## Add Cookie

**Syntax**
```robot
Add Cookie
```

**Description**
Adds a cookie to your current session. ``name`` and ``value`` are required, ``path``, ``domain``, ``secure`` and ``expiry`` are optional. Expiry supports the same formats as the [http://robotframework.org/robotframework/latest/libraries/DateTime.html|DateTime] library or an epoch timestamp. Example: | `Add Cookie` |...

## Capture Element Screenshot

**Syntax**
```robot
Capture Element Screenshot
```

**Description**
Captures a screenshot from the element identified by ``locator`` and embeds it into log file. See `Capture Page Screenshot` for details about ``filename`` argument. See the `Locating elements` section for details about the locator syntax. An absolute path to the created element screenshot is returned. If the ``filen...

## Capture Page Screenshot

**Syntax**
```robot
Capture Page Screenshot
```

**Description**
Takes a screenshot of the current page and embeds it into a log file. ``filename`` argument specifies the name of the file to write the screenshot into. The directory where screenshots are saved can be set when `importing` the library or by using the `Set Screenshot Directory` keyword. If the directory is not config...

## Delete All Cookies

**Syntax**
```robot
Delete All Cookies
```

**Description**
Deletes all cookies.

## Delete Cookie

**Syntax**
```robot
Delete Cookie
```

**Description**
Deletes the cookie matching ``name``. If the cookie is not found, nothing happens.

## Execute Async Javascript

**Syntax**
```robot
Execute Async Javascript
```

**Description**
Executes asynchronous JavaScript code with possible arguments. Similar to `Execute Javascript` except that scripts executed with this keyword must explicitly signal they are finished by invoking the provided callback. This callback is always injected into the executed function as the last argument. Scripts must comp...

## Execute Javascript

**Syntax**
```robot
Execute Javascript
```

**Description**
Executes the given JavaScript code with possible arguments. ``code`` may be divided into multiple cells in the test data and ``code`` may contain multiple lines of code and arguments. In that case, the JavaScript code parts are concatenated together without adding spaces and optional arguments are separated from ``c...

## Get Cookie

**Syntax**
```robot
Get Cookie
```

**Description**
Returns information of cookie with ``name`` as an object. If no cookie is found with ``name``, keyword fails. The cookie object contains details about the cookie. Attributes available in the object are documented in the table below. | = Attribute = | = Explanation = | | name | The name of a cookie. | | value | Value...

## Get Cookies

**Syntax**
```robot
Get Cookies
```

**Description**
Returns all cookies of the current page. If ``as_dict`` argument evaluates as false, see `Boolean arguments` for more details, then cookie information is returned as a single string in format ``name1=value1; name2=value2; name3=value3``. When ``as_dict`` argument evaluates as true, cookie information is returned as ...

## Set Screenshot Directory

**Syntax**
```robot
Set Screenshot Directory
```

**Description**
Sets the directory for captured screenshots. ``path`` argument specifies the absolute path to a directory where the screenshots should be written to. If the directory does not exist, it will be created. The directory can also be set when `importing` the library. If it is not configured anywhere, screenshots are save...
