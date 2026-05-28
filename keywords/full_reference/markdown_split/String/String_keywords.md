# String Keywords

## Convert To Lower Case

**Syntax**
```robot
Convert To Lower Case
```

**Description**
Converts string to lower case. Uses Python's standard [https://docs.python.org/library/stdtypes.html#str.lower|lower()] method. Examples: | ${str1} = | Convert To Lower Case | ABC | | ${str2} = | Convert To Lower Case | 1A2c3D | | Should Be Equal | ${str1} | abc | | Should Be Equal | ${str2} | 1a2c3d | If this keyword is used with bytes, only ASCII charac...

## Convert To Title Case

**Syntax**
```robot
Convert To Title Case
```

**Description**
Converts string to title case. Uses the following algorithm: - Split the string to words from whitespace characters (spaces, newlines, etc.). - Exclude words that are not all lower case. This preserves, for example, "OK" and "iPhone". - Exclude also words listed in the optional ``exclude`` argument. - Title case the first alphabetical character of each wo...

## Convert To Upper Case

**Syntax**
```robot
Convert To Upper Case
```

**Description**
Converts string to upper case. Uses Python's standard [https://docs.python.org/library/stdtypes.html#str.upper|upper()] method. Examples: | ${str1} = | Convert To Upper Case | abc | | ${str2} = | Convert To Upper Case | 1a2C3d | | Should Be Equal | ${str1} | ABC | | Should Be Equal | ${str2} | 1A2C3D | If this keyword is used with bytes, only ASCII charac...

## Decode Bytes To String

**Syntax**
```robot
Decode Bytes To String
```

**Description**
Decodes the given ``bytes`` to a string using the given ``encoding``. ``errors`` argument controls what to do if decoding some bytes fails. All values accepted by ``decode`` method in Python are valid, but in practice the following values are most useful: - ``strict``: fail if characters cannot be decoded (default) - ``ignore``: ignore characters that can...

## Encode String To Bytes

**Syntax**
```robot
Encode String To Bytes
```

**Description**
Encodes the given ``string`` to bytes using the given ``encoding``. ``errors`` argument controls what to do if encoding some characters fails. All values accepted by ``encode`` method in Python are valid, but in practice the following values are most useful: - ``strict``: fail if characters cannot be encoded (default) - ``ignore``: ignore characters that ...

## Fetch From Left

**Syntax**
```robot
Fetch From Left
```

**Description**
Returns contents of the ``string`` before the first occurrence of ``marker``. If the ``marker`` is not found, whole string is returned. If the first argument is bytes, the second argument is automatically converted to bytes as well. This is new in Robot Framework 7.4. See also `Fetch From Right`, `Split String` and `Split String From Right`.

## Fetch From Right

**Syntax**
```robot
Fetch From Right
```

**Description**
Returns contents of the ``string`` after the last occurrence of ``marker``. If the ``marker`` is not found, whole string is returned. If the first argument is bytes, the second argument is automatically converted to bytes as well. This is new in Robot Framework 7.4. See also `Fetch From Left`, `Split String` and `Split String From Right`.

## Format String

**Syntax**
```robot
Format String
```

**Description**
Formats a ``template`` using the given ``positional`` and ``named`` arguments. The template can be either be a string or an absolute path to an existing file. In the latter case the file is read and its contents are used as the template. If the template file contains non-ASCII characters, it must be encoded using UTF-8. The template is formatted using Pyt...

## Generate Random String

**Syntax**
```robot
Generate Random String
```

**Description**
Generates a string with a desired ``length`` from the given ``chars``. ``length`` can be given as a number, a string representation of a number, or as a range of numbers, such as ``5-10``. When a range of values is given the range will be selected by random within the range. The population sequence ``chars`` contains the characters to use when generating ...

## Get Line

**Syntax**
```robot
Get Line
```

**Description**
Returns the specified line from the given ``string``. Line numbering starts from 0, and it is possible to use negative indices to refer to lines from the end. The line is returned without the newline character. Examples: | ${first} = | Get Line | ${string} | 0 | | ${2nd last} = | Get Line | ${string} | -2 | Use `Split To Lines` if all lines are needed.

## Get Line Count

**Syntax**
```robot
Get Line Count
```

**Description**
Returns and logs the number of lines in the given string.

## Get Lines Containing String

**Syntax**
```robot
Get Lines Containing String
```

**Description**
Returns lines of the given ``string`` that contain the ``pattern``. The ``pattern`` is always considered to be a normal string, not a glob or regexp pattern. A line matches if the ``pattern`` is found anywhere on it. The match is case-sensitive by default, but that can be changed by giving ``ignore_case`` a true value. This option is new in Robot Framewor...

## Get Lines Matching Pattern

**Syntax**
```robot
Get Lines Matching Pattern
```

**Description**
Returns lines of the given ``string`` that match the ``pattern``. The ``pattern`` is a _glob pattern_ where: | ``*`` | matches everything | | ``?`` | matches any single character | | ``[chars]`` | matches any character inside square brackets (e.g. ``[abc]`` matches either ``a``, ``b`` or ``c``) | | ``[!chars]`` | matches any character not inside square br...

## Get Lines Matching Regexp

**Syntax**
```robot
Get Lines Matching Regexp
```

**Description**
Returns lines of the given ``string`` that match the regexp ``pattern``. See `BuiltIn.Should Match Regexp` for more information about Python regular expression syntax in general and how to use it in Robot Framework data in particular. Lines match only if they match the pattern fully by default, but partial matching can be enabled by giving the ``partial_m...

## Get Regexp Matches

**Syntax**
```robot
Get Regexp Matches
```

**Description**
Returns a list of all non-overlapping matches in the given string. ``string`` is the string to find matches from and ``pattern`` is the regular expression. See `BuiltIn.Should Match Regexp` for more information about Python regular expression syntax in general and how to use it in Robot Framework data in particular. If no groups are used, the returned lis...

## Get Substring

**Syntax**
```robot
Get Substring
```

**Description**
Returns a substring from ``start`` index to ``end`` index. The ``start`` index is inclusive and ``end`` is exclusive. Indexing starts from 0, and it is possible to use negative indices to refer to characters from the end. Examples: | ${ignore first} = | Get Substring | ${string} | 1 | | | ${ignore last} = | Get Substring | ${string} | 0 | -1 | | ${5th to ...

## Remove String

**Syntax**
```robot
Remove String
```

**Description**
Removes all ``removables`` from the given ``string``. ``removables`` are used as literal strings. Each removable will be matched to a temporary string from which preceding removables have been already removed. See second example below. Use `Remove String Using Regexp` if more powerful pattern matching is needed. If only a certain number of matches should ...

## Remove String Using Regexp

**Syntax**
```robot
Remove String Using Regexp
```

**Description**
Removes ``patterns`` from the given ``string``. This keyword is otherwise identical to `Remove String`, but the ``patterns`` to search for are considered to be a regular expression. See `Replace String Using Regexp` for more information about the regular expression syntax. That keyword can also be used if there is a need to remove only a certain number of...

## Replace String

**Syntax**
```robot
Replace String
```

**Description**
Replaces ``search_for`` in the given ``string`` with ``replace_with``. ``search_for`` is used as a literal string. See `Replace String Using Regexp` if more powerful pattern matching is needed. If you need to just remove a string see `Remove String`. If the optional argument ``count`` is given, only that many occurrences from left are replaced. Negative `...

## Replace String Using Regexp

**Syntax**
```robot
Replace String Using Regexp
```

**Description**
Replaces ``pattern`` in the given ``string`` with ``replace_with``. This keyword is otherwise identical to `Replace String`, but the ``pattern`` to search for is considered to be a regular expression. See `BuiltIn.Should Match Regexp` for more information about Python regular expression syntax in general and how to use it in Robot Framework data in partic...

## Should Be Byte String

**Syntax**
```robot
Should Be Byte String
```

**Description**
Fails if the given ``item`` is not a byte string. Use `Should Be String` if you want to verify the ``item`` is a string. The default error message can be overridden with the optional ``msg`` argument.

## Should Be Lower Case

**Syntax**
```robot
Should Be Lower Case
```

**Description**
Fails if the given ``string`` is not in lower case. For example, ``'string'`` and ``'with specials!'`` would pass, and ``'String'``, ``''`` and ``' '`` would fail. The default error message can be overridden with the optional ``msg`` argument. See also `Should Be Upper Case` and `Should Be Title Case`.

## Should Be String

**Syntax**
```robot
Should Be String
```

**Description**
Fails if the given ``item`` is not a string. The default error message can be overridden with the optional ``msg`` argument.

## Should Be Title Case

**Syntax**
```robot
Should Be Title Case
```

**Description**
Fails if given ``string`` is not title. ``string`` is a title cased string if there is at least one upper case letter in each word. For example, ``'This Is Title'`` and ``'OK, Give Me My iPhone'`` would pass. ``'all words lower'`` and ``'Word In lower'`` would fail. This logic changed in Robot Framework 4.0 to be compatible with `Convert to Title Case`. S...

## Should Be Unicode String

**Syntax**
```robot
Should Be Unicode String
```

**Description**
Fails if the given ``item`` is not a Unicode string. On Python 3 this keyword behaves exactly the same way `Should Be String`. That keyword should be used instead and this keyword will be deprecated.

## Should Be Upper Case

**Syntax**
```robot
Should Be Upper Case
```

**Description**
Fails if the given ``string`` is not in upper case. For example, ``'STRING'`` and ``'WITH SPECIALS!'`` would pass, and ``'String'``, ``''`` and ``' '`` would fail. The default error message can be overridden with the optional ``msg`` argument. See also `Should Be Title Case` and `Should Be Lower Case`.

## Should Not Be String

**Syntax**
```robot
Should Not Be String
```

**Description**
Fails if the given ``item`` is a string. The default error message can be overridden with the optional ``msg`` argument.

## Split String

**Syntax**
```robot
Split String
```

**Description**
Splits the ``string`` using ``separator`` as a delimiter string. If a ``separator`` is not given, any whitespace string is a separator. In that case also possible consecutive whitespace as well as leading and trailing whitespace is ignored. Split words are returned as a list. If the optional ``max_split`` is given, at most ``max_split`` splits are done, a...

## Split String From Right

**Syntax**
```robot
Split String From Right
```

**Description**
Splits the ``string`` using ``separator`` starting from right. Same as `Split String`, but splitting is started from right. This has an effect only when ``max_split`` is given. Examples: | ${first} | ${rest} = | Split String | ${string} | - | 1 | | ${rest} | ${last} = | Split String From Right | ${string} | - | 1 | If the first argument is bytes, the seco...

## Split String To Characters

**Syntax**
```robot
Split String To Characters
```

**Description**
Splits the given ``string`` to characters. Example: | @{characters} = | Split String To Characters | ${string} | Bytes support is new in Robot Framework 7.4.

## Split To Lines

**Syntax**
```robot
Split To Lines
```

**Description**
Splits the given string to lines. It is possible to get only a selection of lines from ``start`` to ``end`` so that ``start`` index is inclusive and ``end`` is exclusive. Line numbering starts from 0, and it is possible to use negative indices to refer to lines from the end. Lines are returned without the newlines. The number of returned lines is automati...

## Strip String

**Syntax**
```robot
Strip String
```

**Description**
Remove leading and/or trailing whitespaces from the given string. ``mode`` is either ``left`` to remove leading characters, ``right`` to remove trailing characters, ``both`` (default) to remove the characters from both sides of the string or ``none`` to return the unmodified string. If the optional ``characters`` is given, it must be a string and the char...
