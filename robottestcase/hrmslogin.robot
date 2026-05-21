*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${hrms_url}  https://hrms.tringapps.net/login/?next=/
${webdriver}  chrome

*** Test Cases ***
LoginTest
    LoginToHRMS

*** Keywords ***
LoginToHRMS
    open browser  ${hrms_url}  ${webdriver}    
    input text  id:username  lokesh.jothiram@tringapps.net
    input text  id:password  Qwertypad@123
    click element  xpath:/html/body/div[1]/main/div[1]/form/button
    close browser
