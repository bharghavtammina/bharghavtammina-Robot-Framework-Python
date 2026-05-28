# SeleniumLibrary Keywords - Frames Alerts And Windows

## Handle Alert

**Syntax**
```robot
Handle Alert
```

**Description**
Handles the current alert and returns its message. By default, the alert is accepted, but this can be controlled with the ``action`` argument that supports the following case-insensitive values: - ``ACCEPT``: Accept the alert i.e. press ``Ok``. Default. - ``DISMISS``: Dismiss the alert i.e. press ``Cancel``. - ``LEA...

## Select Frame

**Syntax**
```robot
Select Frame
```

**Description**
Sets frame identified by ``locator`` as the current frame. See the `Locating elements` section for details about the locator syntax. Works both with frames and iframes. Use `Unselect Frame` to cancel the frame selection and return to the main frame. Example: | `Select Frame` | top-frame | # Select frame with id or n...
