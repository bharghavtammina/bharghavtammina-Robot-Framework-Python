# DateTime Keywords

## Add Time To Date

**Syntax**
```robot
Add Time To Date
```

**Description**
Adds time to date and returns the resulting date. Arguments: - ``date:`` Date to add time to in one of the supported `date formats`. - ``time:`` Time that is added in one of the supported `time formats`. - ``result_format:`` Format of the returned date. - ``exclude_millis:`` When set to any true value, rounds and drops milliseconds as explained in `millis...

## Add Time To Time

**Syntax**
```robot
Add Time To Time
```

**Description**
Adds time to another time and returns the resulting time. Arguments: - ``time1:`` First time in one of the supported `time formats`. - ``time2:`` Second time in one of the supported `time formats`. - ``result_format:`` Format of the returned time. - ``exclude_millis:`` When set to any true value, rounds and drops milliseconds as explained in `millisecond ...

## Convert Date

**Syntax**
```robot
Convert Date
```

**Description**
Converts between supported `date formats`. Arguments: - ``date:`` Date in one of the supported `date formats`. - ``result_format:`` Format of the returned date. - ``exclude_millis:`` When set to any true value, rounds and drops milliseconds as explained in `millisecond handling`. - ``date_format:`` Specifies possible `custom timestamp` format. Examples: |...

## Convert Time

**Syntax**
```robot
Convert Time
```

**Description**
Converts between supported `time formats`. Arguments: - ``time:`` Time in one of the supported `time formats`. - ``result_format:`` Format of the returned time. - ``exclude_millis:`` When set to any true value, rounds and drops milliseconds as explained in `millisecond handling`. Examples: | ${time} = | Convert Time | 10 seconds | | Should Be Equal | ${ti...

## Get Current Date

**Syntax**
```robot
Get Current Date
```

**Description**
Returns current local or UTC time with an optional increment. Arguments: - ``time_zone:`` Get the current time on this time zone. Currently only ``local`` (default) and ``UTC`` are supported. Has no effect if date is returned as an `epoch time`. - ``increment:`` Optional time increment to add to the returned date in one of the supported `time formats`. Ca...

## Subtract Date From Date

**Syntax**
```robot
Subtract Date From Date
```

**Description**
Subtracts date from another date and returns time between. Arguments: - ``date1:`` Date to subtract another date from in one of the supported `date formats`. - ``date2:`` Date that is subtracted in one of the supported `date formats`. - ``result_format:`` Format of the returned time (see `time formats`). - ``exclude_millis:`` When set to any true value, r...

## Subtract Time From Date

**Syntax**
```robot
Subtract Time From Date
```

**Description**
Subtracts time from date and returns the resulting date. Arguments: - ``date:`` Date to subtract time from in one of the supported `date formats`. - ``time:`` Time that is subtracted in one of the supported `time formats`. - ``result_format:`` Format of the returned date. - ``exclude_millis:`` When set to any true value, rounds and drops milliseconds as e...

## Subtract Time From Time

**Syntax**
```robot
Subtract Time From Time
```

**Description**
Subtracts time from another time and returns the resulting time. Arguments: - ``time1:`` Time to subtract another time from in one of the supported `time formats`. - ``time2:`` Time to subtract in one of the supported `time formats`. - ``result_format:`` Format of the returned time. - ``exclude_millis:`` When set to any true value, rounds and drops millis...
