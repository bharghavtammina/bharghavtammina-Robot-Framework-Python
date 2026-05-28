# SeleniumLibrary Keywords - Element Actions And Forms

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

## Click Button

**Syntax**
```robot
Click Button
```

**Description**
Clicks the button identified by ``locator``. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, buttons are searched using ``id``, ``name``, and ``value``. See the `Click Element` keyword for details about the ``modifier`` argument. The ``modifier`` arg...

## Click Element

**Syntax**
```robot
Click Element
```

**Description**
Click the element identified by ``locator``. See the `Locating elements` section for details about the locator syntax. The ``modifier`` argument can be used to pass [https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_common/selenium.webdriver.common.keys.html#module-selenium.webdriver.common.keys|Selen...

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
Clicks an image identified by ``locator``. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, images are searched using ``id``, ``name``, ``src`` and ``alt``. See the `Click Element` keyword for details about the ``modifier`` argument. The ``modifier`` ...

## Click Link

**Syntax**
```robot
Click Link
```

**Description**
Clicks a link identified by ``locator``. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, links are searched using ``id``, ``name``, ``href`` and the link text. See the `Click Element` keyword for details about the ``modifier`` argument. The ``modifie...

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
Drags the element identified by ``locator`` into the ``target`` element. The ``locator`` argument is the locator of the dragged element and the ``target`` is the locator of the target. See the `Locating elements` section for details about the locator syntax. Example: | `Drag And Drop` | css:div#element | css:div.tar...

## Drag And Drop Across Frames

**Syntax**
```robot
Drag And Drop Across Frames
```

**Description**
Drags an element and drops it onto a target element across frame boundaries. The ``locator`` argument is the locator of the element to drag. The ``target`` argument is the locator of the drop target. The ``target_frame`` argument is the locator of the iframe containing the target. The optional ``source_frame`` argum...

## Drag And Drop By Offset

**Syntax**
```robot
Drag And Drop By Offset
```

**Description**
Drags the element identified with ``locator`` by ``xoffset/yoffset``. See the `Locating elements` section for details about the locator syntax. The element will be moved by ``xoffset`` and ``yoffset``, each of which is a negative or positive number specifying the offset. Example: | `Drag And Drop By Offset` | myElem...

## Input Password

**Syntax**
```robot
Input Password
```

**Description**
Types the given password into the text field identified by ``locator``. See the `Locating elements` section for details about the locator syntax. See `Input Text` for ``clear`` argument details. Difference compared to `Input Text` is that this keyword does not log the given password on the INFO level. Notice that if...

## Input Text

**Syntax**
```robot
Input Text
```

**Description**
Types the given ``text`` into the text field identified by ``locator``. When ``clear`` is true, the input element is cleared before the text is typed into the element. When false, the previous text is not cleared from the element. Use `Input Password` if you do not want the given ``text`` to be logged. This keyword ...

## Input Text Into Alert

**Syntax**
```robot
Input Text Into Alert
```

**Description**
Types the given ``text`` into an input field in an alert. The alert is accepted by default, but that behavior can be controlled by using the ``action`` argument same way as with `Handle Alert`. ``timeout`` specifies how long to wait for the alert to appear. If it is not given, the global default `timeout` is used in...

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

## Page Should Contain Checkbox

**Syntax**
```robot
Page Should Contain Checkbox
```

**Description**
Verifies checkbox ``locator`` is found from the current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax.

## Page Should Contain Radio Button

**Syntax**
```robot
Page Should Contain Radio Button
```

**Description**
Verifies radio button ``locator`` is found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, radio buttons are searched using ``id``, ...

## Page Should Not Contain Checkbox

**Syntax**
```robot
Page Should Not Contain Checkbox
```

**Description**
Verifies checkbox ``locator`` is not found from the current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax.

## Page Should Not Contain Radio Button

**Syntax**
```robot
Page Should Not Contain Radio Button
```

**Description**
Verifies radio button ``locator`` is not found from current page. See `Page Should Contain Element` for an explanation about ``message`` and ``loglevel`` arguments. See the `Locating elements` section for details about the locator syntax. When using the default locator strategy, radio buttons are searched using ``id...

## Press Keys

**Syntax**
```robot
Press Keys
```

**Description**
Simulates the user pressing key(s) to an element or on the active browser. If ``locator`` evaluates as false, see `Boolean arguments` for more details, then the ``keys`` are sent to the currently active browser. Otherwise element is searched and ``keys`` are send to the element identified by the ``locator``. In late...

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

## Select Checkbox

**Syntax**
```robot
Select Checkbox
```

**Description**
Selects the checkbox identified by ``locator``. Does nothing if checkbox is already selected. See the `Locating elements` section for details about the locator syntax.

## Select From List By Index

**Syntax**
```robot
Select From List By Index
```

**Description**
Selects options from selection list ``locator`` by ``indexes``. Indexes of list options start from 0. If more than one option is given for a single-selection list, the last value will be selected. With multi-selection lists all specified options are selected, but possible old selections are not cleared. See the `Loc...

## Select From List By Label

**Syntax**
```robot
Select From List By Label
```

**Description**
Selects options from selection list ``locator`` by ``labels``. If more than one option is given for a single-selection list, the last value will be selected. With multi-selection lists all specified options are selected, but possible old selections are not cleared. See the `Locating elements` section for details abo...

## Select From List By Value

**Syntax**
```robot
Select From List By Value
```

**Description**
Selects options from selection list ``locator`` by ``values``. If more than one option is given for a single-selection list, the last value will be selected. With multi-selection lists all specified options are selected, but possible old selections are not cleared. See the `Locating elements` section for details abo...

## Select Radio Button

**Syntax**
```robot
Select Radio Button
```

**Description**
Sets the radio button group ``group_name`` to ``value``. The radio button to be selected is located by two arguments: - ``group_name`` is the name of the radio button group. - ``value`` is the ``id`` or ``value`` attribute of the actual radio button. Examples: | `Select Radio Button` | size | XL | | `Select Radio Bu...

## Submit Form

**Syntax**
```robot
Submit Form
```

**Description**
Submits a form identified by ``locator``. If ``locator`` is not given, first form on the page is submitted. See the `Locating elements` section for details about the locator syntax.

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
