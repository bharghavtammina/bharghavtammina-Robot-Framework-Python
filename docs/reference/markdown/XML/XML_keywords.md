# XML Keywords

## Add Element

**Syntax**
```robot
Add Element
```

**Description**
Adds a child element to the specified element. The element to whom to add the new element is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. The resulting XML structure is returned, and if the ``source`` is an already parsed XML structure, it is also modified in place. The ``element`` to add ca...

## Clear Element

**Syntax**
```robot
Clear Element
```

**Description**
Clears the contents of the specified element. The element to clear is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. The resulting XML structure is returned, and if the ``source`` is an already parsed XML structure, it is also modified in place. Clearing the element means removing its text, at...

## Copy Element

**Syntax**
```robot
Copy Element
```

**Description**
Returns a copy of the specified element. The element to copy is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. If the copy or the original element is modified afterward, the changes have no effect on the other. Examples using ``${XML}`` structure from `Example`: | ${elem} = | Get Element | ${X...

## Element Attribute Should Be

**Syntax**
```robot
Element Attribute Should Be
```

**Description**
Verifies that the specified attribute is ``expected``. The element whose attribute is verified is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. The keyword passes if the attribute ``name`` of the element is equal to the ``expected`` value, and otherwise it fails. The default error message can...

## Element Attribute Should Match

**Syntax**
```robot
Element Attribute Should Match
```

**Description**
Verifies that the specified attribute matches ``expected``. This keyword works exactly like `Element Attribute Should Be` except that the expected value can be given as a pattern that the attribute of the element must match. Pattern matching is similar as matching files in a shell with ``*``, ``?`` and ``[chars]`` acting as wildcards. See the `Pattern mat...

## Element Should Exist

**Syntax**
```robot
Element Should Exist
```

**Description**
Verifies that one or more element match the given ``xpath``. Arguments ``source`` and ``xpath`` have exactly the same semantics as with `Get Elements` keyword. Keyword passes if the ``xpath`` matches one or more elements in the ``source``. The default error message can be overridden with the ``message`` argument. See also `Element Should Not Exist` as wel...

## Element Should Not Exist

**Syntax**
```robot
Element Should Not Exist
```

**Description**
Verifies that no element match the given ``xpath``. Arguments ``source`` and ``xpath`` have exactly the same semantics as with `Get Elements` keyword. Keyword fails if the ``xpath`` matches any element in the ``source``. The default error message can be overridden with the ``message`` argument. See also `Element Should Exist` as well as `Get Element Count...

## Element Should Not Have Attribute

**Syntax**
```robot
Element Should Not Have Attribute
```

**Description**
Verifies that the specified element does not have attribute ``name``. The element whose attribute is verified is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. The keyword fails if the specified element has attribute ``name``. The default error message can be overridden with the ``message`` ar...

## Element Text Should Be

**Syntax**
```robot
Element Text Should Be
```

**Description**
Verifies that the text of the specified element is ``expected``. The element whose text is verified is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. The text to verify is got from the specified element using the same logic as with `Get Element Text`. This includes optional whitespace normaliz...

## Element Text Should Match

**Syntax**
```robot
Element Text Should Match
```

**Description**
Verifies that the text of the specified element matches ``expected``. This keyword works exactly like `Element Text Should Be` except that the expected value can be given as a pattern that the text of the element must match. Pattern matching is similar as matching files in a shell with ``*``, ``?`` and ``[chars]`` acting as wildcards. See the `Pattern mat...

## Element To String

**Syntax**
```robot
Element To String
```

**Description**
Returns the string representation of the specified element. The element to convert to a string is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. The string is returned as Unicode by default. If ``encoding`` argument is given any value, the string is returned as bytes in the specified encoding....

## Elements Should Be Equal

**Syntax**
```robot
Elements Should Be Equal
```

**Description**
Verifies that the given ``source`` element is equal to ``expected``. Both ``source`` and ``expected`` can be given as a path to an XML file, as a string containing XML, or as an already parsed XML element structure. See `introduction` for more information about parsing XML in general. The keyword passes if the ``source`` element and ``expected`` element a...

## Elements Should Match

**Syntax**
```robot
Elements Should Match
```

**Description**
Verifies that the given ``source`` element matches ``expected``. This keyword works exactly like `Elements Should Be Equal` except that texts and attribute values in the expected value can be given as patterns. Pattern matching is similar as matching files in a shell with ``*``, ``?`` and ``[chars]`` acting as wildcards. See the `Pattern matching` section...

## Evaluate Xpath

**Syntax**
```robot
Evaluate Xpath
```

**Description**
Evaluates the given xpath expression and returns results. The element in which context the expression is executed is specified using ``source`` and ``context`` arguments. They have exactly the same semantics as ``source`` and ``xpath`` arguments have with `Get Element` keyword. The xpath expression to evaluate is given as ``expression`` argument. The resu...

## Get Child Elements

**Syntax**
```robot
Get Child Elements
```

**Description**
Returns the child elements of the specified element as a list. The element whose children to return is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. All the direct child elements of the specified element are returned. If the element has no children, an empty list is returned. Examples using `...

## Get Element

**Syntax**
```robot
Get Element
```

**Description**
Returns an element in the ``source`` matching the ``xpath``. The ``source`` can be a path to an XML file, a string containing XML, or an already parsed XML element. The ``xpath`` specifies which element to find. See the `introduction` for more details about both the possible sources and the supported xpath syntax. The keyword fails if more, or less, than ...

## Get Element Attribute

**Syntax**
```robot
Get Element Attribute
```

**Description**
Returns the named attribute of the specified element. The element whose attribute to return is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. The value of the attribute ``name`` of the specified element is returned. If the element does not have such element, the ``default`` value is returned i...

## Get Element Attributes

**Syntax**
```robot
Get Element Attributes
```

**Description**
Returns all attributes of the specified element. The element whose attributes to return is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. Attributes are returned as a Python dictionary. It is a copy of the original attributes so modifying it has no effect on the XML structure. Examples using `...

## Get Element Count

**Syntax**
```robot
Get Element Count
```

**Description**
Returns and logs how many elements the given ``xpath`` matches. Arguments ``source`` and ``xpath`` have exactly the same semantics as with `Get Elements` keyword that this keyword uses internally. See also `Element Should Exist` and `Element Should Not Exist`.

## Get Element Text

**Syntax**
```robot
Get Element Text
```

**Description**
Returns all text of the element, possibly whitespace normalized. The element whose text to return is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. This keyword returns all the text of the specified element, including all the text its children and grandchildren contain. If the element has no t...

## Get Elements

**Syntax**
```robot
Get Elements
```

**Description**
Returns a list of elements in the ``source`` matching the ``xpath``. The ``source`` can be a path to an XML file, a string containing XML, or an already parsed XML element. The ``xpath`` specifies which element to find. See the `introduction` for more details. Elements matching the ``xpath`` are returned as a list. If no elements match, an empty list is r...

## Get Elements Texts

**Syntax**
```robot
Get Elements Texts
```

**Description**
Returns text of all elements matching ``xpath`` as a list. The elements whose text to return is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Elements` keyword. The text of the matched elements is returned using the same logic as with `Get Element Text`. This includes optional whitespace normalization using th...

## Log Element

**Syntax**
```robot
Log Element
```

**Description**
Logs the string representation of the specified element. The element specified with ``source`` and ``xpath`` is first converted into a string using `Element To String` keyword internally. The resulting string is then logged using the given ``level``. The logged string is also returned.

## Parse Xml

**Syntax**
```robot
Parse Xml
```

**Description**
Parses the given XML file or string into an element structure. The ``source`` can either be a path to an XML file or a string containing XML. In both cases the XML is parsed into ElementTree [https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element|Element] structure. Possible comments and processing instructions in the s...

## Remove Element

**Syntax**
```robot
Remove Element
```

**Description**
Removes the element matching ``xpath`` from the ``source`` structure. The element to remove from the ``source`` is specified with ``xpath`` using the same semantics as with `Get Element` keyword. The resulting XML structure is returned, and if the ``source`` is an already parsed XML structure, it is also modified in place. The keyword fails if ``xpath`` d...

## Remove Element Attribute

**Syntax**
```robot
Remove Element Attribute
```

**Description**
Removes attribute ``name`` from the specified element. The element whose attribute to remove is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. The resulting XML structure is returned, and if the ``source`` is an already parsed XML structure, it is also modified in place. It is not a failure to...

## Remove Element Attributes

**Syntax**
```robot
Remove Element Attributes
```

**Description**
Removes all attributes from the specified element. The element whose attributes to remove is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. The resulting XML structure is returned, and if the ``source`` is an already parsed XML structure, it is also modified in place. Use `Remove Element Attri...

## Remove Elements

**Syntax**
```robot
Remove Elements
```

**Description**
Removes all elements matching ``xpath`` from the ``source`` structure. The elements to remove from the ``source`` are specified with ``xpath`` using the same semantics as with `Get Elements` keyword. The resulting XML structure is returned, and if the ``source`` is an already parsed XML structure, it is also modified in place. It is not a failure if ``xpa...

## Remove Elements Attribute

**Syntax**
```robot
Remove Elements Attribute
```

**Description**
Removes attribute ``name`` from the specified elements. Like `Remove Element Attribute` but removes the attribute of all elements matching the given ``xpath``.

## Remove Elements Attributes

**Syntax**
```robot
Remove Elements Attributes
```

**Description**
Removes all attributes from the specified elements. Like `Remove Element Attributes` but removes all attributes of all elements matching the given ``xpath``.

## Save Xml

**Syntax**
```robot
Save Xml
```

**Description**
Saves the given element to the specified file. The element to save is specified with ``source`` using the same semantics as with `Get Element` keyword. The file where the element is saved is denoted with ``path`` and the encoding to use with ``encoding``. The resulting file always contains the XML declaration. The resulting XML file may not be exactly the...

## Set Element Attribute

**Syntax**
```robot
Set Element Attribute
```

**Description**
Sets attribute ``name`` of the specified element to ``value``. The element whose attribute to set is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. The resulting XML structure is returned, and if the ``source`` is an already parsed XML structure, it is also modified in place. It is possible to...

## Set Element Tag

**Syntax**
```robot
Set Element Tag
```

**Description**
Sets the tag of the specified element. The element whose tag to set is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. The resulting XML structure is returned, and if the ``source`` is an already parsed XML structure, it is also modified in place. Examples using ``${XML}`` structure from `Examp...

## Set Element Text

**Syntax**
```robot
Set Element Text
```

**Description**
Sets text and/or tail text of the specified element. The element whose text to set is specified using ``source`` and ``xpath``. They have exactly the same semantics as with `Get Element` keyword. The resulting XML structure is returned, and if the ``source`` is an already parsed XML structure, it is also modified in place. Element's text and tail text are...

## Set Elements Attribute

**Syntax**
```robot
Set Elements Attribute
```

**Description**
Sets attribute ``name`` of the specified elements to ``value``. Like `Set Element Attribute` but sets the attribute of all elements matching the given ``xpath``.

## Set Elements Tag

**Syntax**
```robot
Set Elements Tag
```

**Description**
Sets the tag of the specified elements. Like `Set Element Tag` but sets the tag of all elements matching the given ``xpath``.

## Set Elements Text

**Syntax**
```robot
Set Elements Text
```

**Description**
Sets text and/or tail text of the specified elements. Like `Set Element Text` but sets the text or tail of all elements matching the given ``xpath``.
