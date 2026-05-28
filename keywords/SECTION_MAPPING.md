# Section Mapping For Robot Files

This folder structure answers: where should a command be placed in a `.robot` file?

## 1) `settings/`
- Place only `*** Settings ***` items:
  - `Library`
  - `Resource`
  - `Variables` (file import)
  - `Suite Setup`, `Suite Teardown`
  - `Test Setup`, `Test Teardown`
  - `Documentation`, `Metadata`

## 2) `variables/`
- Place only `*** Variables ***` declarations:
  - `${scalar}`
  - `@{list}`
  - `&{dict}`
- Note: `Set Variable` is a keyword call, so use in steps (`*** Test Cases ***` / `*** Keywords ***`).

## 3) `testcases/`
- Place executable test steps:
  - API keywords (`Create Session`, `GET/POST/PUT/PATCH/DELETE On Session`)
  - data build keywords (`Create Dictionary`, `Set To Dictionary`)
  - assertions (`Should Be Equal`, etc.)
  - logs (`Log`, `Log To Console`)
  - Selenium execution steps

## 4) `keywords/`
- Place reusable custom keywords under `*** Keywords ***`:
  - `[Arguments]`
  - `[Return]`
  - any sequence of calls you want to reuse

---

## Quick usage order in a `.robot` file
1. `*** Settings ***`
2. `*** Variables ***`
3. `*** Test Cases ***`
4. `*** Keywords ***` (optional but recommended for reuse)
