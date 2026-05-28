# SeleniumLibrary Keywords - Browser And Navigation

## Add Location Strategy

**Syntax**
```robot
Add Location Strategy
```

**Description**
Adds a custom location strategy. See `Custom locators` for information on how to create and use custom strategies. `Remove Location Strategy` can be used to remove a registered strategy. Location strategies are automatically removed after leaving the current scope by default. Setting ``persist`` to a true value (see...

## Close All Browsers

**Syntax**
```robot
Close All Browsers
```

**Description**
Closes all open browsers and resets the browser cache. After this keyword, new indexes returned from `Open Browser` keyword are reset to 1. This keyword should be used in test or suite teardown to make sure all browsers are closed.

## Close Browser

**Syntax**
```robot
Close Browser
```

**Description**
Closes the current browser.

## Close Window

**Syntax**
```robot
Close Window
```

**Description**
Closes currently opened and selected browser window/tab.

## Get Browser Aliases

**Syntax**
```robot
Get Browser Aliases
```

**Description**
Returns aliases of all active browser that has an alias as NormalizedDict. The dictionary contains the aliases as keys and the index as value. This can be accessed as dictionary ``${aliases.key}`` or as list ``@{aliases}[0]``. Example: | `Open Browser` | https://example.com | alias=BrowserA | | | `Open Browser` | ht...

## Get Browser Ids

**Syntax**
```robot
Get Browser Ids
```

**Description**
Returns index of all active browser as list. Example: | @{browser_ids}= | Get Browser Ids | | | | FOR | ${id} | IN | @{browser_ids} | | | @{window_titles}= | Get Window Titles | browser=${id} | | | Log | Browser ${id} has these windows: ${window_titles} | | | END | | | | See `Switch Browser` for more information and...

## Get Location

**Syntax**
```robot
Get Location
```

**Description**
Returns the current browser window URL.

## Get Locations

**Syntax**
```robot
Get Locations
```

**Description**
Returns and logs URLs of all windows of the selected browser. *Browser Scope:* The ``browser`` argument specifies the browser that shall return its windows information. - ``browser`` can be ``index_or_alias`` like in `Switch Browser`. - If ``browser`` is ``CURRENT`` (default, case-insensitive) the currently active b...

## Get Title

**Syntax**
```robot
Get Title
```

**Description**
Returns the title of the current page.

## Get Window Handles

**Syntax**
```robot
Get Window Handles
```

**Description**
Returns all child window handles of the selected browser as a list. Can be used as a list of windows to exclude with `Select Window`. How to select the ``browser`` scope of this keyword, see `Get Locations`. Prior to SeleniumLibrary 3.0, this keyword was named `List Windows`.

## Get Window Identifiers

**Syntax**
```robot
Get Window Identifiers
```

**Description**
Returns and logs id attributes of all windows of the selected browser. How to select the ``browser`` scope of this keyword, see `Get Locations`.

## Get Window Names

**Syntax**
```robot
Get Window Names
```

**Description**
Returns and logs names of all windows of the selected browser. How to select the ``browser`` scope of this keyword, see `Get Locations`.

## Get Window Position

**Syntax**
```robot
Get Window Position
```

**Description**
Returns current window position. The position is relative to the top left corner of the screen. Returned values are integers. See also `Set Window Position`. Example: | ${x} | ${y}= | `Get Window Position` |

## Get Window Size

**Syntax**
```robot
Get Window Size
```

**Description**
Returns current window width and height as integers. See also `Set Window Size`. If ``inner`` parameter is set to True, keyword returns HTML DOM window.innerWidth and window.innerHeight properties. See `Boolean arguments` for more details on how to set boolean arguments. The ``inner`` is new in SeleniumLibrary 4.0. ...

## Get Window Titles

**Syntax**
```robot
Get Window Titles
```

**Description**
Returns and logs titles of all windows of the selected browser. How to select the ``browser`` scope of this keyword, see `Get Locations`.

## Go To

**Syntax**
```robot
Go To
```

**Description**
Navigates the current browser window to the provided ``url``.

## Location Should Be

**Syntax**
```robot
Location Should Be
```

**Description**
Verifies that the current URL is exactly ``url``. The ``url`` argument contains the exact url that should exist in browser. The ``message`` argument can be used to override the default error message. ``message`` argument is new in SeleniumLibrary 3.2.0.

## Location Should Contain

**Syntax**
```robot
Location Should Contain
```

**Description**
Verifies that the current URL contains ``expected``. The ``expected`` argument contains the expected value in url. The ``message`` argument can be used to override the default error message. ``message`` argument is new in SeleniumLibrary 3.2.0.

## Log Location

**Syntax**
```robot
Log Location
```

**Description**
Logs and returns the current browser window URL.

## Log Title

**Syntax**
```robot
Log Title
```

**Description**
Logs and returns the title of the current page.

## Maximize Browser Window

**Syntax**
```robot
Maximize Browser Window
```

**Description**
Maximizes current browser window.

## Minimize Browser Window

**Syntax**
```robot
Minimize Browser Window
```

**Description**
Minimizes current browser window.

## Open Browser

**Syntax**
```robot
Open Browser
```

**Description**
Opens a new browser instance to the optional ``url``. The ``browser`` argument specifies which browser to use. The supported browsers are listed in the table below. The browser names are case-insensitive and some browsers have multiple supported names. | = Browser = | = Name(s) = | | Firefox | firefox, ff | | Google...

## Reload Page

**Syntax**
```robot
Reload Page
```

**Description**
Simulates user reloading page.

## Remove Location Strategy

**Syntax**
```robot
Remove Location Strategy
```

**Description**
Removes a previously added custom location strategy. See `Custom locators` for information on how to create and use custom strategies.

## Set Browser Implicit Wait

**Syntax**
```robot
Set Browser Implicit Wait
```

**Description**
Sets the implicit wait value used by Selenium. Same as `Set Selenium Implicit Wait` but only affects the current browser.

## Set Window Position

**Syntax**
```robot
Set Window Position
```

**Description**
Sets window position using ``x`` and ``y`` coordinates. The position is relative to the top left corner of the screen, but some browsers exclude possible task bar set by the operating system from the calculation. The actual position may thus be different with different browsers. Values can be given using strings con...

## Set Window Size

**Syntax**
```robot
Set Window Size
```

**Description**
Sets current windows size to given ``width`` and ``height``. Values can be given using strings containing numbers or by using actual numbers. See also `Get Window Size`. Browsers have a limit on their minimum size. Trying to set them smaller will cause the actual size to be bigger than the requested size. If ``inner...

## Switch Browser

**Syntax**
```robot
Switch Browser
```

**Description**
Switches between active browsers using ``index_or_alias``. Indices are returned by the `Open Browser` keyword and aliases can be given to it explicitly. Indices start from 1. Example: | `Open Browser` | http://google.com | ff | | `Location Should Be` | http://google.com | | | `Open Browser` | http://yahoo.com | ie |...

## Switch Window

**Syntax**
```robot
Switch Window
```

**Description**
Switches to browser window matching ``locator``. If the window is found, all subsequent commands use the selected window, until this keyword is used again. If the window is not found, this keyword fails. The previous windows handle is returned and can be used to switch back to it later. Notice that alerts should be ...

## Title Should Be

**Syntax**
```robot
Title Should Be
```

**Description**
Verifies that the current page title equals ``title``. The ``message`` argument can be used to override the default error message. ``message`` argument is new in SeleniumLibrary 3.1.

## Wait Until Location Contains

**Syntax**
```robot
Wait Until Location Contains
```

**Description**
Waits until the current URL contains ``expected``. The ``expected`` argument contains the expected value in url. Fails if ``timeout`` expires before the location contains. See the `Timeouts` section for more information about using timeouts and their default value. The ``message`` argument can be used to override th...

## Wait Until Location Does Not Contain

**Syntax**
```robot
Wait Until Location Does Not Contain
```

**Description**
Waits until the current URL does not contains ``location``. The ``location`` argument contains value not expected in url. Fails if ``timeout`` expires before the location not contains. See the `Timeouts` section for more information about using timeouts and their default value. The ``message`` argument can be used t...

## Wait Until Location Is

**Syntax**
```robot
Wait Until Location Is
```

**Description**
Waits until the current URL is ``expected``. The ``expected`` argument is the expected value in url. Fails if ``timeout`` expires before the location is. See the `Timeouts` section for more information about using timeouts and their default value. The ``message`` argument can be used to override the default error me...

## Wait Until Location Is Not

**Syntax**
```robot
Wait Until Location Is Not
```

**Description**
Waits until the current URL is not ``location``. The ``location`` argument is the unexpected value in url. Fails if ``timeout`` expires before the location is not. See the `Timeouts` section for more information about using timeouts and their default value. The ``message`` argument can be used to override the defaul...
