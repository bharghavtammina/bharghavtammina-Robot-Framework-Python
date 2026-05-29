# Cookies (JavaScript Side)

Note: SeleniumLibrary also has native cookie keywords (`Get Cookie`, `Add Cookie`, etc.).
These are JavaScript alternatives via `document.cookie`.

## Read all cookies as string

```robot
${cookies}=    Execute Javascript    return document.cookie;
Log            ${cookies}
```

## Set cookie (simple)

```robot
Execute Javascript    document.cookie='testmode=true; path=/';
```

## Set cookie with expiry

```robot
Execute Javascript    document.cookie='token=abc123; path=/; max-age=3600';
```

## Delete cookie (set expired)

```robot
Execute Javascript    document.cookie='token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT';
```

## Check cookie contains value

```robot
${has_token}=    Execute Javascript    return document.cookie.includes('token=');
```

## Important
- JS cookie access is limited compared to HTTP cookies
- HttpOnly cookies cannot be read by JavaScript
- Prefer Selenium cookie keywords for test setup when possible
