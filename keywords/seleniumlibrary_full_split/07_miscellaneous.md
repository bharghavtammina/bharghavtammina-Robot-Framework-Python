# SeleniumLibrary Keywords - Miscellaneous

## Assign Id To Element

**Syntax**
```robot
Assign Id To Element
```

**Description**
Assigns a temporary ``id`` to the element specified by ``locator``. This is mainly useful if the locator is complicated and/or slow XPath expression and it is needed multiple times. Identifier expires when the page is reloaded. See the `Locating elements` section for details about the locator syntax. Example: | `Ass...

## Choose File

**Syntax**
```robot
Choose File
```

**Description**
Inputs the ``file_path`` into the file input field ``locator``. This keyword is most often used to input files into upload forms. The keyword does not check ``file_path`` is the file or folder available on the machine where tests are executed. If the ``file_path`` points at a file and when using Selenium Grid, Selen...

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
Creates an instance of Selenium WebDriver. Like `Open Browser`, but allows passing arguments to the created WebDriver instance directly. This keyword should only be used if the functionality provided by `Open Browser` is not adequate. ``driver_name`` must be a WebDriver implementation name like Firefox, Chrome, Ie, ...

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

## Get CSS Property Value

**Syntax**
```robot
Get CSS Property Value
```

**Description**
Returns the computed value of ``css_property`` from the element ``locator``. See the `Locating elements` section for details about the locator syntax. The value returned is the browser-computed CSS value of the property. For example, colors are often returned in ``rgba(...)`` format and sizes are typically returned ...

## Get Dom Attribute

**Syntax**
```robot
Get Dom Attribute
```

**Description**
Returns the value of ``attribute`` from the element ``locator``. `Get DOM Attribute` keyword only returns attributes declared within the element's HTML markup. If the requested attribute is not there, the keyword returns ${None}. See the `Locating elements` section for details about the locator syntax. Example: | ${...

## Get Element Attribute

**Syntax**
```robot
Get Element Attribute
```

**Description**
Returns the value of ``attribute`` from the element ``locator``. See the `Locating elements` section for details about the locator syntax. Example: | ${id}= | `Get Element Attribute` | css:h1 | id | Passing attribute name as part of the ``locator`` was removed in SeleniumLibrary 3.2. The explicit ``attribute`` argum...

## Get Element Count

**Syntax**
```robot
Get Element Count
```

**Description**
Returns the number of elements matching ``locator``. If you wish to assert the number of matching elements, use `Page Should Contain Element` with ``limit`` argument. Keyword will always return an integer. Example: | ${count} = | `Get Element Count` | name:div_name | | `Should Be True` | ${count} > 2 | | New in Sele...

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
Returns all labels or values of selection list ``locator``. See the `Locating elements` section for details about the locator syntax. Returns visible labels by default, but values can be returned by setting the ``values`` argument to a true value (see `Boolean arguments`). Example: | ${labels} = | `Get List Items` |...

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
Returns contents of a table cell. The table is located using the ``locator`` argument and its cell found using ``row`` and ``column``. See the `Locating elements` section for details about the locator syntax. Both row and column indexes start from 1, and header and footer rows are included in the count. It is possib...

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

## Go Back

**Syntax**
```robot
Go Back
```

**Description**
Simulates the user clicking the back button on their browser.

## Log Source

**Syntax**
```robot
Log Source
```

**Description**
Logs and returns the HTML source of the current page or frame. The ``loglevel`` argument defines the used log level. Valid log levels are ``WARN``, ``INFO`` (default), ``DEBUG``, ``TRACE`` and ``NONE`` (no logging).

## Press Key

**Syntax**
```robot
Press Key
```

**Description**
Simulates user pressing key on element identified by ``locator``. See the `Locating elements` section for details about the locator syntax. ``key`` is either a single character, a string, or a numerical ASCII code of the key lead by '\'. Examples: | `Press Key` | text_field | q | | `Press Key` | text_field | abcde |...

## Print Page As Pdf

**Syntax**
```robot
Print Page As Pdf
```

**Description**
Print the current page as a PDF ``page_ranges`` defaults to `['-']` or "all" pages. ``page_ranges`` takes a list of strings indicating the ranges. The page size defaults to 21.59 for ``page_width`` and 27.94 for ``page_height``. This is the equivalent size of US-Letter. The assumed units on these parameters is centi...

## Register Keyword To Run On Failure

**Syntax**
```robot
Register Keyword To Run On Failure
```

**Description**
Sets the keyword to execute, when a SeleniumLibrary keyword fails. ``keyword`` is the name of a keyword that will be executed if a SeleniumLibrary keyword fails. It is possible to use any available keyword, including user keywords or keywords from other libraries, but the keyword must not take any arguments. The ini...

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

## Set Action Chain Delay

**Syntax**
```robot
Set Action Chain Delay
```

**Description**
Sets the duration of delay in ActionChains() used by SeleniumLibrary. The value can be given as a number that is considered to be seconds or as a human-readable string like ``1 second``. Value is always stored as milliseconds internally. The previous value is returned and can be used to restore the original value la...

## Set Focus To Element

**Syntax**
```robot
Set Focus To Element
```

**Description**
Sets the focus to the element identified by ``locator``. See the `Locating elements` section for details about the locator syntax. Prior to SeleniumLibrary 3.0 this keyword was named `Focus`.

## Simulate Event

**Syntax**
```robot
Simulate Event
```

**Description**
Simulates ``event`` on the element identified by ``locator``. This keyword is useful if element has ``OnEvent`` handler that needs to be explicitly invoked. See the `Locating elements` section for details about the locator syntax. Prior to SeleniumLibrary 3.0 this keyword was named `Simulate`.
