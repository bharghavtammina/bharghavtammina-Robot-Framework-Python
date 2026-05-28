# SeleniumLibrary Keywords - Waits And Assertions

## Alert Should Be Present

**Syntax**
```robot
Alert Should Be Present
```

**Description**
Verifies that an alert is present and by default, accepts it. Fails if no alert is present. If ``text`` is a non-empty string, then it is used to verify alert's message. The alert is accepted by default, but that behavior can be controlled by using the ``action`` argument same way as with `Handle Alert`. ``timeout``...

## Alert Should Not Be Present

**Syntax**
```robot
Alert Should Not Be Present
```

**Description**
Verifies that no alert is present. If the alert actually exists, the ``action`` argument determines how it should be handled. By default, the alert is accepted, but it can be also dismissed or left open the same way as with the `Handle Alert` keyword. ``timeout`` specifies how long to wait for the alert to appear. B...

## Clear Element Text

**Syntax**
```robot
Clear Element Text
```

**Description**
Clears the value of the text-input-element identified by ``locator``. See the `Locating elements` section for details about the locator syntax.

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
Verifies that the element identified by ``locator`` is visible. Herein, visible means that the element is logically visible, not optically visible in the current browser viewport. For example, an element that carries ``display:none`` is not logically visible, so using this keyword on that element would fail. See the...

## Element Should Contain

**Syntax**
```robot
Element Should Contain
```

**Description**
Verifies that element ``locator`` contains text ``expected``. See the `Locating elements` section for details about the locator syntax. The ``message`` argument can be used to override the default error message. The ``ignore_case`` argument can be set to True to compare case insensitive, default is False. New in Sel...

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
Verifies that element ``locator`` does not contain text ``expected``. See the `Locating elements` section for details about the locator syntax. The ``message`` argument can be used to override the default error message. The ``ignore_case`` argument can be set to True to compare case insensitive, default is False. ``...

## Element Text Should Be

**Syntax**
```robot
Element Text Should Be
```

**Description**
Verifies that element ``locator`` contains exact the text ``expected``. See the `Locating elements` section for details about the locator syntax. The ``message`` argument can be used to override the default error message. The ``ignore_case`` argument can be set to True to compare case insensitive, default is False. ...

## Element Text Should Not Be

**Syntax**
```robot
Element Text Should Not Be
```

**Description**
Verifies that element ``locator`` does not contain exact the text ``not_expected``. See the `Locating elements` section for details about the locator syntax. The ``message`` argument can be used to override the default error message. The ``ignore_case`` argument can be set to True to compare case insensitive, defaul...

## Frame Should Contain

**Syntax**
```robot
Frame Should Contain
```

**Description**
Verifies that frame identified by ``locator`` contains ``text``. See the `Locating elements` section for details about the locator syntax. See `Page Should Contain` for an explanation about the ``loglevel`` argument.

## Get Selenium Implicit Wait

**Syntax**
```robot
Get Selenium Implicit Wait
```

**Description**
Gets the implicit wait value used by Selenium. The value is returned as a human-readable string like ``1 second``. See the `Implicit wait` section above for more information.

## Get Text

**Syntax**
```robot
Get Text
```

**Description**
Returns the text value of the element identified by ``locator``. See the `Locating elements` section for details about the locator syntax.

## List Selection Should Be

**Syntax**
```robot
List Selection Should Be
```

**Description**
Verifies selection list ``locator`` has ``expected`` options selected. It is possible to give expected options both as visible labels and as values. Starting from SeleniumLibrary 3.0, mixing labels and values is not possible. Order of the selected options is not validated. If no expected options are given, validates...

## List Should Have No Selections

**Syntax**
```robot
List Should Have No Selections
```

**Description**
Verifies selection list ``locator`` has no options selected. See the `Locating elements` section for details about the locator syntax.

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
Verifies that current page contains ``text``. If this keyword fails, it automatically logs the page source using the log level specified with the optional ``loglevel`` argument. Valid log levels are ``TRACE`` (default), ``DEBUG``, ``INFO``, ``WARN``, and ``NONE``. If the log level is ``NONE`` or below the current ac...

## Page Should Contain Button

**Syntax**
```robot
Page Should Contain Button
```

**Description**
Verifies button ``locator`` is found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, buttons are searched using ``id``, ``name``, an...

## Page Should Contain Element

**Syntax**
```robot
Page Should Contain Element
```

**Description**
Verifies that element ``locator`` is found on the current page. See the `Locating elements` section for details about the locator syntax. The ``message`` argument can be used to override the default error message. The ``limit`` argument can used to define how many elements the page should contain. When ``limit`` is ...

## Page Should Contain Image

**Syntax**
```robot
Page Should Contain Image
```

**Description**
Verifies image identified by ``locator`` is found from current page. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, images are searched using ``id``, ``name``, ``src`` and ``alt``. See `Page Should Contain Element` for an explanation about ``message...

## Page Should Contain Link

**Syntax**
```robot
Page Should Contain Link
```

**Description**
Verifies link identified by ``locator`` is found from current page. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, links are searched using ``id``, ``name``, ``href`` and the link text. See `Page Should Contain Element` for an explanation about ``me...

## Page Should Contain List

**Syntax**
```robot
Page Should Contain List
```

**Description**
Verifies selection list ``locator`` is found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax.

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
Verifies button ``locator`` is not found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, buttons are searched using ``id``, ``name``...

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
Verifies image identified by ``locator`` is not found from current page. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, images are searched using ``id``, ``name``, ``src`` and ``alt``. See `Page Should Contain Element` for an explanation about ``mes...

## Page Should Not Contain Link

**Syntax**
```robot
Page Should Not Contain Link
```

**Description**
Verifies link identified by ``locator`` is not found from current page. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, links are searched using ``id``, ``name``, ``href`` and the link text. See `Page Should Contain Element` for an explanation about ...

## Page Should Not Contain List

**Syntax**
```robot
Page Should Not Contain List
```

**Description**
Verifies selection list ``locator`` is not found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax.

## Page Should Not Contain Textfield

**Syntax**
```robot
Page Should Not Contain Textfield
```

**Description**
Verifies text field ``locator`` is not found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax.

## Set Selenium Implicit Wait

**Syntax**
```robot
Set Selenium Implicit Wait
```

**Description**
Sets the implicit wait value used by Selenium. The value can be given as a number that is considered to be seconds or as a human-readable string like ``1 second``. The previous value is returned and can be used to restore the original value later if needed. This keyword sets the implicit wait for all opened browsers...

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
Verifies table column contains text ``expected``. The table is located using the ``locator`` argument and its column found using ``column``. See the `Locating elements` section for details about the locator syntax. Column indexes start from 1. It is possible to refer to columns from the end by using negative indexes...

## Table Footer Should Contain

**Syntax**
```robot
Table Footer Should Contain
```

**Description**
Verifies table footer contains text ``expected``. Any ``<td>`` element inside ``<tfoot>`` element is considered to be part of the footer. The table is located using the ``locator`` argument. See the `Locating elements` section for details about the locator syntax. See `Page Should Contain Element` for an explanation...

## Table Header Should Contain

**Syntax**
```robot
Table Header Should Contain
```

**Description**
Verifies table header contains text ``expected``. Any ``<th>`` element anywhere in the table is considered to be part of the header. The table is located using the ``locator`` argument. See the `Locating elements` section for details about the locator syntax. See `Page Should Contain Element` for an explanation abou...

## Table Row Should Contain

**Syntax**
```robot
Table Row Should Contain
```

**Description**
Verifies that table row contains text ``expected``. The table is located using the ``locator`` argument and its column found using ``column``. See the `Locating elements` section for details about the locator syntax. Row indexes start from 1. It is possible to refer to rows from the end by using negative indexes so ...

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

## Wait For Condition

**Syntax**
```robot
Wait For Condition
```

**Description**
Waits until ``condition`` is true or ``timeout`` expires. The condition can be arbitrary JavaScript expression but it must return a value to be evaluated. See `Execute JavaScript` for information about accessing content on pages. Fails if the timeout expires before the condition becomes true. See the `Timeouts` sect...

## Wait For Expected Condition

**Syntax**
```robot
Wait For Expected Condition
```

**Description**
Waits until ``condition`` is true or ``timeout`` expires. The condition must be one of selenium's expected condition which can be found within the selenium [https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html#module-selenium.webdriver.support.expected_c...

## Wait Until Element Contains

**Syntax**
```robot
Wait Until Element Contains
```

**Description**
Waits until the element ``locator`` contains ``text``. Fails if ``timeout`` expires before the text appears. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details about the locator syntax. ``error`` can be used to override the def...

## Wait Until Element Does Not Contain

**Syntax**
```robot
Wait Until Element Does Not Contain
```

**Description**
Waits until the element ``locator`` does not contain ``text``. Fails if ``timeout`` expires before the text disappears. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details about the locator syntax. ``error`` can be used to overr...

## Wait Until Element Is Enabled

**Syntax**
```robot
Wait Until Element Is Enabled
```

**Description**
Waits until the element ``locator`` is enabled. Element is considered enabled if it is not disabled nor read-only. Fails if ``timeout`` expires before the element is enabled. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details a...

## Wait Until Element Is Not Visible

**Syntax**
```robot
Wait Until Element Is Not Visible
```

**Description**
Waits until the element ``locator`` is not visible. Fails if ``timeout`` expires before the element is not visible. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details about the locator syntax. ``error`` can be used to override ...

## Wait Until Element Is Visible

**Syntax**
```robot
Wait Until Element Is Visible
```

**Description**
Waits until the element ``locator`` is visible. Fails if ``timeout`` expires before the element is visible. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details about the locator syntax. ``error`` can be used to override the defa...

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
Waits until the element ``locator`` appears on the current page. Fails if ``timeout`` expires before the element appears. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details about the locator syntax. ``error`` can be used to ove...

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
Waits until the element ``locator`` disappears from the current page. Fails if ``timeout`` expires before the element disappears. See the `Timeouts` section for more information about using timeouts and their default value and the `Locating elements` section for details about the locator syntax. ``error`` can be use...
