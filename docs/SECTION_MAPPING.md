# Section Mapping For Robot Files

This maps Robot Framework file sections to documentation folders under `docs/curated/`.

## 1) `docs/curated/settings/`
- Place only `*** Settings ***` items:
  - `Library`
  - `Resource`
  - `Variables` (file import)
  - `Suite Setup`, `Suite Teardown`
  - `Test Setup`, `Test Teardown`
  - `Documentation`, `Metadata`

## 2) `docs/curated/variables/`
- Place only `*** Variables ***` declarations:
  - `${scalar}`
  - `@{list}`
  - `&{dict}`
- Note: `Set Variable` is a keyword call, so use in steps (`*** Test Cases ***` / `*** Keywords ***`).

## 3) `docs/curated/test-steps/`
- Place executable test steps:
  - API keywords (`Create Session`, `GET/POST/PUT/PATCH/DELETE On Session`)
  - data build keywords (`Create Dictionary`, `Set To Dictionary`)
  - assertions (`Should Be Equal`, etc.)
  - logs (`Log`, `Log To Console`)
  - Selenium execution steps

## 4) `docs/curated/user-keywords/`
- Place reusable custom keywords under `*** Keywords ***`:
  - `[Arguments]`
  - `[Return]`
  - any sequence of calls you want to reuse

## 5) `docs/curated/javascript/`
- JavaScript snippets used inside `Execute Javascript` / `Execute JavaScript`

---

## Quick usage order in a `.robot` file
1. `*** Settings ***`
2. `*** Variables ***`
3. `*** Test Cases ***` or `*** Tasks ***`
4. `*** Keywords ***` (optional but recommended for reuse)
