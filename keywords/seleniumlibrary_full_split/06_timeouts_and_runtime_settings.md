# SeleniumLibrary Keywords - Timeouts And Runtime Settings

## Get Selenium Page Load Timeout

**Syntax**
```robot
Get Selenium Page Load Timeout
```

**Description**
Gets the time to wait for a page load to complete before raising a timeout exception. The value is returned as a human-readable string like ``1 second``. See the `Page load` section above for more information. New in SeleniumLibrary 6.1

## Get Selenium Speed

**Syntax**
```robot
Get Selenium Speed
```

**Description**
Gets the delay that is waited after each Selenium command. The value is returned as a human-readable string like ``1 second``. See the `Selenium Speed` section above for more information.

## Get Selenium Timeout

**Syntax**
```robot
Get Selenium Timeout
```

**Description**
Gets the timeout that is used by various keywords. The value is returned as a human-readable string like ``1 second``. See the `Timeout` section above for more information.

## Set Selenium Page Load Timeout

**Syntax**
```robot
Set Selenium Page Load Timeout
```

**Description**
Sets the page load timeout value used by Selenium. The value can be given as a number that is considered to be seconds or as a human-readable string like ``1 second``. The previous value is returned and can be used to restore the original value later if needed. In contrast to `Set Selenium Timeout` and `Set Selenium...

## Set Selenium Speed

**Syntax**
```robot
Set Selenium Speed
```

**Description**
Sets the delay that is waited after each Selenium command. The value can be given as a number that is considered to be seconds or as a human-readable string like ``1 second``. The previous value is returned and can be used to restore the original value later if needed. See the `Selenium Speed` section above for more...

## Set Selenium Timeout

**Syntax**
```robot
Set Selenium Timeout
```

**Description**
Sets the timeout that is used by various keywords. The value can be given as a number that is considered to be seconds or as a human-readable string like ``1 second``. The previous value is returned and can be used to restore the original value later if needed. See the `Timeout` section above for more information. E...
