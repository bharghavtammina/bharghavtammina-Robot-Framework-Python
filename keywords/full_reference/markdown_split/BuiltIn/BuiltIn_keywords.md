# BuiltIn Keywords

## Call Method

**Syntax**
```robot
Call Method
```

**Description**
Calls the named method of the given object with the provided arguments. The possible return value from the method is returned and can be assigned to a variable. Keyword fails both if the object does not have a method with the given name or if executing the method raises an exception. Possible equal signs in arguments must be escaped with a backslash like ...

## Catenate

**Syntax**
```robot
Catenate
```

**Description**
Catenates the given items together and returns the resulted string. By default, items are catenated with spaces, but if the first item contains the string ``SEPARATOR=<sep>``, the separator ``<sep>`` is used instead. Items are converted into strings when necessary. Examples: | ${str1} = | Catenate | Hello | world | | | ${str2} = | Catenate | SEPARATOR=---...

## Comment

**Syntax**
```robot
Comment
```

**Description**
Displays the given messages in the log file as keyword arguments. This keyword does nothing with the arguments it receives, but as they are visible in the log, this keyword can be used to display simple messages. Given arguments are ignored so thoroughly that they can even contain non-existing variables. If you are interested about variable values, you ca...

## Continue For Loop

**Syntax**
```robot
Continue For Loop
```

**Description**
Skips the current FOR loop iteration and continues from the next. --- *NOTE:* Robot Framework 5.0 added support for native ``CONTINUE`` statement that is recommended over this keyword. In the examples below, ``Continue For Loop`` can simply be replaced with ``CONTINUE``. In addition to that, the ``IF`` syntax can be used instead of ``Run Keyword If``. For...

## Continue For Loop If

**Syntax**
```robot
Continue For Loop If
```

**Description**
Skips the current FOR loop iteration if the ``condition`` is true. --- *NOTE:* Robot Framework 5.0 added support for native ``CONTINUE`` statement and for inline ``IF``, and that combination should be used instead of this keyword. For example, ``Continue For Loop If`` usage in the example below could be replaced with | IF '${var}' == 'CONTINUE' CONTINUE T...

## Convert To Binary

**Syntax**
```robot
Convert To Binary
```

**Description**
Converts the given item to a binary string. The ``item``, with an optional ``base``, is first converted to an integer using `Convert To Integer` internally. After that it is converted to a binary number (base 2) represented as a string such as ``1011``. The returned value can contain an optional ``prefix`` and can be required to be of minimum ``length`` (...

## Convert To Boolean

**Syntax**
```robot
Convert To Boolean
```

**Description**
Converts the given item to Boolean ``True`` or ``False``. Returns item's [http://docs.python.org/library/stdtypes.html#truth|truth value]. Uses Python's ``bool()`` function in other cases, but the string ``FALSE``, case-insensitively, is considered ``False``. Notice that this keyword handles strings differently than argument and variable conversion where ...

## Convert To Bytes

**Syntax**
```robot
Convert To Bytes
```

**Description**
Converts the given ``input`` to bytes according to the ``input_type``. Valid input types are listed below: - ``text:`` Converts text to bytes character by character. All characters with ordinal below 256 can be used and are converted to bytes with same values. Many characters are easiest to represent using escapes like ``\x00`` or ``\xff``. In practice th...

## Convert To Hex

**Syntax**
```robot
Convert To Hex
```

**Description**
Converts the given item to a hexadecimal string. The ``item``, with an optional ``base``, is first converted to an integer using `Convert To Integer` internally. After that it is converted to a hexadecimal number (base 16) represented as a string such as ``FF0A``. The returned value can contain an optional ``prefix`` and can be required to be of minimum `...

## Convert To Integer

**Syntax**
```robot
Convert To Integer
```

**Description**
Converts the given item to an integer number. If the given item is a string, it is by default expected to be an integer in base 10. There are two ways to convert from other bases: - Give base explicitly to the keyword as ``base`` argument. - Prefix the given string with the base so that ``0b`` means binary (base 2), ``0o`` means octal (base 8), and ``0x``...

## Convert To Number

**Syntax**
```robot
Convert To Number
```

**Description**
Converts the given item to a floating point number. If the optional ``precision`` is positive or zero, the returned number is rounded to that number of decimal digits. Negative precision means that the number is rounded to the closest multiple of 10 to the power of the absolute precision. If a number is equally close to a certain precision, it is rounded ...

## Convert To Octal

**Syntax**
```robot
Convert To Octal
```

**Description**
Converts the given item to an octal string. The ``item``, with an optional ``base``, is first converted to an integer using `Convert To Integer` internally. After that it is converted to an octal number (base 8) represented as a string such as ``775``. The returned value can contain an optional ``prefix`` and can be required to be of minimum ``length`` (e...

## Convert To String

**Syntax**
```robot
Convert To String
```

**Description**
Converts the given item to a Unicode string. Strings are also [https://en.wikipedia.org/wiki/Unicode_equivalence| NFC normalized]. Use `Encode String To Bytes` and `Decode Bytes To String` keywords in ``String`` library if you need to convert between Unicode and byte strings using different encodings. Use `Convert To Bytes` if you just want to create byte...

## Create Dictionary

**Syntax**
```robot
Create Dictionary
```

**Description**
Creates and returns a dictionary based on the given ``items``. Items are typically given using the ``key=value`` syntax same way as ``&{dictionary}`` variables are created in the Variable table. Both keys and values can contain variables, and possible equal sign in key can be escaped with a backslash like ``escaped\=key=value``. It is also possible to get...

## Create List

**Syntax**
```robot
Create List
```

**Description**
Returns a list containing given items. The returned list can be assigned both to ``${scalar}`` and ``@{list}`` variables. Examples: | @{list} = | Create List | a | b | c | | ${scalar} = | Create List | a | b | c | | ${ints} = | Create List | ${1} | ${2} | ${3} |

## Evaluate

**Syntax**
```robot
Evaluate
```

**Description**
Evaluates the given expression in Python and returns the result. ``expression`` is evaluated in Python as explained in the `Evaluating expressions` section. ``modules`` argument can be used to specify a comma separated list of Python modules to be imported and added to the evaluation namespace. ``namespace`` argument can be used to pass a custom evaluatio...

## Exit For Loop

**Syntax**
```robot
Exit For Loop
```

**Description**
Stops executing the enclosing FOR loop. --- *NOTE:* Robot Framework 5.0 added support for native ``BREAK`` statement that is recommended over this keyword. In the examples below, ``Exit For Loop`` can simply be replaced with ``BREAK``. In addition to that, the ``IF`` syntax can be used instead of ``Run Keyword If``. For example, the first example below co...

## Exit For Loop If

**Syntax**
```robot
Exit For Loop If
```

**Description**
Stops executing the enclosing FOR loop if the ``condition`` is true. --- *NOTE:* Robot Framework 5.0 added support for native ``BREAK`` statement and for inline ``IF``, and that combination should be used instead of this keyword. For example, ``Exit For Loop If`` usage in the example below could be replaced with | IF '${var}' == 'EXIT' BREAK This keyword ...

## Fail

**Syntax**
```robot
Fail
```

**Description**
Fails the test with the given message and optionally alters its tags. The error message is specified using the ``msg`` argument. It is possible to use HTML in the given error message, similarly as with any other keyword accepting an error message, by prefixing the error with ``*HTML*``. It is possible to modify tags of the current test case by passing tag...

## Fatal Error

**Syntax**
```robot
Fatal Error
```

**Description**
Stops the whole test execution. The test or suite where this keyword is used fails with the provided message, and subsequent tests fail with a canned message. Possible teardowns will nevertheless be executed. See `Fail` if you only want to stop one test case unconditionally.

## Get Count

**Syntax**
```robot
Get Count
```

**Description**
Returns and logs how many times ``item`` is found from ``container``. This keyword works with Python strings and lists and all objects that either have ``count`` method or can be converted to Python lists. Example: | ${count} = | Get Count | ${some item} | interesting value | | Should Be True | 5 < ${count} < 10 |

## Get Length

**Syntax**
```robot
Get Length
```

**Description**
Returns and logs the length of the given item as an integer. The item can be anything that has length or size, for example, a string, a list, or a dictionary. For legacy reasons, this keyword supports also other ways to get item length than the standard ``len(item)``. These other approaches are deprecated, though, and they will be removed in the future. E...

## Get Library Instance

**Syntax**
```robot
Get Library Instance
```

**Description**
Returns the currently active instance of the specified library. This keyword makes it easy for libraries to interact with other libraries that have state. This is illustrated by the Python example below: | from robot.libraries.BuiltIn import BuiltIn | | def title_should_start_with(expected): | lib = BuiltIn().get_library_instance('SeleniumLibrary') | titl...

## Get Time

**Syntax**
```robot
Get Time
```

**Description**
Returns the given time in the requested format. *NOTE:* DateTime library contains much more flexible keywords for getting the current date and time and for date and time handling in general. How time is returned is determined based on the given ``format`` string as follows. Note that all checks are case-insensitive. 1) If ``format`` contains the word ``ep...

## Get Variable Value

**Syntax**
```robot
Get Variable Value
```

**Description**
Returns variable value or ``default`` if the variable does not exist. The name of the variable can be given either as a normal variable name like ``${name}`` or in escaped format like ``$name`` or ``\${name}``. For the reasons explained in the `Using variables with keywords creating or accessing variables` section, using the escaped format is recommended....

## Get Variables

**Syntax**
```robot
Get Variables
```

**Description**
Returns a dictionary containing all variables in the current scope. Variables are returned as a special dictionary that allows accessing variables in space, case, and underscore insensitive manner similarly as accessing variables in the test data. This dictionary supports all same operations as normal Python dictionaries and, for example, Collections libr...

## Import Library

**Syntax**
```robot
Import Library
```

**Description**
Imports a library with the given name and optional arguments. This functionality allows dynamic importing of libraries while tests are running. That may be necessary, if the library itself is dynamic and not yet available when test data is processed. In a normal case, libraries should be imported using the Library setting in the Setting section. This keyw...

## Import Resource

**Syntax**
```robot
Import Resource
```

**Description**
Imports a resource file with the given path. Resources imported with this keyword are set into the test suite scope similarly when importing them in the Setting table using the Resource setting. The given path must be absolute or found from [http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#module-search-path|search path]. Forwa...

## Import Variables

**Syntax**
```robot
Import Variables
```

**Description**
Imports a variable file with the given path and optional arguments. Variables imported with this keyword are set into the test suite scope similarly when importing them in the Setting table using the Variables setting. These variables override possible existing variables with the same names. This functionality can thus be used to import new variables, for...

## Keyword Should Exist

**Syntax**
```robot
Keyword Should Exist
```

**Description**
Fails unless the given keyword exists in the current scope. Fails also if there is more than one keyword with the same name. Works both with the short name (e.g. ``Log``) and the full name (e.g. ``BuiltIn.Log``). The default error message can be overridden with the ``msg`` argument. See also `Variable Should Exist`.

## Length Should Be

**Syntax**
```robot
Length Should Be
```

**Description**
Verifies that the length of the given item is correct. The length of the item is got using the `Get Length` keyword. The default error message can be overridden with the ``msg`` argument.

## Log

**Syntax**
```robot
Log
```

**Description**
Logs the given message with the given level. Valid levels are TRACE, DEBUG, INFO (default), WARN and ERROR. In addition to that, there are pseudo log levels HTML and CONSOLE that both log messages using INFO. Non-string messages are converted to strings automatically. Messages below the current active log level are ignored. See `Set Log Level` keyword and...

## Log Many

**Syntax**
```robot
Log Many
```

**Description**
Logs the given messages as separate entries using the INFO level. Supports also logging list and dictionary variable items individually. Non-string items are converted to strings automatically. Examples: | Log Many | Hello | ${var} | | Log Many | @{list} | &{dict} | See `Log` and `Log To Console` keywords if you want to use alternative log levels, use HTM...

## Log To Console

**Syntax**
```robot
Log To Console
```

**Description**
Logs the given message to the console. Uses the standard output stream by default. Using the standard error stream is possible by giving the ``stream`` argument value ``stderr`` (case-insensitive). Converts non-string messages to strings automatically. Appends a newline to the logged message by default. This can be disabled by giving the ``no_newline`` ar...

## Log Variables

**Syntax**
```robot
Log Variables
```

**Description**
Logs all variables in the current scope with given log level.

## No Operation

**Syntax**
```robot
No Operation
```

**Description**
Does absolutely nothing.

## Pass Execution

**Syntax**
```robot
Pass Execution
```

**Description**
Skips rest of the current test, setup, or teardown with PASS status. This keyword can be used anywhere in the test data, but the place where used affects the behavior: - When used in any setup or teardown (suite, test or keyword), passes that setup or teardown. Possible keyword teardowns of the started keywords are executed. Does not affect execution or s...

## Pass Execution If

**Syntax**
```robot
Pass Execution If
```

**Description**
Conditionally skips rest of the current test, setup, or teardown with PASS status. A wrapper for `Pass Execution` to skip rest of the current test, setup or teardown based the given ``condition``. The condition is evaluated similarly as with `Should Be True` keyword, and ``message`` and ``*tags`` have same semantics as with `Pass Execution`. Example: | FO...

## Regexp Escape

**Syntax**
```robot
Regexp Escape
```

**Description**
Returns each argument escaped for use as a regular expression. This keyword can be used to escape strings to be used with `Should Match Regexp` and `Should Not Match Regexp` keywords. Escaping is done with Python's [https://docs.python.org/3/library/re.html#re.escape|re.escape()] function. Examples: | ${escaped} = | Regexp Escape | ${original} | | @{strin...

## Reload Library

**Syntax**
```robot
Reload Library
```

**Description**
Rechecks what keywords the specified library provides. Can be called explicitly in the test data or by a library itself when keywords it provides have changed. The library can be specified by its name or as the active instance of the library. The latter is especially useful if the library itself calls this keyword as a method.

## Remove Tags

**Syntax**
```robot
Remove Tags
```

**Description**
Removes given ``tags`` from the current test or all tests in a suite. Tags can be given exactly or using a pattern with ``*``, ``?`` and ``[chars]`` acting as wildcards. See the `Glob patterns` section for more information. This keyword can affect either one test case or all test cases in a test suite similarly as `Set Tags` keyword. The current tags are ...

## Repeat Keyword

**Syntax**
```robot
Repeat Keyword
```

**Description**
Executes the specified keyword multiple times. ``name`` and ``args`` define the keyword that is executed similarly as with `Run Keyword`. ``repeat`` specifies how many times (as a count) or how long time (as a timeout) the keyword should be executed. If ``repeat`` is given as count, it specifies how many times the keyword should be executed. ``repeat`` ca...

## Replace Variables

**Syntax**
```robot
Replace Variables
```

**Description**
Replaces variables in the given text with their current values. If the text contains undefined variables, this keyword fails. If the given ``text`` contains only a single variable, its value is returned as-is, and it can be any object. Otherwise, this keyword always returns a string. Example: The file ``template.txt`` contains ``Hello ${NAME}!`` and varia...

## Reset Log Level

**Syntax**
```robot
Reset Log Level
```

**Description**
Resets the log level to the original value. The original log level is set from the command line with the ``--loglevel`` option and is INFO by default. The active log level can be changed using the `Set Log Level` keyword. The previous log level is returned. New in Robot Framework 7.0.

## Return From Keyword

**Syntax**
```robot
Return From Keyword
```

**Description**
Returns from the enclosing user keyword. --- *NOTE:* Robot Framework 5.0 added support for native ``RETURN`` statement that is recommended over this keyword. In the examples below, ``Return From Keyword`` can simply be replaced with ``RETURN``. In addition to that, the ``IF`` syntax can be used instead of ``Run Keyword If``. For example, the first example...

## Return From Keyword If

**Syntax**
```robot
Return From Keyword If
```

**Description**
Returns from the enclosing user keyword if ``condition`` is true. --- *NOTE:* Robot Framework 5.0 added support for native ``RETURN`` statement and for inline ``IF``, and that combination should be used instead of this keyword. For example, `Return From Keyword If` usage in the `Find Index` example below could be replaced with this: | IF '${item}' == '${e...

## Run Keyword

**Syntax**
```robot
Run Keyword
```

**Description**
Executes the given keyword with the given arguments. Because the name of the keyword to execute is given as an argument, it can be a variable and thus set dynamically, e.g. from a return value of another keyword or from the command line.

## Run Keyword And Continue On Failure

**Syntax**
```robot
Run Keyword And Continue On Failure
```

**Description**
Runs the keyword and continues execution even if a failure occurs. The keyword name and arguments work as with `Run Keyword`. Example: | Run Keyword And Continue On Failure | Fail | This is a stupid example | | Log | This keyword is executed | The execution is not continued if the failure is caused by invalid syntax, timeout, or fatal exception.

## Run Keyword And Expect Error

**Syntax**
```robot
Run Keyword And Expect Error
```

**Description**
Runs the keyword and checks that the expected error occurred. The keyword to execute and its arguments are specified using ``name`` and ``*args`` exactly like with `Run Keyword`. The expected error must be given in the same format as in Robot Framework reports. It is interpreted as a glob pattern with ``*``, ``?`` and ``[chars]`` as wildcards by default, ...

## Run Keyword And Ignore Error

**Syntax**
```robot
Run Keyword And Ignore Error
```

**Description**
Runs the given keyword with the given arguments and ignores possible error. This keyword returns two values, so that the first is either string ``PASS`` or ``FAIL``, depending on the status of the executed keyword. The second value is either the return value of the keyword or the received error message. See `Run Keyword And Return Status` If you are only ...

## Run Keyword And Return

**Syntax**
```robot
Run Keyword And Return
```

**Description**
Runs the specified keyword and returns from the enclosing user keyword. The keyword to execute is defined with ``name`` and ``*args`` exactly like with `Run Keyword`. After running the keyword, returns from the enclosing user keyword and passes possible return value from the executed keyword further. Returning from a keyword has exactly same semantics as ...

## Run Keyword And Return If

**Syntax**
```robot
Run Keyword And Return If
```

**Description**
Runs the specified keyword and returns from the enclosing user keyword. A wrapper for `Run Keyword And Return` to run and return based on the given ``condition``. The condition is evaluated using the same semantics as with `Should Be True` keyword. Example: | `Run Keyword And Return If` | ${rc} > 0 | `My Keyword` | arg1 | arg2 | | # Above is equivalent to...

## Run Keyword And Return Status

**Syntax**
```robot
Run Keyword And Return Status
```

**Description**
Runs the specified keyword and returns the status as a Boolean value. This keyword returns Boolean ``True`` if the keyword that is executed succeeds and ``False`` if it fails. This is useful, for example, in combination with `Run Keyword If`. If you are interested in the error message or return value, use `Run Keyword And Ignore Error` instead. The keywor...

## Run Keyword And Warn On Failure

**Syntax**
```robot
Run Keyword And Warn On Failure
```

**Description**
Runs the specified keyword logs a warning if the keyword fails. This keyword is similar to `Run Keyword And Ignore Error` but if the executed keyword fails, the error message is logged as a warning to make it more visible. Returns status and possible return value or error message exactly like `Run Keyword And Ignore Error` does. Errors caused by invalid s...

## Run Keyword If

**Syntax**
```robot
Run Keyword If
```

**Description**
Runs the given keyword with the given arguments, if ``condition`` is true. --- *NOTE:* Native IF/ELSE syntax introduced in Robot Framework 4.0 is generally recommended over using this keyword. --- The given ``condition`` is evaluated in Python as explained in the `Evaluating expressions` section, and ``name`` and ``*args`` have same semantics as with `Run...

## Run Keyword If All Tests Passed

**Syntax**
```robot
Run Keyword If All Tests Passed
```

**Description**
Runs the given keyword with the given arguments, if all tests passed. This keyword can only be used in a suite teardown. Trying to use it anywhere else results in an error. Otherwise, this keyword works exactly like `Run Keyword`, see its documentation for more details.

## Run Keyword If Any Tests Failed

**Syntax**
```robot
Run Keyword If Any Tests Failed
```

**Description**
Runs the given keyword with the given arguments, if one or more tests failed. This keyword can only be used in a suite teardown. Trying to use it anywhere else results in an error. Otherwise, this keyword works exactly like `Run Keyword`, see its documentation for more details.

## Run Keyword If Test Failed

**Syntax**
```robot
Run Keyword If Test Failed
```

**Description**
Runs the given keyword with the given arguments, if the test failed. This keyword can only be used in a test teardown. Trying to use it anywhere else results in an error. Otherwise, this keyword works exactly like `Run Keyword`, see its documentation for more details.

## Run Keyword If Test Passed

**Syntax**
```robot
Run Keyword If Test Passed
```

**Description**
Runs the given keyword with the given arguments, if the test passed. This keyword can only be used in a test teardown. Trying to use it anywhere else results in an error. Otherwise, this keyword works exactly like `Run Keyword`, see its documentation for more details.

## Run Keyword If Timeout Occurred

**Syntax**
```robot
Run Keyword If Timeout Occurred
```

**Description**
Runs the given keyword if either a test or a keyword timeout has occurred. This keyword can only be used in a test teardown. Trying to use it anywhere else results in an error. Otherwise, this keyword works exactly like `Run Keyword`, see its documentation for more details.

## Run Keyword Unless

**Syntax**
```robot
Run Keyword Unless
```

**Description**
*DEPRECATED since RF 5.0. Use native IF/ELSE or `Run Keyword If` instead.* Runs the given keyword with the given arguments if ``condition`` is false. See `Run Keyword If` for more information and an example. Notice that this keyword does not support ELSE or ELSE IF branches like `Run Keyword If` does.

## Run Keywords

**Syntax**
```robot
Run Keywords
```

**Description**
Executes all the given keywords in a sequence. This keyword is mainly useful in setups and teardowns when they need to take care of multiple actions and creating a new higher level user keyword would be an overkill. By default, all arguments are expected to be keywords to be executed. Examples: | `Run Keywords` | `Initialize database` | `Start servers` | ...

## Set Global Variable

**Syntax**
```robot
Set Global Variable
```

**Description**
Makes a variable available globally in all tests and suites. Variables set with this keyword are globally available in all subsequent test suites, test cases and user keywords. Also variables created in the Variables sections are overridden. Variables assigned locally based on keyword return values or by using `Set Suite Variable`, `Set Test Variable` or ...

## Set Library Search Order

**Syntax**
```robot
Set Library Search Order
```

**Description**
Sets the resolution order to use when a name matches multiple keywords. The library search order is used to resolve conflicts when a keyword name that is used matches multiple keyword implementations. The first library (or resource, see below) containing the keyword is selected and that keyword implementation used. If the keyword is not found from any lib...

## Set Local Variable

**Syntax**
```robot
Set Local Variable
```

**Description**
Makes a variable available everywhere within the local scope. Variables set with this keyword are available within the local scope of the currently executed test case or in the local scope of the keyword in which they are defined. For example, if you set a variable in a user keyword, it is available only in that keyword. Other test cases or keywords will ...

## Set Log Level

**Syntax**
```robot
Set Log Level
```

**Description**
Sets the log threshold to the specified level. Messages below the level will not logged. The default logging level is INFO, but it can be overridden with the ``--loglevel`` command line option. The available levels are TRACE, DEBUG, INFO (default), WARN, ERROR and NONE (no logging). The old level is returned and can be used for setting the level back late...

## Set Suite Documentation

**Syntax**
```robot
Set Suite Documentation
```

**Description**
Sets documentation for the current test suite. By default, the possible existing documentation is overwritten, but this can be changed using the optional ``append`` argument similarly as with `Set Test Message` keyword. This keyword sets the documentation of the current suite by default. If the optional ``top`` argument is given a true value, the document...

## Set Suite Metadata

**Syntax**
```robot
Set Suite Metadata
```

**Description**
Sets metadata for the current test suite. By default, possible existing metadata values are overwritten, but this can be changed using the optional ``append`` argument similarly as with `Set Test Message` keyword. This keyword sets the metadata of the current suite by default. If the optional ``top`` argument is given a true value, the metadata of the top...

## Set Suite Variable

**Syntax**
```robot
Set Suite Variable
```

**Description**
Makes a variable available everywhere within the scope of the current suite. Variables set with this keyword are available everywhere within the scope of the currently executed test suite. Setting variables with this keyword thus has the same effect as creating them using the Variables section in the data file or importing them from variable files. Possib...

## Set Tags

**Syntax**
```robot
Set Tags
```

**Description**
Adds given ``tags`` for the current test or all tests in a suite. When this keyword is used inside a test case, that test gets the specified tags and other tests are not affected. If this keyword is used in a suite setup, all test cases in that suite, recursively, gets the given tags. It is a failure to use this keyword in a suite teardown. The current ta...

## Set Task Variable

**Syntax**
```robot
Set Task Variable
```

**Description**
Makes a variable available everywhere within the scope of the current task. This is an alias for `Set Test Variable` that is more applicable when creating tasks, not tests. *NOTE:* The ``VAR`` syntax introduced in Robot Framework 7.0 is recommended over this keyword.

## Set Test Documentation

**Syntax**
```robot
Set Test Documentation
```

**Description**
Sets documentation for the current test case. The possible existing documentation is overwritten by default, but this can be changed using the optional ``append`` argument similarly as with `Set Test Message` keyword. An optional ``separator`` argument can be used to provide custom separator string when appending to the old text. A single space is used as...

## Set Test Message

**Syntax**
```robot
Set Test Message
```

**Description**
Sets message for the current test case. If the optional ``append`` argument is given a true value, the given ``message`` is added after the possible earlier message. An optional ``separator`` argument can be used to provide custom separator string when appending to the old text. A single space is used as separator by default. In test teardown this keyword...

## Set Test Variable

**Syntax**
```robot
Set Test Variable
```

**Description**
Makes a variable available everywhere within the scope of the current test. Variables set with this keyword are available everywhere within the scope of the currently executed test case. For example, if you set a variable in a user keyword, it is available both in the test case level and also in all other user keywords used in the current test. Other test...

## Set Variable

**Syntax**
```robot
Set Variable
```

**Description**
Returns the given values which can then be assigned to a variables. --- *NOTE:* This keyword is considered deprecated and the ``VAR`` syntax introduced in Robot Framework 7.0 should be used instead. The basic ``VAR`` syntax is shown below and the Robot Framework User Guide explains the syntax in detail. | VAR ${hi} Hello, world! | VAR ${hi2} I said: ${hi}...

## Set Variable If

**Syntax**
```robot
Set Variable If
```

**Description**
Sets variable based on the given condition. The basic usage is giving a condition and two values. The given condition is first evaluated the same way as with the `Should Be True` keyword. If the condition is true, then the first value is returned, and otherwise the second value is returned. The second value can also be omitted, in which case it has a defa...

## Should Be Empty

**Syntax**
```robot
Should Be Empty
```

**Description**
Verifies that the given item is empty. The length of the item is got using the `Get Length` keyword. The default error message can be overridden with the ``msg`` argument.

## Should Be Equal

**Syntax**
```robot
Should Be Equal
```

**Description**
Fails if the given objects are unequal. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. The `String representations` section explains how ``formatter`` can be used for formatting values shown in failure messages. The `String and bytes normalization` section ...

## Should Be Equal As Integers

**Syntax**
```robot
Should Be Equal As Integers
```

**Description**
Fails if objects are unequal after converting them to integers. See `Convert To Integer` for information how to convert integers from other bases than 10 using ``base`` argument or ``0b/0o/0x`` prefixes. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. Exampl...

## Should Be Equal As Numbers

**Syntax**
```robot
Should Be Equal As Numbers
```

**Description**
Fails if objects are unequal after converting them to real numbers. The conversion is done with `Convert To Number` keyword using the given ``precision``. Examples: | Should Be Equal As Numbers | ${x} | 1.1 | | # Passes if ${x} is 1.1 | | Should Be Equal As Numbers | 1.123 | 1.1 | precision=1 | # Passes | | Should Be Equal As Numbers | 1.123 | 1.4 | preci...

## Should Be Equal As Strings

**Syntax**
```robot
Should Be Equal As Strings
```

**Description**
Fails if objects are unequal after converting them to strings. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. The `String and bytes normalization` section explains how ``ignore_case``, ``strip_spaces`` and ``collapse_spaces`` can be used for normalizing val...

## Should Be True

**Syntax**
```robot
Should Be True
```

**Description**
Fails if the given condition is not true. If ``condition`` is a string (e.g. ``${rc} < 10``), it is evaluated as a Python expression as explained in `Evaluating expressions` and the keyword status is decided based on the result. If a non-string item is given, the status is got directly from its [http://docs.python.org/library/stdtypes.html#truth|truth val...

## Should Contain

**Syntax**
```robot
Should Contain
```

**Description**
Fails if ``container`` does not contain ``item`` one or more times. Works with strings, lists, bytes, and anything that supports Python's ``in`` operator. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. The `String and bytes normalization` section explains h...

## Should Contain Any

**Syntax**
```robot
Should Contain Any
```

**Description**
Fails if ``container`` does not contain any of the ``*items``. Works with strings, lists, and anything that supports Python's ``in`` operator. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. The `String and bytes normalization` section explains how ``ignore_...

## Should Contain X Times

**Syntax**
```robot
Should Contain X Times
```

**Description**
Fails if ``container`` does not contain ``item`` ``count`` times. Works with strings, lists and all objects that `Get Count` works with. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. The `String and bytes normalization` section explains how ``ignore_case``...

## Should End With

**Syntax**
```robot
Should End With
```

**Description**
Fails if the string ``str1`` does not end with the string ``str2``. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. The `String and bytes normalization` section explains how ``ignore_case``, ``strip_spaces`` and ``collapse_spaces`` can be used for normalizin...

## Should Match

**Syntax**
```robot
Should Match
```

**Description**
Fails if the given ``string`` does not match the given ``pattern``. Pattern matching is similar as matching files in a shell with ``*``, ``?`` and ``[chars]`` acting as wildcards. See the `Glob patterns` section for more information. If ``ignore_case`` is given a true value, comparison is case-insensitive. See the `Controlling failure messages` section fo...

## Should Match Regexp

**Syntax**
```robot
Should Match Regexp
```

**Description**
Fails if ``string`` does not match ``pattern`` as a regular expression. See the `Regular expressions` section for more information about regular expressions and how to use then in Robot Framework test data. Notice that the given pattern does not need to match the whole string. For example, the pattern ``ello`` matches the string ``Hello world!``. If a ful...

## Should Not Be Empty

**Syntax**
```robot
Should Not Be Empty
```

**Description**
Verifies that the given item is not empty. The length of the item is got using the `Get Length` keyword. The default error message can be overridden with the ``msg`` argument.

## Should Not Be Equal

**Syntax**
```robot
Should Not Be Equal
```

**Description**
Fails if the given objects are equal. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. The `String and bytes normalization` section explains how ``ignore_case``, ``strip_spaces`` and ``collapse_spaces`` can be used for normalizing values before comparison. If...

## Should Not Be Equal As Integers

**Syntax**
```robot
Should Not Be Equal As Integers
```

**Description**
Fails if objects are equal after converting them to integers. See `Convert To Integer` for information how to convert integers from other bases than 10 using ``base`` argument or ``0b/0o/0x`` prefixes. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. See `Sho...

## Should Not Be Equal As Numbers

**Syntax**
```robot
Should Not Be Equal As Numbers
```

**Description**
Fails if objects are equal after converting them to real numbers. The conversion is done with `Convert To Number` keyword using the given ``precision``. See `Should Be Equal As Numbers` for examples on how to use ``precision`` and why it does not always work as expected. See the `Controlling failure messages` section for information about overriding the d...

## Should Not Be Equal As Strings

**Syntax**
```robot
Should Not Be Equal As Strings
```

**Description**
Fails if objects are equal after converting them to strings. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. The `String and bytes normalization` section explains how ``ignore_case``, ``strip_spaces`` and ``collapse_spaces`` can be used for normalizing value...

## Should Not Be True

**Syntax**
```robot
Should Not Be True
```

**Description**
Fails if the given condition is true. See `Should Be True` for details about how ``condition`` is evaluated and how ``msg`` can be used to override the default error message.

## Should Not Contain

**Syntax**
```robot
Should Not Contain
```

**Description**
Fails if ``container`` contains ``item`` one or more times. Works with strings, lists, and anything that supports Python's ``in`` operator. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. The `String and bytes normalization` section explains how ``ignore_cas...

## Should Not Contain Any

**Syntax**
```robot
Should Not Contain Any
```

**Description**
Fails if ``container`` contains one or more of the ``*items``. Works with strings, lists, and anything that supports Python's ``in`` operator. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. The `String and bytes normalization` section explains how ``ignore_...

## Should Not End With

**Syntax**
```robot
Should Not End With
```

**Description**
Fails if the string ``str1`` ends with the string ``str2``. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. The `String and bytes normalization` section explains how ``ignore_case``, ``strip_spaces`` and ``collapse_spaces`` can be used for normalizing values...

## Should Not Match

**Syntax**
```robot
Should Not Match
```

**Description**
Fails if the given ``string`` matches the given ``pattern``. Pattern matching is similar as matching files in a shell with ``*``, ``?`` and ``[chars]`` acting as wildcards. See the `Glob patterns` section for more information. If ``ignore_case`` is given a true value, comparison is case-insensitive. See the `Controlling failure messages` section for infor...

## Should Not Match Regexp

**Syntax**
```robot
Should Not Match Regexp
```

**Description**
Fails if ``string`` matches ``pattern`` as a regular expression. See `Should Match Regexp` for more information about arguments.

## Should Not Start With

**Syntax**
```robot
Should Not Start With
```

**Description**
Fails if the string ``str1`` starts with the string ``str2``. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. The `String and bytes normalization` section explains how ``ignore_case``, ``strip_spaces`` and ``collapse_spaces`` can be used for normalizing valu...

## Should Start With

**Syntax**
```robot
Should Start With
```

**Description**
Fails if the string ``str1`` does not start with the string ``str2``. See the `Controlling failure messages` section for information about overriding the default failure message with ``msg`` and ``values`` arguments. The `String and bytes normalization` section explains how ``ignore_case``, ``strip_spaces`` and ``collapse_spaces`` can be used for normaliz...

## Skip

**Syntax**
```robot
Skip
```

**Description**
Skips the rest of the current test. Skips the remaining keywords in the current test and sets the given message to the test. If the test has teardown, it will be executed.

## Skip If

**Syntax**
```robot
Skip If
```

**Description**
Skips the rest of the current test if the ``condition`` is True. Skips the remaining keywords in the current test and sets the given message to the test. If ``msg`` is not given, the ``condition`` will be used as the message. If the test has teardown, it will be executed. If the ``condition`` evaluates to False, does nothing.

## Sleep

**Syntax**
```robot
Sleep
```

**Description**
Pauses the test executed for the given time. ``time`` may be either a number or a time string. Time strings are in a format such as ``1 day 2 hours 3 minutes 4 seconds 5milliseconds`` or ``1d 2h 3m 4s 5ms``, and they are fully explained in an appendix of Robot Framework User Guide. Providing a value without specifying minutes or seconds, defaults to secon...

## Variable Should Exist

**Syntax**
```robot
Variable Should Exist
```

**Description**
Fails unless the given variable exists within the current scope. The name of the variable can be given either as a normal variable name like ``${name}`` or in escaped format like ``$name`` or ``\${name}``. For the reasons explained in the `Using variables with keywords creating or accessing variables` section, using the escaped format is recommended. The ...

## Variable Should Not Exist

**Syntax**
```robot
Variable Should Not Exist
```

**Description**
Fails if the given variable exists within the current scope. The name of the variable can be given either as a normal variable name like ``${name}`` or in escaped format like ``$name`` or ``\${name}``. For the reasons explained in the `Using variables with keywords creating or accessing variables` section, using the escaped format is recommended. The defa...

## Wait Until Keyword Succeeds

**Syntax**
```robot
Wait Until Keyword Succeeds
```

**Description**
Runs the specified keyword and retries if it fails. ``name`` and ``args`` define the keyword that is executed similarly as with `Run Keyword`. How long to retry running the keyword is defined using ``retry`` argument either as timeout or count. ``retry_interval`` is the time to wait between execution attempts. If ``retry`` is given as timeout, it must be ...
