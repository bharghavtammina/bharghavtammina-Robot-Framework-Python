# OperatingSystem Keywords

## Append To Environment Variable

**Syntax**
```robot
Append To Environment Variable
```

**Description**
Appends given ``values`` to environment variable ``name``. If the environment variable already exists, values are added after it, and otherwise a new environment variable is created. Values are, by default, joined together using the operating system path separator (``;`` on Windows, ``:`` elsewhere). This can be changed by giving a separator after the val...

## Append To File

**Syntax**
```robot
Append To File
```

**Description**
Appends the given content to the specified file. If the file exists, the given text is written to its end. If the file does not exist, it is created. Other than not overwriting possible existing files, this keyword works exactly like `Create File`. See its documentation for more details about the usage.

## Copy Directory

**Syntax**
```robot
Copy Directory
```

**Description**
Copies the source directory into the destination. If the destination exists, the source is copied under it. Otherwise, the destination directory and the possible missing intermediate directories are created.

## Copy File

**Syntax**
```robot
Copy File
```

**Description**
Copies the source file into the destination. Source must be a path to an existing file or a glob pattern (see `Glob patterns`) that matches exactly one file. How the destination is interpreted is explained below. 1) If the destination is an existing file, the source file is copied over it. 2) If the destination is an existing directory, the source file is...

## Copy Files

**Syntax**
```robot
Copy Files
```

**Description**
Copies specified files to the target directory. Source files can be given as exact paths and as glob patterns (see `Glob patterns`). At least one source must be given, but it is not an error if it is a pattern that does not match anything. Last argument must be the destination directory. If the destination does not exist, it will be created. Examples: | C...

## Count Directories In Directory

**Syntax**
```robot
Count Directories In Directory
```

**Description**
Wrapper for `Count Items In Directory` returning only directory count.

## Count Files In Directory

**Syntax**
```robot
Count Files In Directory
```

**Description**
Wrapper for `Count Items In Directory` returning only file count.

## Count Items In Directory

**Syntax**
```robot
Count Items In Directory
```

**Description**
Returns and logs the number of all items in the given directory. The argument ``pattern`` has the same semantics as with `List Directory` keyword. The count is returned as an integer, so it must be checked e.g. with the built-in keyword `Should Be Equal As Integers`.

## Create Binary File

**Syntax**
```robot
Create Binary File
```

**Description**
Creates a binary file with the given content. If content is given as a Unicode string, it is first converted to bytes character by character. All characters with ordinal below 256 can be used and are converted to bytes with same values. Using characters with higher ordinal is an error. Byte strings, and possible other types, are written to the file as is....

## Create Directory

**Syntax**
```robot
Create Directory
```

**Description**
Creates the specified directory. Possible intermediate directories are created as well. Passes if the directory already exists, but fails if the path exists and is not a directory.

## Create File

**Syntax**
```robot
Create File
```

**Description**
Creates a file with the given content and encoding. If the directory where the file is created does not exist, it is automatically created along with possible missing intermediate directories. Possible existing file is overwritten. On Windows newline characters (``\n``) in content are automatically converted to Windows native newline sequence (``\r\n``). ...

## Directory Should Be Empty

**Syntax**
```robot
Directory Should Be Empty
```

**Description**
Fails unless the specified directory is empty. The default error message can be overridden with the ``msg`` argument.

## Directory Should Exist

**Syntax**
```robot
Directory Should Exist
```

**Description**
Fails unless the given path points to an existing directory. The path can be given as an exact path or as a glob pattern. See the `Glob patterns` section for details about the supported syntax. The default error message can be overridden with the ``msg`` argument.

## Directory Should Not Be Empty

**Syntax**
```robot
Directory Should Not Be Empty
```

**Description**
Fails if the specified directory is empty. The default error message can be overridden with the ``msg`` argument.

## Directory Should Not Exist

**Syntax**
```robot
Directory Should Not Exist
```

**Description**
Fails if the given path points to an existing file. The path can be given as an exact path or as a glob pattern. See the `Glob patterns` section for details about the supported syntax. The default error message can be overridden with the ``msg`` argument.

## Empty Directory

**Syntax**
```robot
Empty Directory
```

**Description**
Deletes all the content from the given directory. Deletes both files and subdirectories, but the specified directory itself if not removed. Use `Remove Directory` if you want to remove the whole directory.

## Environment Variable Should Be Set

**Syntax**
```robot
Environment Variable Should Be Set
```

**Description**
Fails if the specified environment variable is not set. Environment variable is considered not to be set if it does not exist or if its value is an empty string. The default error message can be overridden with the ``msg`` argument.

## Environment Variable Should Not Be Set

**Syntax**
```robot
Environment Variable Should Not Be Set
```

**Description**
Fails if the specified environment variable is set. Environment variable is considered not to be set if it does not exist or if its value is an empty string. The default error message can be overridden with the ``msg`` argument.

## File Should Be Empty

**Syntax**
```robot
File Should Be Empty
```

**Description**
Fails unless the specified file is empty. The default error message can be overridden with the ``msg`` argument.

## File Should Exist

**Syntax**
```robot
File Should Exist
```

**Description**
Fails unless the given ``path`` points to an existing file. The path can be given as an exact path or as a glob pattern. See the `Glob patterns` section for details about the supported syntax. The default error message can be overridden with the ``msg`` argument.

## File Should Not Be Empty

**Syntax**
```robot
File Should Not Be Empty
```

**Description**
Fails if the specified file is empty. The default error message can be overridden with the ``msg`` argument.

## File Should Not Exist

**Syntax**
```robot
File Should Not Exist
```

**Description**
Fails if the given path points to an existing file. The path can be given as an exact path or as a glob pattern. See the `Glob patterns` section for details about the supported syntax. The default error message can be overridden with the ``msg`` argument.

## Get Binary File

**Syntax**
```robot
Get Binary File
```

**Description**
Returns the contents of a specified file. This keyword reads the specified file and returns the contents as is. See also `Get File`.

## Get Environment Variable

**Syntax**
```robot
Get Environment Variable
```

**Description**
Returns the value of an environment variable with the given name. If no environment variable is found, returns possible default value. If no default value is given, the keyword fails. Returned variables are automatically decoded to Unicode using the system encoding. Note that you can also access environment variables directly using the variable syntax ``%...

## Get Environment Variables

**Syntax**
```robot
Get Environment Variables
```

**Description**
Returns currently available environment variables as a dictionary. Both keys and values are decoded to Unicode using the system encoding. Altering the returned dictionary has no effect on the actual environment variables.

## Get File

**Syntax**
```robot
Get File
```

**Description**
Returns the contents of a specified file. This keyword reads the specified file and returns the contents. Line breaks in content are converted to platform independent form. See also `Get Binary File`. ``encoding`` defines the encoding of the file. The default value is ``UTF-8``, which means that UTF-8 and ASCII encoded files are read correctly. In additio...

## Get File Size

**Syntax**
```robot
Get File Size
```

**Description**
Returns and logs file size as an integer in bytes.

## Get Modified Time

**Syntax**
```robot
Get Modified Time
```

**Description**
Returns the last modification time of a file or directory. How time is returned is determined based on the given ``format`` string as follows. Note that all checks are case-insensitive. Returned time is also automatically logged. 1) If ``format`` contains the word ``epoch``, the time is returned in seconds after the UNIX epoch. The return value is always ...

## Grep File

**Syntax**
```robot
Grep File
```

**Description**
Returns the lines of the specified file that match the ``pattern``. This keyword reads a file from the file system using the defined ``path``, ``encoding`` and ``encoding_errors`` similarly as `Get File`. A difference is that only the lines that match the given ``pattern`` are returned. Lines are returned as a single string concatenated back together with...

## Join Path

**Syntax**
```robot
Join Path
```

**Description**
Joins the given path part(s) to the given base path. The path separator (``/`` or ``\``) is inserted when needed and the possible absolute paths handled as expected. The resulted path is also normalized. Examples: | ${path} = | Join Path | my | path | | ${p2} = | Join Path | my/ | path/ | | ${p3} = | Join Path | my | path | my | file.txt | | ${p4} = | Joi...

## Join Paths

**Syntax**
```robot
Join Paths
```

**Description**
Joins given paths with base and returns resulted paths. See `Join Path` for more information. Examples: | @{p1} = | Join Paths | base | example | other | | | @{p2} = | Join Paths | /my/base | /example | other | | | @{p3} = | Join Paths | my/base | example/path/ | other | one/more | => - @{p1} = ['base/example', 'base/other'] - @{p2} = ['/example', '/my/ba...

## List Directories In Directory

**Syntax**
```robot
List Directories In Directory
```

**Description**
Wrapper for `List Directory` that returns only directories.

## List Directory

**Syntax**
```robot
List Directory
```

**Description**
Returns and logs items in a directory, optionally filtered with ``pattern``. File and directory names are returned in case-sensitive alphabetical order, e.g. ``['A Name', 'Second', 'a lower case name', 'one more']``. Implicit directories ``.`` and ``..`` are not returned. The returned items are automatically logged. File and directory names are returned r...

## List Files In Directory

**Syntax**
```robot
List Files In Directory
```

**Description**
Wrapper for `List Directory` that returns only files.

## Log Environment Variables

**Syntax**
```robot
Log Environment Variables
```

**Description**
Logs all environment variables using the given log level. Environment variables are also returned the same way as with `Get Environment Variables` keyword.

## Log File

**Syntax**
```robot
Log File
```

**Description**
Wrapper for `Get File` that also logs the returned file. The file is logged with the INFO level. If you want something else, just use `Get File` and the built-in keyword `Log` with the desired level. See `Get File` for more information about ``encoding`` and ``encoding_errors`` arguments.

## Move Directory

**Syntax**
```robot
Move Directory
```

**Description**
Moves the source directory into a destination. Uses `Copy Directory` keyword internally, and ``source`` and ``destination`` arguments have exactly same semantics as with that keyword.

## Move File

**Syntax**
```robot
Move File
```

**Description**
Moves the source file into the destination. Arguments have exactly same semantics as with `Copy File` keyword. Destination file path is returned. If the source and destination are on the same filesystem, rename operation is used. Otherwise, file is copied to the destination filesystem and then removed from the original filesystem. See also `Move Files`, `...

## Move Files

**Syntax**
```robot
Move Files
```

**Description**
Moves specified files to the target directory. Arguments have exactly same semantics as with `Copy Files` keyword. See also `Move File`, `Copy File`, and `Copy Files`.

## Normalize Path

**Syntax**
```robot
Normalize Path
```

**Description**
Normalizes the given path. - Collapses redundant separators and up-level references. - Converts ``/`` to ``\`` on Windows. - Replaces initial ``~`` or ``~user`` by that user's home directory. - If ``case_normalize`` is given a true value on Windows, converts the path to all lowercase. - Converts ``pathlib.Path`` instances to ``str``. Examples: | ${path1} ...

## Remove Directory

**Syntax**
```robot
Remove Directory
```

**Description**
Removes the directory pointed to by the given ``path``. If the second argument ``recursive`` is given a true value, the directory is removed recursively. Otherwise, removing fails if the directory is not empty. If the directory pointed to by the ``path`` does not exist, the keyword passes, but it fails, if the ``path`` points to a file.

## Remove Environment Variable

**Syntax**
```robot
Remove Environment Variable
```

**Description**
Deletes the specified environment variable. Does nothing if the environment variable is not set. It is possible to remove multiple variables by passing them to this keyword as separate arguments.

## Remove File

**Syntax**
```robot
Remove File
```

**Description**
Removes a file with the given path. Passes if the file does not exist, but fails if the path does not point to a regular file (e.g. it points to a directory). The path can be given as an exact path or as a glob pattern. See the `Glob patterns` section for details about the supported syntax. If the path is a pattern, all files matching it are removed.

## Remove Files

**Syntax**
```robot
Remove Files
```

**Description**
Uses `Remove File` to remove multiple files one-by-one. Example: | Remove Files | ${TEMPDIR}${/}foo.txt | ${TEMPDIR}${/}bar.txt | ${TEMPDIR}${/}zap.txt |

## Run

**Syntax**
```robot
Run
```

**Description**
_This keyword is considered deprecated. Use the [http://robotframework.org/robotframework/latest/libraries/Process.html| Process] library instead._ Runs the given command in the system and returns the output. The execution status of the command _is not checked_ by this keyword, and it must be done separately based on the returned output. If the execution ...

## Run And Return Rc

**Syntax**
```robot
Run And Return Rc
```

**Description**
_This keyword is considered deprecated. Use the [http://robotframework.org/robotframework/latest/libraries/Process.html| Process] library instead._ Runs the given command in the system and returns the return code (RC). The return code is returned as a positive integer in range from 0 to 255 as returned by the executed command. On some operating systems (n...

## Run And Return Rc And Output

**Syntax**
```robot
Run And Return Rc And Output
```

**Description**
_This keyword is considered deprecated. Use the [http://robotframework.org/robotframework/latest/libraries/Process.html| Process] library instead._ Runs the given command in the system and returns the return code (RC) and output. The return code is returned similarly as with `Run And Return RC` and the output similarly as with `Run`. Examples: | ${rc} | $...

## Set Environment Variable

**Syntax**
```robot
Set Environment Variable
```

**Description**
Sets an environment variable to a specified value. Values are converted to strings automatically. Set variables are automatically encoded using the system encoding.

## Set Modified Time

**Syntax**
```robot
Set Modified Time
```

**Description**
Sets the file modification and access times. Changes the modification and access times of the given file to the value determined by ``mtime``. The time can be given in different formats described below. Note that all checks involving strings are case-insensitive. Modified time can only be set to regular files. 1) If ``mtime`` is a number, or a string that...

## Should Exist

**Syntax**
```robot
Should Exist
```

**Description**
Fails unless the given path (file or directory) exists. The path can be given as an exact path or as a glob pattern. See the `Glob patterns` section for details about the supported syntax. The default error message can be overridden with the ``msg`` argument.

## Should Not Exist

**Syntax**
```robot
Should Not Exist
```

**Description**
Fails if the given path (file or directory) exists. The path can be given as an exact path or as a glob pattern. See the `Glob patterns` section for details about the supported syntax. The default error message can be overridden with the ``msg`` argument.

## Split Extension

**Syntax**
```robot
Split Extension
```

**Description**
Splits the extension from the given path. The given path is first normalized (e.g. possible trailing path separators removed, special directories ``..`` and ``.`` removed). The base path and extension are returned as separate components so that the dot used as an extension separator is removed. If the path contains no extension, an empty string is returne...

## Split Path

**Syntax**
```robot
Split Path
```

**Description**
Splits the given path from the last path separator (``/`` or ``\``). The given path is first normalized (e.g. a possible trailing path separator is removed, special directories ``..`` and ``.`` removed). The parts that are split are returned as separate components. Examples: | ${path1} | ${dir} = | Split Path | abc/def | | ${path2} | ${file} = | Split Pat...

## Touch

**Syntax**
```robot
Touch
```

**Description**
Emulates the UNIX touch command. Creates a file, if it does not exist. Otherwise, changes its access and modification times to the current time. Fails if used with the directories or the parent directory of the given file does not exist.

## Wait Until Created

**Syntax**
```robot
Wait Until Created
```

**Description**
Waits until the given file or directory is created. The path can be given as an exact path or as a glob pattern. See the `Glob patterns` section for details about the supported syntax. If the path is a pattern, the keyword returns when an item matching it is created. Waits for 1 minute by default, but that can be changed by using the ``timeout`` argument....

## Wait Until Removed

**Syntax**
```robot
Wait Until Removed
```

**Description**
Waits until the given file or directory is removed. The path can be given as an exact path or as a glob pattern. See the `Glob patterns` section for details about the supported syntax. If the path is a pattern, the keyword waits until all matching items are removed. Waits for 1 minute by default, but that can be changed by using the ``timeout`` argument. ...
