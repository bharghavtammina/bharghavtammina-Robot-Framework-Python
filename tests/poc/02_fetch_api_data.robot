*** Settings ***
Documentation    POC: call a public API and log the response (no browser).
Library          RequestsLibrary
Library          ../libraries/helpers.py

*** Variables ***
${API_BASE}    https://httpbin.org

*** Tasks ***
Fetch Sample API Data
    ${when}=    Get Run Timestamp
    Log    API automation started at ${when}    console=yes
    Create Session    httpbin    ${API_BASE}
    ${response}=    GET On Session    httpbin    /get
    Should Be Equal As Numbers    ${response.status_code}    200
    ${url}=    Set Variable    ${response.json()}[url]
    Log    API returned URL: ${url}    console=yes
