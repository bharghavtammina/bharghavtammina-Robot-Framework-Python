# SeleniumLibrary Keywords

## Add Cookie

**Syntax**
```robot
Add Cookie
```

**Description**
Adds a cookie to your current session. ``name`` and ``value`` are required, ``path``, ``domain``, ``secure`` and ``expiry`` are optional. Expiry supports the same formats as the [http://robotframework.org/robotframework/latest/libraries/DateTime.html|DateTime] library or an epoch timestamp. Example: | `Add Cookie` | foo | bar | | | `Add Cookie` | foo | ba...

## Add Location Strategy

**Syntax**
```robot
Add Location Strategy
```

**Description**
Adds a custom location strategy. See `Custom locators` for information on how to create and use custom strategies. `Remove Location Strategy` can be used to remove a registered strategy. Location strategies are automatically removed after leaving the current scope by default. Setting ``persist`` to a true value (see `Boolean arguments`) will cause the loc...

## Alert Should Be Present

**Syntax**
```robot
Alert Should Be Present
```

**Description**
Verifies that an alert is present and by default, accepts it. Fails if no alert is present. If ``text`` is a non-empty string, then it is used to verify alert's message. The alert is accepted by default, but that behavior can be controlled by using the ``action`` argument same way as with `Handle Alert`. ``timeout`` specifies how long to wait for the aler...

## Alert Should Not Be Present

**Syntax**
```robot
Alert Should Not Be Present
```

**Description**
Verifies that no alert is present. If the alert actually exists, the ``action`` argument determines how it should be handled. By default, the alert is accepted, but it can be also dismissed or left open the same way as with the `Handle Alert` keyword. ``timeout`` specifies how long to wait for the alert to appear. By default, is not waited for the alert a...

## Assign Id To Element

**Syntax**
```robot
Assign Id To Element
```

**Description**
Assigns a temporary ``id`` to the element specified by ``locator``. This is mainly useful if the locator is complicated and/or slow XPath expression and it is needed multiple times. Identifier expires when the page is reloaded. See the `Locating elements` section for details about the locator syntax. Example: | `Assign ID to Element` | //ul[@class='exampl...

## Capture Element Screenshot

**Syntax**
```robot
Capture Element Screenshot
```

**Description**
Captures a screenshot from the element identified by ``locator`` and embeds it into log file. See `Capture Page Screenshot` for details about ``filename`` argument. See the `Locating elements` section for details about the locator syntax. An absolute path to the created element screenshot is returned. If the ``filename`` equals to BASE64 (case insensitive...

## Capture Page Screenshot

**Syntax**
```robot
Capture Page Screenshot
```

**Description**
Takes a screenshot of the current page and embeds it into a log file. ``filename`` argument specifies the name of the file to write the screenshot into. The directory where screenshots are saved can be set when `importing` the library or by using the `Set Screenshot Directory` keyword. If the directory is not configured, screenshots are saved to the same ...

## Checkbox Should Be Selected

**Syntax**
```robot
Checkbox Should Be Selected
```

**Description**
Verifies checkbox ``locator`` is selected/checked. See the `Locating elements` section for details about the locator syntax.

## Checkbox Should Not Be Selected

**Syntax**
```robot
Checkbox Should Not Be Selected
```

**Description**
Verifies checkbox ``locator`` is not selected/checked. See the `Locating elements` section for details about the locator syntax.

## Choose File

**Syntax**
```robot
Choose File
```

**Description**
Inputs the ``file_path`` into the file input field ``locator``. This keyword is most often used to input files into upload forms. The keyword does not check ``file_path`` is the file or folder available on the machine where tests are executed. If the ``file_path`` points at a file and when using Selenium Grid, Selenium will [https://www.selenium.dev/selen...

## Clear Element Text

**Syntax**
```robot
Clear Element Text
```

**Description**
Clears the value of the text-input-element identified by ``locator``. See the `Locating elements` section for details about the locator syntax.

## Click Button

**Syntax**
```robot
Click Button
```

**Description**
Clicks the button identified by ``locator``. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, buttons are searched using ``id``, ``name``, and ``value``. See the `Click Element` keyword for details about the ``modifier`` argument. The ``modifier`` argument is new in SeleniumLibrary 3.3

## Click Element

**Syntax**
```robot
Click Element
```

**Description**
Click the element identified by ``locator``. See the `Locating elements` section for details about the locator syntax. The ``modifier`` argument can be used to pass [https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_common/selenium.webdriver.common.keys.html#module-selenium.webdriver.common.keys|Selenium Keys] when clicking the element. The...

## Click Element At Coordinates

**Syntax**
```robot
Click Element At Coordinates
```

**Description**
Click the element ``locator`` at ``xoffset/yoffset``. The Cursor is moved and the center of the element and x/y coordinates are calculated from that point. See the `Locating elements` section for details about the locator syntax.

## Click Image

**Syntax**
```robot
Click Image
```

**Description**
Clicks an image identified by ``locator``. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, images are searched using ``id``, ``name``, ``src`` and ``alt``. See the `Click Element` keyword for details about the ``modifier`` argument. The ``modifier`` argument is new in SeleniumLibrary 3.3

## Click Link

**Syntax**
```robot
Click Link
```

**Description**
Clicks a link identified by ``locator``. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, links are searched using ``id``, ``name``, ``href`` and the link text. See the `Click Element` keyword for details about the ``modifier`` argument. The ``modifier`` argument is new in SeleniumLibrary 3.3

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

## Cover Element

**Syntax**
```robot
Cover Element
```

**Description**
Will cover elements identified by ``locator`` with a blue div without breaking page layout. See the `Locating elements` section for details about the locator syntax. New in SeleniumLibrary 3.3.0 Example: |`Cover Element` | css:div#container |

## Create Webdriver

**Syntax**
```robot
Create Webdriver
```

**Description**
Creates an instance of Selenium WebDriver. Like `Open Browser`, but allows passing arguments to the created WebDriver instance directly. This keyword should only be used if the functionality provided by `Open Browser` is not adequate. ``driver_name`` must be a WebDriver implementation name like Firefox, Chrome, Ie, Edge, Safari, or Remote. The initialized...

## Current Frame Should Contain

**Syntax**
```robot
Current Frame Should Contain
```

**Description**
Verifies that the current frame contains ``text``. See `Page Should Contain` for an explanation about the ``loglevel`` argument. Prior to SeleniumLibrary 3.0 this keyword was named `Current Frame Contains`.

## Current Frame Should Not Contain

**Syntax**
```robot
Current Frame Should Not Contain
```

**Description**
Verifies that the current frame does not contain ``text``. See `Page Should Contain` for an explanation about the ``loglevel`` argument.

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

## Double Click Element

**Syntax**
```robot
Double Click Element
```

**Description**
Double clicks the element identified by ``locator``. See the `Locating elements` section for details about the locator syntax.

## Drag And Drop

**Syntax**
```robot
Drag And Drop
```

**Description**
Drags the element identified by ``locator`` into the ``target`` element. The ``locator`` argument is the locator of the dragged element and the ``target`` is the locator of the target. See the `Locating elements` section for details about the locator syntax. Example: | `Drag And Drop` | css:div#element | css:div.target |

## Drag And Drop Across Frames

**Syntax**
```robot
Drag And Drop Across Frames
```

**Description**
Drags an element and drops it onto a target element across frame boundaries. The ``locator`` argument is the locator of the element to drag. The ``target`` argument is the locator of the drop target. The ``target_frame`` argument is the locator of the iframe containing the target. The optional ``source_frame`` argument is the locator of the iframe contain...

## Drag And Drop By Offset

**Syntax**
```robot
Drag And Drop By Offset
```

**Description**
Drags the element identified with ``locator`` by ``xoffset/yoffset``. See the `Locating elements` section for details about the locator syntax. The element will be moved by ``xoffset`` and ``yoffset``, each of which is a negative or positive number specifying the offset. Example: | `Drag And Drop By Offset` | myElem | 50 | -35 | # Move myElem 50px right a...

## Element Attribute Value Should Be

**Syntax**
```robot
Element Attribute Value Should Be
```

**Description**
Verifies element identified by ``locator`` contains expected attribute value. See the `Locating elements` section for details about the locator syntax. Example: `Element Attribute Value Should Be` | css:img | href | value New in SeleniumLibrary 3.2.

## Element Should Be Disabled

**Syntax**
```robot
Element Should Be Disabled
```

**Description**
Verifies that element identified by ``locator`` is disabled. This keyword considers also elements that are read-only to be disabled. See the `Locating elements` section for details about the locator syntax.

## Element Should Be Enabled

**Syntax**
```robot
Element Should Be Enabled
```

**Description**
Verifies that element identified by ``locator`` is enabled. This keyword considers also elements that are read-only to be disabled. See the `Locating elements` section for details about the locator syntax.

## Element Should Be Focused

**Syntax**
```robot
Element Should Be Focused
```

**Description**
Verifies that element identified by ``locator`` is focused. See the `Locating elements` section for details about the locator syntax. New in SeleniumLibrary 3.0.

## Element Should Be Visible

**Syntax**
```robot
Element Should Be Visible
```

**Description**
Verifies that the element identified by ``locator`` is visible. Herein, visible means that the element is logically visible, not optically visible in the current browser viewport. For example, an element that carries ``display:none`` is not logically visible, so using this keyword on that element would fail. See the `Locating elements` section for details...

## Element Should Contain

**Syntax**
```robot
Element Should Contain
```

**Description**
Verifies that element ``locator`` contains text ``expected``. See the `Locating elements` section for details about the locator syntax. The ``message`` argument can be used to override the default error message. The ``ignore_case`` argument can be set to True to compare case insensitive, default is False. New in SeleniumLibrary 3.1. ``ignore_case`` argume...

## Element Should Not Be Visible

**Syntax**
```robot
Element Should Not Be Visible
```

**Description**
Verifies that the element identified by ``locator`` is NOT visible. Passes if the element does not exists. See `Element Should Be Visible` for more information about visibility and supported arguments.

## Element Should Not Contain

**Syntax**
```robot
Element Should Not Contain
```

**Description**
Verifies that element ``locator`` does not contain text ``expected``. See the `Locating elements` section for details about the locator syntax. The ``message`` argument can be used to override the default error message. The ``ignore_case`` argument can be set to True to compare case insensitive, default is False. ``ignore_case`` argument new in SeleniumLi...

## Element Text Should Be

**Syntax**
```robot
Element Text Should Be
```

**Description**
Verifies that element ``locator`` contains exact the text ``expected``. See the `Locating elements` section for details about the locator syntax. The ``message`` argument can be used to override the default error message. The ``ignore_case`` argument can be set to True to compare case insensitive, default is False. ``ignore_case`` argument is new in Selen...

## Element Text Should Not Be

**Syntax**
```robot
Element Text Should Not Be
```

**Description**
Verifies that element ``locator`` does not contain exact the text ``not_expected``. See the `Locating elements` section for details about the locator syntax. The ``message`` argument can be used to override the default error message. The ``ignore_case`` argument can be set to True to compare case insensitive, default is False. New in SeleniumLibrary 3.1.1

## Execute Async Javascript

**Syntax**
```robot
Execute Async Javascript
```

**Description**
Executes asynchronous JavaScript code with possible arguments. Similar to `Execute Javascript` except that scripts executed with this keyword must explicitly signal they are finished by invoking the provided callback. This callback is always injected into the executed function as the last argument. Scripts must complete within the script timeout or this k...

## Execute Javascript

**Syntax**
```robot
Execute Javascript
```

**Description**
Executes the given JavaScript code with possible arguments. ``code`` may be divided into multiple cells in the test data and ``code`` may contain multiple lines of code and arguments. In that case, the JavaScript code parts are concatenated together without adding spaces and optional arguments are separated from ``code``. If ``code`` is a path to an exist...

## Frame Should Contain

**Syntax**
```robot
Frame Should Contain
```

**Description**
Verifies that frame identified by ``locator`` contains ``text``. See the `Locating elements` section for details about the locator syntax. See `Page Should Contain` for an explanation about the ``loglevel`` argument.

## Get Action Chain Delay

**Syntax**
```robot
Get Action Chain Delay
```

**Description**
Gets the currently stored value for chain_delay_value in timestr format.

## Get All Links

**Syntax**
```robot
Get All Links
```

**Description**
Returns a list containing ids of all links found in current page. If a link has no id, an empty string will be in the list instead.

## Get Browser Aliases

**Syntax**
```robot
Get Browser Aliases
```

**Description**
Returns aliases of all active browser that has an alias as NormalizedDict. The dictionary contains the aliases as keys and the index as value. This can be accessed as dictionary ``${aliases.key}`` or as list ``@{aliases}[0]``. Example: | `Open Browser` | https://example.com | alias=BrowserA | | | `Open Browser` | https://example.com | alias=BrowserB | | |...

## Get Browser Ids

**Syntax**
```robot
Get Browser Ids
```

**Description**
Returns index of all active browser as list. Example: | @{browser_ids}= | Get Browser Ids | | | | FOR | ${id} | IN | @{browser_ids} | | | @{window_titles}= | Get Window Titles | browser=${id} | | | Log | Browser ${id} has these windows: ${window_titles} | | | END | | | | See `Switch Browser` for more information and examples. New in SeleniumLibrary 4.0

## Get Cookie

**Syntax**
```robot
Get Cookie
```

**Description**
Returns information of cookie with ``name`` as an object. If no cookie is found with ``name``, keyword fails. The cookie object contains details about the cookie. Attributes available in the object are documented in the table below. | = Attribute = | = Explanation = | | name | The name of a cookie. | | value | Value of the cookie. | | path | Indicates a U...

## Get Cookies

**Syntax**
```robot
Get Cookies
```

**Description**
Returns all cookies of the current page. If ``as_dict`` argument evaluates as false, see `Boolean arguments` for more details, then cookie information is returned as a single string in format ``name1=value1; name2=value2; name3=value3``. When ``as_dict`` argument evaluates as true, cookie information is returned as Robot Framework dictionary format. The s...

## Get CSS Property Value

**Syntax**
```robot
Get CSS Property Value
```

**Description**
Returns the computed value of ``css_property`` from the element ``locator``. See the `Locating elements` section for details about the locator syntax. The value returned is the browser-computed CSS value of the property. For example, colors are often returned in ``rgba(...)`` format and sizes are typically returned in pixels. Example: | ${color}= | `Get C...

## Get Dom Attribute

**Syntax**
```robot
Get Dom Attribute
```

**Description**
Returns the value of ``attribute`` from the element ``locator``. `Get DOM Attribute` keyword only returns attributes declared within the element's HTML markup. If the requested attribute is not there, the keyword returns ${None}. See the `Locating elements` section for details about the locator syntax. Example: | ${id}= | `Get DOM Attribute` | css:h1 | id |

## Get Element Attribute

**Syntax**
```robot
Get Element Attribute
```

**Description**
Returns the value of ``attribute`` from the element ``locator``. See the `Locating elements` section for details about the locator syntax. Example: | ${id}= | `Get Element Attribute` | css:h1 | id | Passing attribute name as part of the ``locator`` was removed in SeleniumLibrary 3.2. The explicit ``attribute`` argument should be used instead.

## Get Element Count

**Syntax**
```robot
Get Element Count
```

**Description**
Returns the number of elements matching ``locator``. If you wish to assert the number of matching elements, use `Page Should Contain Element` with ``limit`` argument. Keyword will always return an integer. Example: | ${count} = | `Get Element Count` | name:div_name | | `Should Be True` | ${count} > 2 | | New in SeleniumLibrary 3.0.

## Get Element Size

**Syntax**
```robot
Get Element Size
```

**Description**
Returns width and height of the element identified by ``locator``. See the `Locating elements` section for details about the locator syntax. Both width and height are returned as integers. Example: | ${width} | ${height} = | `Get Element Size` | css:div#container |

## Get Horizontal Position

**Syntax**
```robot
Get Horizontal Position
```

**Description**
Returns the horizontal position of the element identified by ``locator``. See the `Locating elements` section for details about the locator syntax. The position is returned in pixels off the left side of the page, as an integer. See also `Get Vertical Position`.

## Get List Items

**Syntax**
```robot
Get List Items
```

**Description**
Returns all labels or values of selection list ``locator``. See the `Locating elements` section for details about the locator syntax. Returns visible labels by default, but values can be returned by setting the ``values`` argument to a true value (see `Boolean arguments`). Example: | ${labels} = | `Get List Items` | mylist | | | ${values} = | `Get List It...

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
Returns and logs URLs of all windows of the selected browser. *Browser Scope:* The ``browser`` argument specifies the browser that shall return its windows information. - ``browser`` can be ``index_or_alias`` like in `Switch Browser`. - If ``browser`` is ``CURRENT`` (default, case-insensitive) the currently active browser is selected. - If ``browser`` is ...

## Get Property

**Syntax**
```robot
Get Property
```

**Description**
Returns the value of ``property`` from the element ``locator``. See the `Locating elements` section for details about the locator syntax. Example: | ${text_length}= | `Get Property` | css:h1 | text_length |

## Get Selected List Label

**Syntax**
```robot
Get Selected List Label
```

**Description**
Returns the label of selected option from selection list ``locator``. If there are multiple selected options, the label of the first option is returned. See the `Locating elements` section for details about the locator syntax.

## Get Selected List Labels

**Syntax**
```robot
Get Selected List Labels
```

**Description**
Returns labels of selected options from selection list ``locator``. Starting from SeleniumLibrary 3.0, returns an empty list if there are no selections. In earlier versions, this caused an error. See the `Locating elements` section for details about the locator syntax.

## Get Selected List Value

**Syntax**
```robot
Get Selected List Value
```

**Description**
Returns the value of selected option from selection list ``locator``. If there are multiple selected options, the value of the first option is returned. See the `Locating elements` section for details about the locator syntax.

## Get Selected List Values

**Syntax**
```robot
Get Selected List Values
```

**Description**
Returns values of selected options from selection list ``locator``. Starting from SeleniumLibrary 3.0, returns an empty list if there are no selections. In earlier versions, this caused an error. See the `Locating elements` section for details about the locator syntax.

## Get Selenium Implicit Wait

**Syntax**
```robot
Get Selenium Implicit Wait
```

**Description**
Gets the implicit wait value used by Selenium. The value is returned as a human-readable string like ``1 second``. See the `Implicit wait` section above for more information.

## Get Selenium Page Load Timeout

**Syntax**
```robot
Get Selenium Page Load Timeout
```

**Description**
Gets the time to wait for a page load to complete before raising a timeout exception. The value is returned as a human-readable string like ``1 second``. See the `Page load` section above for more information. New in SeleniumLibrary 6.1

## Get Selenium Speed

**Syntax**
```robot
Get Selenium Speed
```

**Description**
Gets the delay that is waited after each Selenium command. The value is returned as a human-readable string like ``1 second``. See the `Selenium Speed` section above for more information.

## Get Selenium Timeout

**Syntax**
```robot
Get Selenium Timeout
```

**Description**
Gets the timeout that is used by various keywords. The value is returned as a human-readable string like ``1 second``. See the `Timeout` section above for more information.

## Get Session Id

**Syntax**
```robot
Get Session Id
```

**Description**
Returns the currently active browser session id. New in SeleniumLibrary 3.2

## Get Source

**Syntax**
```robot
Get Source
```

**Description**
Returns the entire HTML source of the current page or frame.

## Get Table Cell

**Syntax**
```robot
Get Table Cell
```

**Description**
Returns contents of a table cell. The table is located using the ``locator`` argument and its cell found using ``row`` and ``column``. See the `Locating elements` section for details about the locator syntax. Both row and column indexes start from 1, and header and footer rows are included in the count. It is possible to refer to rows and columns from the...

## Get Text

**Syntax**
```robot
Get Text
```

**Description**
Returns the text value of the element identified by ``locator``. See the `Locating elements` section for details about the locator syntax.

## Get Title

**Syntax**
```robot
Get Title
```

**Description**
Returns the title of the current page.

## Get Value

**Syntax**
```robot
Get Value
```

**Description**
Returns the value attribute of the element identified by ``locator``. See the `Locating elements` section for details about the locator syntax.

## Get Vertical Position

**Syntax**
```robot
Get Vertical Position
```

**Description**
Returns the vertical position of the element identified by ``locator``. See the `Locating elements` section for details about the locator syntax. The position is returned in pixels off the top of the page, as an integer. See also `Get Horizontal Position`.

## Get WebElement

**Syntax**
```robot
Get WebElement
```

**Description**
Returns the first WebElement matching the given ``locator``. See the `Locating elements` section for details about the locator syntax.

## Get WebElements

**Syntax**
```robot
Get WebElements
```

**Description**
Returns a list of WebElement objects matching the ``locator``. See the `Locating elements` section for details about the locator syntax. Starting from SeleniumLibrary 3.0, the keyword returns an empty list if there are no matching elements. In previous releases, the keyword failed in this case.

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
Returns current window width and height as integers. See also `Set Window Size`. If ``inner`` parameter is set to True, keyword returns HTML DOM window.innerWidth and window.innerHeight properties. See `Boolean arguments` for more details on how to set boolean arguments. The ``inner`` is new in SeleniumLibrary 4.0. Example: | ${width} | ${height}= | `Get ...

## Get Window Titles

**Syntax**
```robot
Get Window Titles
```

**Description**
Returns and logs titles of all windows of the selected browser. How to select the ``browser`` scope of this keyword, see `Get Locations`.

## Go Back

**Syntax**
```robot
Go Back
```

**Description**
Simulates the user clicking the back button on their browser.

## Go To

**Syntax**
```robot
Go To
```

**Description**
Navigates the current browser window to the provided ``url``.

## Handle Alert

**Syntax**
```robot
Handle Alert
```

**Description**
Handles the current alert and returns its message. By default, the alert is accepted, but this can be controlled with the ``action`` argument that supports the following case-insensitive values: - ``ACCEPT``: Accept the alert i.e. press ``Ok``. Default. - ``DISMISS``: Dismiss the alert i.e. press ``Cancel``. - ``LEAVE``: Leave the alert open. The ``timeou...

## Input Password

**Syntax**
```robot
Input Password
```

**Description**
Types the given password into the text field identified by ``locator``. See the `Locating elements` section for details about the locator syntax. See `Input Text` for ``clear`` argument details. Difference compared to `Input Text` is that this keyword does not log the given password on the INFO level. Notice that if you use the keyword like | Input Passwo...

## Input Text

**Syntax**
```robot
Input Text
```

**Description**
Types the given ``text`` into the text field identified by ``locator``. When ``clear`` is true, the input element is cleared before the text is typed into the element. When false, the previous text is not cleared from the element. Use `Input Password` if you do not want the given ``text`` to be logged. This keyword supports Robot Framework 7.4 [https://ro...

## Input Text Into Alert

**Syntax**
```robot
Input Text Into Alert
```

**Description**
Types the given ``text`` into an input field in an alert. The alert is accepted by default, but that behavior can be controlled by using the ``action`` argument same way as with `Handle Alert`. ``timeout`` specifies how long to wait for the alert to appear. If it is not given, the global default `timeout` is used instead. New in SeleniumLibrary 3.0.

## List Selection Should Be

**Syntax**
```robot
List Selection Should Be
```

**Description**
Verifies selection list ``locator`` has ``expected`` options selected. It is possible to give expected options both as visible labels and as values. Starting from SeleniumLibrary 3.0, mixing labels and values is not possible. Order of the selected options is not validated. If no expected options are given, validates that the list has no selections. A more...

## List Should Have No Selections

**Syntax**
```robot
List Should Have No Selections
```

**Description**
Verifies selection list ``locator`` has no options selected. See the `Locating elements` section for details about the locator syntax.

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

## Log Source

**Syntax**
```robot
Log Source
```

**Description**
Logs and returns the HTML source of the current page or frame. The ``loglevel`` argument defines the used log level. Valid log levels are ``WARN``, ``INFO`` (default), ``DEBUG``, ``TRACE`` and ``NONE`` (no logging).

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

## Mouse Down

**Syntax**
```robot
Mouse Down
```

**Description**
Simulates pressing the left mouse button on the element ``locator``. See the `Locating elements` section for details about the locator syntax. The element is pressed without releasing the mouse button. See also the more specific keywords `Mouse Down On Image` and `Mouse Down On Link`.

## Mouse Down On Image

**Syntax**
```robot
Mouse Down On Image
```

**Description**
Simulates a mouse down event on an image identified by ``locator``. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, images are searched using ``id``, ``name``, ``src`` and ``alt``.

## Mouse Down On Link

**Syntax**
```robot
Mouse Down On Link
```

**Description**
Simulates a mouse down event on a link identified by ``locator``. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, links are searched using ``id``, ``name``, ``href`` and the link text.

## Mouse Out

**Syntax**
```robot
Mouse Out
```

**Description**
Simulates moving the mouse away from the element ``locator``. See the `Locating elements` section for details about the locator syntax.

## Mouse Over

**Syntax**
```robot
Mouse Over
```

**Description**
Simulates hovering the mouse over the element ``locator``. See the `Locating elements` section for details about the locator syntax.

## Mouse Up

**Syntax**
```robot
Mouse Up
```

**Description**
Simulates releasing the left mouse button on the element ``locator``. See the `Locating elements` section for details about the locator syntax.

## Open Browser

**Syntax**
```robot
Open Browser
```

**Description**
Opens a new browser instance to the optional ``url``. The ``browser`` argument specifies which browser to use. The supported browsers are listed in the table below. The browser names are case-insensitive and some browsers have multiple supported names. | = Browser = | = Name(s) = | | Firefox | firefox, ff | | Google Chrome | googlechrome, chrome, gc | | H...

## Open Context Menu

**Syntax**
```robot
Open Context Menu
```

**Description**
Opens the context menu on the element identified by ``locator``.

## Page Should Contain

**Syntax**
```robot
Page Should Contain
```

**Description**
Verifies that current page contains ``text``. If this keyword fails, it automatically logs the page source using the log level specified with the optional ``loglevel`` argument. Valid log levels are ``TRACE`` (default), ``DEBUG``, ``INFO``, ``WARN``, and ``NONE``. If the log level is ``NONE`` or below the current active log level the source will not be lo...

## Page Should Contain Button

**Syntax**
```robot
Page Should Contain Button
```

**Description**
Verifies button ``locator`` is found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, buttons are searched using ``id``, ``name``, and ``value``.

## Page Should Contain Checkbox

**Syntax**
```robot
Page Should Contain Checkbox
```

**Description**
Verifies checkbox ``locator`` is found from the current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax.

## Page Should Contain Element

**Syntax**
```robot
Page Should Contain Element
```

**Description**
Verifies that element ``locator`` is found on the current page. See the `Locating elements` section for details about the locator syntax. The ``message`` argument can be used to override the default error message. The ``limit`` argument can used to define how many elements the page should contain. When ``limit`` is ``None`` (default) page can contain one ...

## Page Should Contain Image

**Syntax**
```robot
Page Should Contain Image
```

**Description**
Verifies image identified by ``locator`` is found from current page. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, images are searched using ``id``, ``name``, ``src`` and ``alt``. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments.

## Page Should Contain Link

**Syntax**
```robot
Page Should Contain Link
```

**Description**
Verifies link identified by ``locator`` is found from current page. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, links are searched using ``id``, ``name``, ``href`` and the link text. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments.

## Page Should Contain List

**Syntax**
```robot
Page Should Contain List
```

**Description**
Verifies selection list ``locator`` is found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax.

## Page Should Contain Radio Button

**Syntax**
```robot
Page Should Contain Radio Button
```

**Description**
Verifies radio button ``locator`` is found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, radio buttons are searched using ``id``, ``name`` and ``value``.

## Page Should Contain Textfield

**Syntax**
```robot
Page Should Contain Textfield
```

**Description**
Verifies text field ``locator`` is found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax.

## Page Should Not Contain

**Syntax**
```robot
Page Should Not Contain
```

**Description**
Verifies the current page does not contain ``text``. See `Page Should Contain` for an explanation about the ``loglevel`` argument.

## Page Should Not Contain Button

**Syntax**
```robot
Page Should Not Contain Button
```

**Description**
Verifies button ``locator`` is not found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, buttons are searched using ``id``, ``name``, and ``value``.

## Page Should Not Contain Checkbox

**Syntax**
```robot
Page Should Not Contain Checkbox
```

**Description**
Verifies checkbox ``locator`` is not found from the current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax.

## Page Should Not Contain Element

**Syntax**
```robot
Page Should Not Contain Element
```

**Description**
Verifies that element ``locator`` is not found on the current page. See the `Locating elements` section for details about the locator syntax. See `Page Should Contain` for an explanation about ``message`` and ``loglevel`` arguments.

## Page Should Not Contain Image

**Syntax**
```robot
Page Should Not Contain Image
```

**Description**
Verifies image identified by ``locator`` is not found from current page. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, images are searched using ``id``, ``name``, ``src`` and ``alt``. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments.

## Page Should Not Contain Link

**Syntax**
```robot
Page Should Not Contain Link
```

**Description**
Verifies link identified by ``locator`` is not found from current page. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, links are searched using ``id``, ``name``, ``href`` and the link text. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments.

## Page Should Not Contain List

**Syntax**
```robot
Page Should Not Contain List
```

**Description**
Verifies selection list ``locator`` is not found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax.

## Page Should Not Contain Radio Button

**Syntax**
```robot
Page Should Not Contain Radio Button
```

**Description**
Verifies radio button ``locator`` is not found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, radio buttons are searched using ``id``, ``name`` and ``value``.

## Page Should Not Contain Textfield

**Syntax**
```robot
Page Should Not Contain Textfield
```

**Description**
Verifies text field ``locator`` is not found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax.

## Press Key

**Syntax**
```robot
Press Key
```

**Description**
Simulates user pressing key on element identified by ``locator``. See the `Locating elements` section for details about the locator syntax. ``key`` is either a single character, a string, or a numerical ASCII code of the key lead by '\'. Examples: | `Press Key` | text_field | q | | `Press Key` | text_field | abcde | | `Press Key` | login_button | \13 | # ...

## Press Keys

**Syntax**
```robot
Press Keys
```

**Description**
Simulates the user pressing key(s) to an element or on the active browser. If ``locator`` evaluates as false, see `Boolean arguments` for more details, then the ``keys`` are sent to the currently active browser. Otherwise element is searched and ``keys`` are send to the element identified by the ``locator``. In later case, keyword fails if element is not ...

## Print Page As Pdf

**Syntax**
```robot
Print Page As Pdf
```

**Description**
Print the current page as a PDF ``page_ranges`` defaults to `['-']` or "all" pages. ``page_ranges`` takes a list of strings indicating the ranges. The page size defaults to 21.59 for ``page_width`` and 27.94 for ``page_height``. This is the equivalent size of US-Letter. The assumed units on these parameters is centimeters. The default margin for top, left...

## Radio Button Should Be Set To

**Syntax**
```robot
Radio Button Should Be Set To
```

**Description**
Verifies radio button group ``group_name`` is set to ``value``. ``group_name`` is the ``name`` of the radio button group.

## Radio Button Should Not Be Selected

**Syntax**
```robot
Radio Button Should Not Be Selected
```

**Description**
Verifies radio button group ``group_name`` has no selection. ``group_name`` is the ``name`` of the radio button group.

## Register Keyword To Run On Failure

**Syntax**
```robot
Register Keyword To Run On Failure
```

**Description**
Sets the keyword to execute, when a SeleniumLibrary keyword fails. ``keyword`` is the name of a keyword that will be executed if a SeleniumLibrary keyword fails. It is possible to use any available keyword, including user keywords or keywords from other libraries, but the keyword must not take any arguments. The initial keyword to use is set when `importi...

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

## Scroll Element Into View

**Syntax**
```robot
Scroll Element Into View
```

**Description**
Scrolls the element identified by ``locator`` into view. See the `Locating elements` section for details about the locator syntax. New in SeleniumLibrary 3.2.0

## Select All From List

**Syntax**
```robot
Select All From List
```

**Description**
Selects all options from multi-selection list ``locator``. See the `Locating elements` section for details about the locator syntax.

## Select Checkbox

**Syntax**
```robot
Select Checkbox
```

**Description**
Selects the checkbox identified by ``locator``. Does nothing if checkbox is already selected. See the `Locating elements` section for details about the locator syntax.

## Select Frame

**Syntax**
```robot
Select Frame
```

**Description**
Sets frame identified by ``locator`` as the current frame. See the `Locating elements` section for details about the locator syntax. Works both with frames and iframes. Use `Unselect Frame` to cancel the frame selection and return to the main frame. Example: | `Select Frame` | top-frame | # Select frame with id or name 'top-frame' | | `Click Link` | examp...

## Select From List By Index

**Syntax**
```robot
Select From List By Index
```

**Description**
Selects options from selection list ``locator`` by ``indexes``. Indexes of list options start from 0. If more than one option is given for a single-selection list, the last value will be selected. With multi-selection lists all specified options are selected, but possible old selections are not cleared. See the `Locating elements` section for details abou...

## Select From List By Label

**Syntax**
```robot
Select From List By Label
```

**Description**
Selects options from selection list ``locator`` by ``labels``. If more than one option is given for a single-selection list, the last value will be selected. With multi-selection lists all specified options are selected, but possible old selections are not cleared. See the `Locating elements` section for details about the locator syntax.

## Select From List By Value

**Syntax**
```robot
Select From List By Value
```

**Description**
Selects options from selection list ``locator`` by ``values``. If more than one option is given for a single-selection list, the last value will be selected. With multi-selection lists all specified options are selected, but possible old selections are not cleared. See the `Locating elements` section for details about the locator syntax.

## Select Radio Button

**Syntax**
```robot
Select Radio Button
```

**Description**
Sets the radio button group ``group_name`` to ``value``. The radio button to be selected is located by two arguments: - ``group_name`` is the name of the radio button group. - ``value`` is the ``id`` or ``value`` attribute of the actual radio button. Examples: | `Select Radio Button` | size | XL | | `Select Radio Button` | contact | email |

## Set Action Chain Delay

**Syntax**
```robot
Set Action Chain Delay
```

**Description**
Sets the duration of delay in ActionChains() used by SeleniumLibrary. The value can be given as a number that is considered to be seconds or as a human-readable string like ``1 second``. Value is always stored as milliseconds internally. The previous value is returned and can be used to restore the original value later if needed.

## Set Browser Implicit Wait

**Syntax**
```robot
Set Browser Implicit Wait
```

**Description**
Sets the implicit wait value used by Selenium. Same as `Set Selenium Implicit Wait` but only affects the current browser.

## Set Focus To Element

**Syntax**
```robot
Set Focus To Element
```

**Description**
Sets the focus to the element identified by ``locator``. See the `Locating elements` section for details about the locator syntax. Prior to SeleniumLibrary 3.0 this keyword was named `Focus`.

## Set Screenshot Directory

**Syntax**
```robot
Set Screenshot Directory
```

**Description**
Sets the directory for captured screenshots. ``path`` argument specifies the absolute path to a directory where the screenshots should be written to. If the directory does not exist, it will be created. The directory can also be set when `importing` the library. If it is not configured anywhere, screenshots are saved to the same directory where Robot Fram...

## Set Selenium Implicit Wait

**Syntax**
```robot
Set Selenium Implicit Wait
```

**Description**
Sets the implicit wait value used by Selenium. The value can be given as a number that is considered to be seconds or as a human-readable string like ``1 second``. The previous value is returned and can be used to restore the original value later if needed. This keyword sets the implicit wait for all opened browsers. Use `Set Browser Implicit Wait` to set...

## Set Selenium Page Load Timeout

**Syntax**
```robot
Set Selenium Page Load Timeout
```

**Description**
Sets the page load timeout value used by Selenium. The value can be given as a number that is considered to be seconds or as a human-readable string like ``1 second``. The previous value is returned and can be used to restore the original value later if needed. In contrast to `Set Selenium Timeout` and `Set Selenium Implicit Wait`, this keywords sets the ...

## Set Selenium Speed

**Syntax**
```robot
Set Selenium Speed
```

**Description**
Sets the delay that is waited after each Selenium command. The value can be given as a number that is considered to be seconds or as a human-readable string like ``1 second``. The previous value is returned and can be used to restore the original value later if needed. See the `Selenium Speed` section above for more information. Example: | `Set Selenium S...

## Set Selenium Timeout

**Syntax**
```robot
Set Selenium Timeout
```

**Description**
Sets the timeout that is used by various keywords. The value can be given as a number that is considered to be seconds or as a human-readable string like ``1 second``. The previous value is returned and can be used to restore the original value later if needed. See the `Timeout` section above for more information. Example: | ${orig timeout} = | `Set Selen...

## Set Window Position

**Syntax**
```robot
Set Window Position
```

**Description**
Sets window position using ``x`` and ``y`` coordinates. The position is relative to the top left corner of the screen, but some browsers exclude possible task bar set by the operating system from the calculation. The actual position may thus be different with different browsers. Values can be given using strings containing numbers or by using actual numbe...

## Set Window Size

**Syntax**
```robot
Set Window Size
```

**Description**
Sets current windows size to given ``width`` and ``height``. Values can be given using strings containing numbers or by using actual numbers. See also `Get Window Size`. Browsers have a limit on their minimum size. Trying to set them smaller will cause the actual size to be bigger than the requested size. If ``inner`` parameter is set to True, keyword set...

## Simulate Event

**Syntax**
```robot
Simulate Event
```

**Description**
Simulates ``event`` on the element identified by ``locator``. This keyword is useful if element has ``OnEvent`` handler that needs to be explicitly invoked. See the `Locating elements` section for details about the locator syntax. Prior to SeleniumLibrary 3.0 this keyword was named `Simulate`.

## Submit Form

**Syntax**
```robot
Submit Form
```

**Description**
Submits a form identified by ``locator``. If ``locator`` is not given, first form on the page is submitted. See the `Locating elements` section for details about the locator syntax.

## Switch Browser

**Syntax**
```robot
Switch Browser
```

**Description**
Switches between active browsers using ``index_or_alias``. Indices are returned by the `Open Browser` keyword and aliases can be given to it explicitly. Indices start from 1. Example: | `Open Browser` | http://google.com | ff | | `Location Should Be` | http://google.com | | | `Open Browser` | http://yahoo.com | ie | alias=second | | `Location Should Be` |...

## Switch Window

**Syntax**
```robot
Switch Window
```

**Description**
Switches to browser window matching ``locator``. If the window is found, all subsequent commands use the selected window, until this keyword is used again. If the window is not found, this keyword fails. The previous windows handle is returned and can be used to switch back to it later. Notice that alerts should be handled with `Handle Alert` or other ale...

## Table Cell Should Contain

**Syntax**
```robot
Table Cell Should Contain
```

**Description**
Verifies table cell contains text ``expected``. See `Get Table Cell` that this keyword uses internally for an explanation about accepted arguments.

## Table Column Should Contain

**Syntax**
```robot
Table Column Should Contain
```

**Description**
Verifies table column contains text ``expected``. The table is located using the ``locator`` argument and its column found using ``column``. See the `Locating elements` section for details about the locator syntax. Column indexes start from 1. It is possible to refer to columns from the end by using negative indexes so that -1 is the last column, -2 is th...

## Table Footer Should Contain

**Syntax**
```robot
Table Footer Should Contain
```

**Description**
Verifies table footer contains text ``expected``. Any ``<td>`` element inside ``<tfoot>`` element is considered to be part of the footer. The table is located using the ``locator`` argument. See the `Locating elements` section for details about the locator syntax. See `Page Should Contain Element` for an explanation about the ``loglevel`` argument.

## Table Header Should Contain

**Syntax**
```robot
Table Header Should Contain
```

**Description**
Verifies table header contains text ``expected``. Any ``<th>`` element anywhere in the table is considered to be part of the header. The table is located using the ``locator`` argument. See the `Locating elements` section for details about the locator syntax. See `Page Should Contain Element` for an explanation about the ``loglevel`` argument.

## Table Row Should Contain

**Syntax**
```robot
Table Row Should Contain
```

**Description**
Verifies that table row contains text ``expected``. The table is located using the ``locator`` argument and its column found using ``column``. See the `Locating elements` section for details about the locator syntax. Row indexes start from 1. It is possible to refer to rows from the end by using negative indexes so that -1 is the last row, -2 is the secon...

## Table Should Contain

**Syntax**
```robot
Table Should Contain
```

**Description**
Verifies table contains text ``expected``. The table is located using the ``locator`` argument. See the `Locating elements` section for details about the locator syntax. See `Page Should Contain Element` for an explanation about the ``loglevel`` argument.

## Textarea Should Contain

**Syntax**
```robot
Textarea Should Contain
```

**Description**
Verifies text area ``locator`` contains text ``expected``. ``message`` can be used to override default error message. See the `Locating elements` section for details about the locator syntax.

## Textarea Value Should Be

**Syntax**
```robot
Textarea Value Should Be
```

**Description**
Verifies text area ``locator`` has exactly text ``expected``. ``message`` can be used to override default error message. See the `Locating elements` section for details about the locator syntax.

## Textfield Should Contain

**Syntax**
```robot
Textfield Should Contain
```

**Description**
Verifies text field ``locator`` contains text ``expected``. ``message`` can be used to override the default error message. See the `Locating elements` section for details about the locator syntax.

## Textfield Value Should Be

**Syntax**
```robot
Textfield Value Should Be
```

**Description**
Verifies text field ``locator`` has exactly text ``expected``. ``message`` can be used to override default error message. See the `Locating elements` section for details about the locator syntax.

## Title Should Be

**Syntax**
```robot
Title Should Be
```

**Description**
Verifies that the current page title equals ``title``. The ``message`` argument can be used to override the default error message. ``message`` argument is new in SeleniumLibrary 3.1.

## Unselect All From List

**Syntax**
```robot
Unselect All From List
```

**Description**
Unselects all options from multi-selection list ``locator``. See the `Locating elements` section for details about the locator syntax. New in SeleniumLibrary 3.0.

## Unselect Checkbox

**Syntax**
```robot
Unselect Checkbox
```

**Description**
Removes the selection of checkbox identified by ``locator``. Does nothing if the checkbox is not selected. See the `Locating elements` section for details about the locator syntax.

## Unselect Frame

**Syntax**
```robot
Unselect Frame
```

**Description**
Sets the main frame as the current frame. In practice cancels the previous `Select Frame` call.

## Unselect From List By Index

**Syntax**
```robot
Unselect From List By Index
```

**Description**
Unselects options from selection list ``locator`` by ``indexes``. Indexes of list options start from 0. This keyword works only with multi-selection lists. See the `Locating elements` section for details about the locator syntax.

## Unselect From List By Label

**Syntax**
```robot
Unselect From List By Label
```

**Description**
Unselects options from selection list ``locator`` by ``labels``. This keyword works only with multi-selection lists. See the `Locating elements` section for details about the locator syntax.

## Unselect From List By Value

**Syntax**
```robot
Unselect From List By Value
```

**Description**
Unselects options from selection list ``locator`` by ``values``. This keyword works only with multi-selection lists. See the `Locating elements` section for details about the locator syntax.

## Wait For Condition

**Syntax**
```robot
Wait For Condition
```

**Description**
Waits until ``condition`` is true or ``timeout`` expires. The condition can be arbitrary JavaScript expression but it must return a value to be evaluated. See `Execute JavaScript` for information about accessing content on pages. Fails if the timeout expires before the condition becomes true. See the `Timeouts` section for more information about using tim...

## Wait For Expected Condition

**Syntax**
```robot
Wait For Expected Condition
```

**Description**
Waits until ``condition`` is true or ``timeout`` expires. The condition must be one of selenium's expected condition which can be found within the selenium [https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html#module-selenium.webdriver.support.expected_conditions|Python API] documentation. The...

## Wait Until Element Contains

**Syntax**
```robot
Wait Until Element Contains
```

**Description**
Waits until the element ``locator`` contains ``text``. Fails if ``timeout`` expires before the text appears. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details about the locator syntax. ``error`` can be used to override the default error message.

## Wait Until Element Does Not Contain

**Syntax**
```robot
Wait Until Element Does Not Contain
```

**Description**
Waits until the element ``locator`` does not contain ``text``. Fails if ``timeout`` expires before the text disappears. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details about the locator syntax. ``error`` can be used to override the default error message.

## Wait Until Element Is Enabled

**Syntax**
```robot
Wait Until Element Is Enabled
```

**Description**
Waits until the element ``locator`` is enabled. Element is considered enabled if it is not disabled nor read-only. Fails if ``timeout`` expires before the element is enabled. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details about the locator syntax. ``error`` can b...

## Wait Until Element Is Not Visible

**Syntax**
```robot
Wait Until Element Is Not Visible
```

**Description**
Waits until the element ``locator`` is not visible. Fails if ``timeout`` expires before the element is not visible. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details about the locator syntax. ``error`` can be used to override the default error message.

## Wait Until Element Is Visible

**Syntax**
```robot
Wait Until Element Is Visible
```

**Description**
Waits until the element ``locator`` is visible. Fails if ``timeout`` expires before the element is visible. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details about the locator syntax. ``error`` can be used to override the default error message.

## Wait Until Location Contains

**Syntax**
```robot
Wait Until Location Contains
```

**Description**
Waits until the current URL contains ``expected``. The ``expected`` argument contains the expected value in url. Fails if ``timeout`` expires before the location contains. See the `Timeouts` section for more information about using timeouts and their default value. The ``message`` argument can be used to override the default error message. New in Selenium...

## Wait Until Location Does Not Contain

**Syntax**
```robot
Wait Until Location Does Not Contain
```

**Description**
Waits until the current URL does not contains ``location``. The ``location`` argument contains value not expected in url. Fails if ``timeout`` expires before the location not contains. See the `Timeouts` section for more information about using timeouts and their default value. The ``message`` argument can be used to override the default error message. Ne...

## Wait Until Location Is

**Syntax**
```robot
Wait Until Location Is
```

**Description**
Waits until the current URL is ``expected``. The ``expected`` argument is the expected value in url. Fails if ``timeout`` expires before the location is. See the `Timeouts` section for more information about using timeouts and their default value. The ``message`` argument can be used to override the default error message. New in SeleniumLibrary 4.0

## Wait Until Location Is Not

**Syntax**
```robot
Wait Until Location Is Not
```

**Description**
Waits until the current URL is not ``location``. The ``location`` argument is the unexpected value in url. Fails if ``timeout`` expires before the location is not. See the `Timeouts` section for more information about using timeouts and their default value. The ``message`` argument can be used to override the default error message. New in SeleniumLibrary 4.3

## Wait Until Page Contains

**Syntax**
```robot
Wait Until Page Contains
```

**Description**
Waits until ``text`` appears on the current page. Fails if ``timeout`` expires before the text appears. See the `Timeouts` section for more information about using timeouts and their default value. ``error`` can be used to override the default error message.

## Wait Until Page Contains Element

**Syntax**
```robot
Wait Until Page Contains Element
```

**Description**
Waits until the element ``locator`` appears on the current page. Fails if ``timeout`` expires before the element appears. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details about the locator syntax. ``error`` can be used to override the default error message. The ``l...

## Wait Until Page Does Not Contain

**Syntax**
```robot
Wait Until Page Does Not Contain
```

**Description**
Waits until ``text`` disappears from the current page. Fails if ``timeout`` expires before the text disappears. See the `Timeouts` section for more information about using timeouts and their default value. ``error`` can be used to override the default error message.

## Wait Until Page Does Not Contain Element

**Syntax**
```robot
Wait Until Page Does Not Contain Element
```

**Description**
Waits until the element ``locator`` disappears from the current page. Fails if ``timeout`` expires before the element disappears. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details about the locator syntax. ``error`` can be used to override the default error message....
