# Dialogs Keywords

## Execute Manual Step

**Syntax**
```robot
Execute Manual Step
```

**Description**
Pauses execution until user sets the keyword status. User can press either ``PASS`` or ``FAIL`` button. In the latter case execution fails and an additional dialog is opened for defining the error message. ``message`` is the instruction shown in the initial dialog and ``default_error`` is the default value shown in the possible error message dialog.

## Get Selection From User

**Syntax**
```robot
Get Selection From User
```

**Description**
Pauses execution and asks user to select a value. The selected value is returned. Pressing ``Cancel`` fails the keyword. ``message`` is the instruction shown in the dialog, ``values`` are the options given to the user and ``default`` is the optional default value. The default value can either be one of the specified values or the index of the value starti...

## Get Selections From User

**Syntax**
```robot
Get Selections From User
```

**Description**
Pauses execution and asks user to select multiple values. The selected values are returned as a list. Selecting no values is OK and in that case the returned list is empty. Pressing ``Cancel`` fails the keyword. ``message`` is the instruction shown in the dialog and ``values`` are the options given to the user. Example: | ${users} = | Get Selections From ...

## Get Value From User

**Syntax**
```robot
Get Value From User
```

**Description**
Pauses execution and asks user to input a value. Value typed by the user, or the possible default value, is returned. Returning an empty value is fine, but pressing ``Cancel`` fails the keyword. ``message`` is the instruction shown in the dialog and ``default_value`` is the possible default value shown in the input field. If ``hidden`` is given a true val...

## Pause Execution

**Syntax**
```robot
Pause Execution
```

**Description**
Pauses execution until user clicks ``Ok`` button. ``message`` is the message shown in the dialog.
