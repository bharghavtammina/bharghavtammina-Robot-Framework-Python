# Process Keywords

## Get Process Id

**Syntax**
```robot
Get Process Id
```

**Description**
Returns the process ID (pid) of the process as an integer. If ``handle`` is not given, uses the current `active process`. Starting from Robot Framework 5.0, it is also possible to directly access the ``pid`` attribute of the ``subprocess.Popen`` object returned by `Start Process` like ``${process.pid}``.

## Get Process Object

**Syntax**
```robot
Get Process Object
```

**Description**
Return the underlying ``subprocess.Popen`` object. If ``handle`` is not given, uses the current `active process`. Starting from Robot Framework 5.0, `Start Process` returns the created ``subprocess.Popen`` object, not a generic handle, making this keyword mostly redundant.

## Get Process Result

**Syntax**
```robot
Get Process Result
```

**Description**
Returns the specified `result object` or some of its attributes. The given ``handle`` specifies the process whose results should be returned. If no ``handle`` is given, results of the current `active process` are returned. In either case, the process must have been finishes before this keyword can be used. In practice this means that processes started wit...

## Is Process Running

**Syntax**
```robot
Is Process Running
```

**Description**
Checks is the process running or not. If ``handle`` is not given, uses the current `active process`. Returns ``True`` if the process is still running and ``False`` otherwise.

## Join Command Line

**Syntax**
```robot
Join Command Line
```

**Description**
Joins arguments into one command line string. In resulting command line string arguments are delimited with a space, arguments containing spaces are surrounded with quotes, and possible quotes are escaped with a backslash. Command to join can be given as individual arguments or as a list. Giving command as individual arguments: | ${cmd} = | Join Command L...

## Process Should Be Running

**Syntax**
```robot
Process Should Be Running
```

**Description**
Verifies that the process is running. If ``handle`` is not given, uses the current `active process`. Fails if the process has stopped.

## Process Should Be Stopped

**Syntax**
```robot
Process Should Be Stopped
```

**Description**
Verifies that the process is not running. If ``handle`` is not given, uses the current `active process`. Fails if the process is still running.

## Run Process

**Syntax**
```robot
Run Process
```

**Description**
Runs a process and waits for it to complete. ``command`` and ``arguments`` specify the command to execute and arguments passed to it. See `Specifying command and arguments` for more details. The started process can be configured using ``cwd``, ``shell``, ``stdout``, ``stderr``, ``stdin``, ``output_encoding``, ``alias``, ``env`` and ``env_extra`` parameter...

## Send Signal To Process

**Syntax**
```robot
Send Signal To Process
```

**Description**
Sends the given ``signal`` to the specified process. If ``handle`` is not given, uses the current `active process`. Signal can be specified either as an integer as a signal name. In the latter case it is possible to give the name both with or without ``SIG`` prefix, but names are case-sensitive. For example, all the examples below send signal ``INT (2)``:...

## Split Command Line

**Syntax**
```robot
Split Command Line
```

**Description**
Splits command line string into a list of arguments. String is split from spaces, but argument surrounded in quotes may contain spaces in them. If ``escaping`` is given a true value, then backslash is treated as an escape character. It can escape unquoted spaces, quotes inside quotes, and so on, but it also requires doubling backslashes in Windows paths a...

## Start Process

**Syntax**
```robot
Start Process
```

**Description**
Starts a new process on background. See `Specifying command and arguments` and `Process configuration` sections for more information about the arguments, and `Run Process` keyword for related examples. This includes information about redirecting process outputs to avoid process handing due to output buffers getting full. Makes the started process new `act...

## Switch Process

**Syntax**
```robot
Switch Process
```

**Description**
Makes the specified process the current `active process`. The handle can be an identifier returned by `Start Process` or the ``alias`` given to it explicitly. Example: | Start Process | prog1 | alias=process1 | | Start Process | prog2 | alias=process2 | | # currently active process is process2 | | Switch Process | process1 | | # now active process is proc...

## Terminate All Processes

**Syntax**
```robot
Terminate All Processes
```

**Description**
Terminates all still running processes started by this library. This keyword can be used in suite teardown or elsewhere to make sure that all processes are stopped, Tries to terminate processes gracefully by default, but can be configured to forcefully kill them immediately. See `Terminate Process` that this keyword uses internally for more details.

## Terminate Process

**Syntax**
```robot
Terminate Process
```

**Description**
Stops the process gracefully or forcefully. If ``handle`` is not given, uses the current `active process`. By default, first tries to stop the process gracefully. If the process does not stop in 30 seconds, or the ``kill`` argument is given a true value, kills the process forcefully. Stops also all the child processes of the originally started process. Wa...

## Wait For Process

**Syntax**
```robot
Wait For Process
```

**Description**
Waits for the process to complete or to reach the given timeout. The process to wait for must have been started earlier with `Start Process`. If ``handle`` is not given, uses the current `active process`. ``timeout`` defines the maximum time to wait for the process. It can be given in [http://robotframework.org/robotframework/latest/RobotFrameworkUserGuid...
