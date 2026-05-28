*** Settings ***
Library    RequestsLibrary

*** Variables ***
${base_url}    http://restapi.demoqa.com
${city}    Delhi

*** Test Cases ***
get_weather_info
    create session    mysession    ${base_url}
    ${response}=    get request mysession    /utilites/weather/city/${city}
    log    ${response.status_code}
    log    ${response.content}
    log    ${response.headers}

