# Collections Keywords

## Append To List

**Syntax**
```robot
Append To List
```

**Description**
Adds ``values`` to the end of ``list``. Starting from Robot Framework 7.4, the modified list is also returned. Example: | Append To List | ${L1} | xxx | | | | Append To List | ${L2} | x | y | z | => | ${L1} = ['a', 'xxx'] | ${L2} = ['a', 'b', 'x', 'y', 'z']

## Combine Lists

**Syntax**
```robot
Combine Lists
```

**Description**
Combines the given ``lists`` together and returns the result. The given lists are not altered by this keyword. Example: | ${x} = | Combine Lists | ${L1} | ${L2} | | | ${y} = | Combine Lists | ${L1} | ${L2} | ${L1} | => | ${x} = ['a', 'a', 'b'] | ${y} = ['a', 'a', 'b', 'a'] | ${L1} and ${L2} are not changed.

## Convert To Dictionary

**Syntax**
```robot
Convert To Dictionary
```

**Description**
Converts the given ``item`` to a Python ``dict`` type. Mainly useful for converting other mappings to normal dictionaries. This includes converting Robot Framework's own ``DotDict`` instances that it uses if variables are created using the ``&{var}`` syntax. Use `Create Dictionary` from the BuiltIn library for constructing new dictionaries.

## Convert To List

**Syntax**
```robot
Convert To List
```

**Description**
Converts the given ``item`` to a Python ``list`` type. Mainly useful for converting tuples and other iterable to lists. Use `Create List` from the BuiltIn library for constructing new lists. To split strings into characters, the `Split String To Characters` from the String Library can be used.

## Copy Dictionary

**Syntax**
```robot
Copy Dictionary
```

**Description**
Returns a copy of the given dictionary. By default, returns a new dictionary with same items as in the original. Set the ``deepcopy`` argument to a true value if also items should be copied. The given dictionary is never altered by this keyword.

## Copy List

**Syntax**
```robot
Copy List
```

**Description**
Returns a copy of the given list. By default, returns a new list with same items as in the original. Set the ``deepcopy`` argument to a true value if also items should be copied. The given list is never altered by this keyword.

## Count Values In List

**Syntax**
```robot
Count Values In List
```

**Description**
Returns the number of occurrences of the given ``value`` in ``list``. The search can be narrowed to the selected sublist by the ``start`` and ``end`` indexes having the same semantics as with `Get Slice From List` keyword. The given list is never altered by this keyword. Example: | ${x} = | Count Values In List | ${L3} | b | => | ${x} = 1 | ${L3} is not c...

## Dictionaries Should Be Equal

**Syntax**
```robot
Dictionaries Should Be Equal
```

**Description**
Fails if the given dictionaries are not equal. First the equality of dictionaries' keys is checked and after that all the key value pairs. If there are differences between the values, those are listed in the error message. The types of the dictionaries do not need to be same. ``ignore_keys`` can be used to provide a list of keys to ignore in the compariso...

## Dictionary Should Contain Item

**Syntax**
```robot
Dictionary Should Contain Item
```

**Description**
An item of ``key`` / ``value`` must be found in a ``dictionary``. Use the ``msg`` argument to override the default error message. The ``ignore_case`` argument can be used to make comparison case-insensitive. See the `Ignore case` section for more details. This option is new in Robot Framework 7.0.

## Dictionary Should Contain Key

**Syntax**
```robot
Dictionary Should Contain Key
```

**Description**
Fails if ``key`` is not found from ``dictionary``. Use the ``msg`` argument to override the default error message. The ``ignore_case`` argument can be used to make comparison case-insensitive. See the `Ignore case` section for more details. This option is new in Robot Framework 7.0.

## Dictionary Should Contain Sub Dictionary

**Syntax**
```robot
Dictionary Should Contain Sub Dictionary
```

**Description**
Fails unless all items in ``dict2`` are found from ``dict1``. See `Lists Should Be Equal` for more information about configuring the error message with ``msg`` and ``values`` arguments. The ``ignore_case`` argument can be used to make comparison case-insensitive. See the `Ignore case` section for more details. This option is new in Robot Framework 7.0. Th...

## Dictionary Should Contain Value

**Syntax**
```robot
Dictionary Should Contain Value
```

**Description**
Fails if ``value`` is not found from ``dictionary``. Use the ``msg`` argument to override the default error message. The ``ignore_case`` argument can be used to make comparison case-insensitive. See the `Ignore case` section for more details. This option is new in Robot Framework 7.0.

## Dictionary Should Not Contain Key

**Syntax**
```robot
Dictionary Should Not Contain Key
```

**Description**
Fails if ``key`` is found from ``dictionary``. Use the ``msg`` argument to override the default error message. The ``ignore_case`` argument can be used to make comparison case-insensitive. See the `Ignore case` section for more details. This option is new in Robot Framework 7.0.

## Dictionary Should Not Contain Value

**Syntax**
```robot
Dictionary Should Not Contain Value
```

**Description**
Fails if ``value`` is found from ``dictionary``. Use the ``msg`` argument to override the default error message. The ``ignore_case`` argument can be used to make comparison case-insensitive. See the `Ignore case` section for more details. This option is new in Robot Framework 7.0.

## Get Dictionary Items

**Syntax**
```robot
Get Dictionary Items
```

**Description**
Returns items of the given ``dictionary`` as a list. Uses `Get Dictionary Keys` to get keys and then returns corresponding items. By default, keys are sorted and items returned in that order, but this can be changed by giving ``sort_keys`` a false value. Items are returned as a flat list so that first item is a key, second item is a corresponding value, t...

## Get Dictionary Keys

**Syntax**
```robot
Get Dictionary Keys
```

**Description**
Returns keys of the given ``dictionary`` as a list. By default, keys are returned in sorted order (assuming they are sortable), but they can be returned in the original order by giving ``sort_keys`` a false value. The given ``dictionary`` is never altered by this keyword. Example: | ${sorted} = | Get Dictionary Keys | ${D3} | | ${unsorted} = | Get Diction...

## Get Dictionary Values

**Syntax**
```robot
Get Dictionary Values
```

**Description**
Returns values of the given ``dictionary`` as a list. Uses `Get Dictionary Keys` to get keys and then returns corresponding values. By default, keys are sorted and values returned in that order, but this can be changed by giving ``sort_keys`` a false value. The given ``dictionary`` is never altered by this keyword. Example: | ${sorted} = | Get Dictionary ...

## Get From Dictionary

**Syntax**
```robot
Get From Dictionary
```

**Description**
Returns a value from the given ``dictionary`` based on the given ``key``. If the given ``key`` cannot be found from the ``dictionary``, this keyword fails. If optional ``default`` value is given, it will be returned instead of failing. The given dictionary is never altered by this keyword. Example: | ${value} = | Get From Dictionary | ${D3} | b | => | ${v...

## Get From List

**Syntax**
```robot
Get From List
```

**Description**
Returns the value specified with an ``index`` from ``list``. The given list is never altered by this keyword. Index ``0`` means the first position, ``1`` the second, and so on. Similarly, ``-1`` is the last position, ``-2`` the second last, and so on. Using an index that does not exist on the list causes an error. The index can be either an integer or a s...

## Get Index From List

**Syntax**
```robot
Get Index From List
```

**Description**
Returns the index of the first occurrence of the ``value`` on the list. The search can be narrowed to the selected sublist by the ``start`` and ``end`` indexes having the same semantics as with `Get Slice From List` keyword. In case the value is not found, -1 is returned. The given list is never altered by this keyword. Example: | ${x} = | Get Index From ...

## Get Match Count

**Syntax**
```robot
Get Match Count
```

**Description**
Returns the count of matches to ``pattern`` in ``list``. For more information on ``pattern``, ``case_insensitive/ignore_case``, and ``whitespace_insensitive/ignore_whitespace``, see `Should Contain Match`. Examples: | ${count}= | Get Match Count | ${list} | a* | # ${count} will be the count of strings beginning with 'a' | | ${count}= | Get Match Count | $...

## Get Matches

**Syntax**
```robot
Get Matches
```

**Description**
Returns a list of matches to ``pattern`` in ``list``. For more information on ``pattern``, ``case_insensitive/ignore_case``, and ``whitespace_insensitive/ignore_whitespace``, see `Should Contain Match`. Examples: | ${matches}= | Get Matches | ${list} | a* | # ${matches} will contain any string beginning with 'a' | | ${matches}= | Get Matches | ${list} | r...

## Get Slice From List

**Syntax**
```robot
Get Slice From List
```

**Description**
Returns a slice of the given list between ``start`` and ``end`` indexes. The given list is never altered by this keyword. If both ``start`` and ``end`` are given, a sublist containing values from ``start`` to ``end`` is returned. This is the same as ``list[start:end]`` in Python. To get all items from the beginning, use 0 as the start value, and to get al...

## Insert Into List

**Syntax**
```robot
Insert Into List
```

**Description**
Inserts ``value`` into ``list`` to the position specified with ``index``. Index ``0`` adds the value into the first position, ``1`` to the second, and so on. Inserting from right works with negative indices so that ``-1`` is the second last position, ``-2`` third last, and so on. Use `Append To List` to add items to the end of the list. If the absolute va...

## Keep In Dictionary

**Syntax**
```robot
Keep In Dictionary
```

**Description**
Keeps the given ``keys`` in the ``dictionary`` and removes all others. If the given ``key`` does not exist in the ``dictionary``, it is ignored. Starting from Robot Framework 7.4, the modified dictionary is also returned. Example: | Keep In Dictionary | ${D5} | b | x | d | => | ${D5} = {'b': 2, 'd': 4}

## List Should Contain Sub List

**Syntax**
```robot
List Should Contain Sub List
```

**Description**
Fails if not all elements in ``list2`` are found in ``list1``. The order of values and the number of values are not taken into account. See `Lists Should Be Equal` for more information about configuring the error message with ``msg`` and ``values`` arguments. The ``ignore_case`` argument can be used to make comparison case-insensitive. See the `Ignore cas...

## List Should Contain Value

**Syntax**
```robot
List Should Contain Value
```

**Description**
Fails if the ``value`` is not found from ``list``. Use the ``msg`` argument to override the default error message. The ``ignore_case`` argument can be used to make comparison case-insensitive. See the `Ignore case` section for more details. This option is new in Robot Framework 7.0.

## List Should Not Contain Duplicates

**Syntax**
```robot
List Should Not Contain Duplicates
```

**Description**
Fails if any element in the ``list`` is found from it more than once. The default error message lists all the elements that were found from the ``list`` multiple times, but it can be overridden by giving a custom ``msg``. All multiple times found items and their counts are also logged. This keyword works with all iterables that can be converted to a list....

## List Should Not Contain Value

**Syntax**
```robot
List Should Not Contain Value
```

**Description**
Fails if the ``value`` is found from ``list``. Use the ``msg`` argument to override the default error message. The ``ignore_case`` argument can be used to make comparison case-insensitive. See the `Ignore case` section for more details. This option is new in Robot Framework 7.0.

## Lists Should Be Equal

**Syntax**
```robot
Lists Should Be Equal
```

**Description**
Fails if given lists are unequal. The keyword first verifies that the lists have equal lengths, and then it checks are all their values equal. Possible differences between the values are listed in the default error message like ``Index 4: ABC != Abc``. The types of the lists do not need to be the same. For example, Python tuple and list with same content ...

## Log Dictionary

**Syntax**
```robot
Log Dictionary
```

**Description**
Logs the contents of the ``dictionary`` using the given ``level``.

## Log List

**Syntax**
```robot
Log List
```

**Description**
Logs contents of the ``list`` using the given ``level``.

## Pop From Dictionary

**Syntax**
```robot
Pop From Dictionary
```

**Description**
Pops the given ``key`` from the ``dictionary`` and returns its value. The keyword fails if the given ``key`` cannot be found from the ``dictionary`` by default. If optional ``default`` value is given, it will be returned instead. Example: | ${val}= | Pop From Dictionary | ${D3} | b | => | ${val} = 2 | ${D3} = {'a': 1, 'c': 3}

## Remove Duplicates

**Syntax**
```robot
Remove Duplicates
```

**Description**
Returns a list without duplicates based on the given ``list``. Creates and returns a new list that contains all items in the given list so that one item can appear only once. Order of the items in the new list is the same as in the original except for missing duplicates. Number of the removed duplicates is logged.

## Remove From Dictionary

**Syntax**
```robot
Remove From Dictionary
```

**Description**
Removes the given ``keys`` from the ``dictionary``. If the given ``key`` does not exist in the ``dictionary``, it is ignored. Starting from Robot Framework 7.4, the modified dictionary is also returned. Example: | Remove From Dictionary | ${D3} | b | x | y | => | ${D3} = {'a': 1, 'c': 3}

## Remove From List

**Syntax**
```robot
Remove From List
```

**Description**
Removes and returns the value specified with an ``index`` from ``list``. Index ``0`` means the first position, ``1`` the second and so on. Similarly, ``-1`` is the last position, ``-2`` the second last, and so on. Using an index that does not exist on the list causes an error. The index can be either an integer or a string that can be converted to an inte...

## Remove Values From List

**Syntax**
```robot
Remove Values From List
```

**Description**
Removes all occurrences of given ``values`` from ``list``. It is not an error if a value does not exist in the list at all. Starting from Robot Framework 7.4, the modified list is also returned. Example: | Remove Values From List | ${L4} | a | c | e | f | => | ${L4} = ['b', 'd']

## Reverse List

**Syntax**
```robot
Reverse List
```

**Description**
Reverses the given list in place. Note that the given list is changed and nothing is returned. Use `Copy List` first, if you need to keep also the original order. Starting from Robot Framework 7.4, the reversed list is also returned. | Reverse List | ${L3} | => | ${L3} = ['c', 'b', 'a']

## Set List Value

**Syntax**
```robot
Set List Value
```

**Description**
Sets the value of ``list`` specified by ``index`` to the given ``value``. Index ``0`` means the first position, ``1`` the second and so on. Similarly, ``-1`` is the last position, ``-2`` second last, and so on. Using an index that does not exist on the list causes an error. The index can be either an integer or a string that can be converted to an integer...

## Set To Dictionary

**Syntax**
```robot
Set To Dictionary
```

**Description**
Adds the given ``key_value_pairs`` and/or ``items`` to the ``dictionary``. If given items already exist in the dictionary, their values are updated. The modified dictionary is also returned. It is easiest to specify items using the ``name=value`` syntax: | Set To Dictionary | ${D1} | key=value | second=${2} | => | ${D1} = {'a': 1, 'key': 'value', 'second'...

## Should Contain Match

**Syntax**
```robot
Should Contain Match
```

**Description**
Fails if ``pattern`` is not found in ``list``. By default, pattern matching is similar to matching files in a shell and is case-sensitive and whitespace-sensitive. In the pattern syntax, ``*`` matches to anything and ``?`` matches to any single character. You can also prepend ``glob=`` to your pattern to explicitly use this pattern matching behavior. If y...

## Should Not Contain Match

**Syntax**
```robot
Should Not Contain Match
```

**Description**
Fails if ``pattern`` is found in ``list``. Exact opposite of `Should Contain Match` keyword. See that keyword for information about arguments and usage in general.

## Sort List

**Syntax**
```robot
Sort List
```

**Description**
Sorts the given list in place. Sorting fails if items in the list are not comparable with each others. For example, sorting a list containing strings and numbers is not possible. Note that the given list is changed and nothing is returned. Use `Copy List` first, if you need to preserve the list also in the original order. Starting from Robot Framework 7.4...
