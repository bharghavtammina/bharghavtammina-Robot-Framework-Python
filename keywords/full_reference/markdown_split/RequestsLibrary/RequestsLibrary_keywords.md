# RequestsLibrary Keywords

## Create Client Cert Session

**Syntax**
```robot
Create Client Cert Session
```

**Description**
Create Session: create a HTTP session to a server ``url`` Base url of the server ``alias`` Robot Framework alias to identify the session ``headers`` Dictionary of default headers ``cookies`` Dictionary of cookies ``client_certs`` ['client certificate', 'client key'] PEM files containing the client key and certificate ``timeout`` Connection timeout ``proxi...

## Create Custom Session

**Syntax**
```robot
Create Custom Session
```

**Description**
Create Session: create a HTTP session to a server ``url`` Base url of the server ``alias`` Robot Framework alias to identify the session ``headers`` Dictionary of default headers ``cookies`` Dictionary of cookies ``auth`` A Custom Authentication object to be passed on to the requests library. http://docs.python-requests.org/en/master/user/advanced/#custom...

## Create Digest Session

**Syntax**
```robot
Create Digest Session
```

**Description**
Create Session: create a HTTP session to a server ``url`` Base url of the server ``alias`` Robot Framework alias to identify the session ``headers`` Dictionary of default headers ``cookies`` Dictionary of cookies ``auth`` ['DOMAIN', 'username', 'password'] for NTLM Authentication ``timeout`` Connection timeout ``proxies`` Dictionary mapping protocol or pr...

## Create Ntlm Session

**Syntax**
```robot
Create Ntlm Session
```

**Description**
Create Session: create a HTTP session to a server ``url`` Base url of the server ``alias`` Robot Framework alias to identify the session ``headers`` Dictionary of default headers ``cookies`` Dictionary of cookies ``auth`` ['DOMAIN', 'username', 'password'] for NTLM Authentication ``timeout`` Connection timeout ``proxies`` Dictionary mapping protocol or pr...

## Create Session

**Syntax**
```robot
Create Session
```

**Description**
Create Session: create a HTTP session to a server ``alias`` Robot Framework alias to identify the session ``url`` Base url of the server ``headers`` Dictionary of default headers ``cookies`` Dictionary of cookies ``auth`` List of username & password for HTTP Basic Auth ``timeout`` Connection timeout ``proxies`` Dictionary mapping protocol or protocol and ...

## DELETE

**Syntax**
```robot
DELETE
```

**Description**
Sends a DELETE request. The endpoint used to send the request is the ``url`` parameter. By default this keyword fails if a status code with error values is returned in the response, this behavior can be modified using the ``expected_status`` and ``msg`` parameters, read more about it in `Status Should Be` keyword documentation. In order to disable this im...

## Delete All Sessions

**Syntax**
```robot
Delete All Sessions
```

**Description**
Removes all the session objects

## DELETE On Session

**Syntax**
```robot
DELETE On Session
```

**Description**
Sends a DELETE request on a previously created HTTP Session. Session will be identified using the ``alias`` name. The endpoint used to send the request is the ``url`` parameter. By default this keyword fails if a status code with error values is returned in the response, this behavior can be modified using the ``expected_status`` and ``msg`` parameters, r...

## Delete Request

**Syntax**
```robot
Delete Request
```

**Description**
*DEPRECATED* Please use `DELETE On Session` instead. Send a DELETE request on the session object found using the given `alias` ``alias`` that will be used to identify the Session object in the cache ``uri`` to send the DELETE request to ``json`` a value that will be json encoded and sent as request data if data is not specified ``headers`` a dictionary of...

## GET

**Syntax**
```robot
GET
```

**Description**
Sends a GET request. The endpoint used to retrieve the resource is the ``url``, while query string parameters can be passed as string, dictionary (or list of tuples or bytes) through the ``params``. By default this keyword fails if a status code with error values is returned in the response, this behavior can be modified using the ``expected_status`` and ...

## Get File For Streaming Upload

**Syntax**
```robot
Get File For Streaming Upload
```

**Description**
Opens and returns a file descriptor of a specified file to be passed as ``data`` parameter to other requests keywords. This allows streaming upload of large files without reading them into memory. File descriptor is binary mode and read only. Requests keywords will automatically close the file, if used outside this library it's up to the caller to close it.

## GET On Session

**Syntax**
```robot
GET On Session
```

**Description**
Sends a GET request on a previously created HTTP Session. Session will be identified using the ``alias`` name. The endpoint used to retrieve the resource is the ``url``, while query string parameters can be passed as string, dictionary (or list of tuples or bytes) through the ``params``. By default this keyword fails if a status code with error values is ...

## Get Request

**Syntax**
```robot
Get Request
```

**Description**
*DEPRECATED* Please use `GET On Session` instead. Send a GET request on the session object found using the given `alias` ``alias`` that will be used to identify the Session object in the cache ``uri`` to send the GET request to ``params`` url parameters to append to the uri ``headers`` a dictionary of headers to use with the request ``data`` a dictionary ...

## HEAD

**Syntax**
```robot
HEAD
```

**Description**
Sends a HEAD request. The endpoint used to retrieve the HTTP headers is the ``url``. ``allow_redirects`` parameter is not provided, it will be set to `False` (as opposed to the default behavior). By default this keyword fails if a status code with error values is returned in the response, this behavior can be modified using the ``expected_status`` and ``m...

## HEAD On Session

**Syntax**
```robot
HEAD On Session
```

**Description**
Sends a HEAD request on a previously created HTTP Session. Session will be identified using the ``alias`` name. The endpoint used to retrieve the HTTP headers is the ``url``. ``allow_redirects`` parameter is not provided, it will be set to `False` (as opposed to the default behavior). By default this keyword fails if a status code with error values is ret...

## Head Request

**Syntax**
```robot
Head Request
```

**Description**
*DEPRECATED* Please use `HEAD On Session` instead. Send a HEAD request on the session object found using the given `alias` ``alias`` that will be used to identify the Session object in the cache ``uri`` to send the HEAD request to ``allow_redirects`` Boolean. Set to True if POST/PUT/DELETE redirect following is allowed. ``headers`` a dictionary of headers...

## OPTIONS

**Syntax**
```robot
OPTIONS
```

**Description**
Sends a OPTIONS request. The endpoint used to retrieve the resource is the ``url``. By default this keyword fails if a status code with error values is returned in the response, this behavior can be modified using the ``expected_status`` and ``msg`` parameters, read more about it in `Status Should Be` keyword documentation. In order to disable this implic...

## OPTIONS On Session

**Syntax**
```robot
OPTIONS On Session
```

**Description**
Sends a OPTIONS request on a previously created HTTP Session. Session will be identified using the ``alias`` name. The endpoint used to retrieve the resource is the ``url``. By default this keyword fails if a status code with error values is returned in the response, this behavior can be modified using the ``expected_status`` and ``msg`` parameters, read ...

## Options Request

**Syntax**
```robot
Options Request
```

**Description**
*DEPRECATED* Please use `OPTIONS On Session` instead. Send an OPTIONS request on the session object found using the given `alias` ``alias`` that will be used to identify the Session object in the cache ``uri`` to send the OPTIONS request to ``allow_redirects`` Boolean. Set to True if POST/PUT/DELETE redirect following is allowed. ``headers`` a dictionary ...

## PATCH

**Syntax**
```robot
PATCH
```

**Description**
Sends a PUT request. The endpoint used to send the request is the ``url`` parameter, while its body can be passed using ``data`` or ``json`` parameters. ``data`` can be a dictionary, list of tuples, bytes, or file-like object. If you want to pass a json body pass a dictionary as ``json`` parameter. By default this keyword fails if a status code with error...

## PATCH On Session

**Syntax**
```robot
PATCH On Session
```

**Description**
Sends a PATCH request on a previously created HTTP Session. Session will be identified using the ``alias`` name. The endpoint used to send the request is the ``url`` parameter, while its body can be passed using ``data`` or ``json`` parameters. ``data`` can be a dictionary, list of tuples, bytes, or file-like object. If you want to pass a json body pass a...

## Patch Request

**Syntax**
```robot
Patch Request
```

**Description**
*DEPRECATED* Please use `PATCH On Session` instead. Send a PATCH request on the session object found using the given `alias` ``alias`` that will be used to identify the Session object in the cache ``uri`` to send the PATCH request to ``data`` a dictionary of key-value pairs that will be urlencoded and sent as PATCH data or binary data that is sent as the ...

## POST

**Syntax**
```robot
POST
```

**Description**
Sends a POST request. The endpoint used to send the request is the ``url`` parameter, while its body can be passed using ``data`` or ``json`` parameters. ``data`` can be a dictionary, list of tuples, bytes, or file-like object. If you want to pass a json body pass a dictionary as ``json`` parameter. By default this keyword fails if a status code with erro...

## POST On Session

**Syntax**
```robot
POST On Session
```

**Description**
Sends a POST request on a previously created HTTP Session. Session will be identified using the ``alias`` name. The endpoint used to send the request is the ``url`` parameter, while its body can be passed using ``data`` or ``json`` parameters. ``data`` can be a dictionary, list of tuples, bytes, or file-like object. If you want to pass a json body pass a ...

## Post Request

**Syntax**
```robot
Post Request
```

**Description**
*DEPRECATED* Please use `POST On Session` instead. Send a POST request on the session object found using the given `alias` ``alias`` that will be used to identify the Session object in the cache ``uri`` to send the POST request to ``data`` a dictionary of key-value pairs that will be urlencoded and sent as POST data or binary data that is sent as the raw ...

## PUT

**Syntax**
```robot
PUT
```

**Description**
Sends a PUT request. The endpoint used to send the request is the ``url`` parameter, while its body can be passed using ``data`` or ``json`` parameters. ``data`` can be a dictionary, list of tuples, bytes, or file-like object. If you want to pass a json body pass a dictionary as ``json`` parameter. By default this keyword fails if a status code with error...

## PUT On Session

**Syntax**
```robot
PUT On Session
```

**Description**
Sends a PUT request on a previously created HTTP Session. Session will be identified using the ``alias`` name. The endpoint used to send the request is the ``url`` parameter, while its body can be passed using ``data`` or ``json`` parameters. ``data`` can be a dictionary, list of tuples, bytes, or file-like object. If you want to pass a json body pass a d...

## Put Request

**Syntax**
```robot
Put Request
```

**Description**
*DEPRECATED* Please use `PUT On Session` instead. Send a PUT request on the session object found using the given `alias` ``alias`` that will be used to identify the Session object in the cache ``uri`` to send the PUT request to ``data`` a dictionary of key-value pairs that will be urlencoded and sent as PUT data or binary data that is sent as the raw body...

## Request Should Be Successful

**Syntax**
```robot
Request Should Be Successful
```

**Description**
Fails if response status code is a client or server error (4xx, 5xx). ``response`` is the output of other requests keywords like `GET On Session`. If omitted the last response will be used. In case of failure an HTTPError will be automatically raised. For a more versatile assert keyword see `Status Should Be`.

## Session Exists

**Syntax**
```robot
Session Exists
```

**Description**
Return True if the session has been already created ``alias`` that has been used to identify the Session object in the cache

## Status Should Be

**Syntax**
```robot
Status Should Be
```

**Description**
Fails if response status code is different than the expected. ``expected_status`` could be the code number as an integer or as string. But it could also be a named status code like 'ok', 'created', 'accepted' or 'bad request', 'not found' etc. ``response`` is the output of other requests keywords like `GET` or `GET On Session`. If omitted the last respons...

## To Json

**Syntax**
```robot
To Json
```

**Description**
*DEPRECATED* Please use ${resp.json()} instead. Have a look at the improved HTML output as pretty printing replacement. Convert a string to a JSON object ``content`` String content to convert into JSON ``pretty_print`` If defined, will output JSON is pretty print format

## Update Session

**Syntax**
```robot
Update Session
```

**Description**
Updates HTTP Session Headers and Cookies. Session will be identified using the ``alias`` name. Dictionary of ``headers`` and ``cookies`` to be updated and merged into session data.
