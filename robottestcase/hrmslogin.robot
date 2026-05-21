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
    maximize browser window   
    set selenium speed  2 seconds
    input text  id:username  lokesh.jothiram@tringapps.net
    sleep 3
    input text  id:password  Qwertypad@123
    click element  xpath:/html/body/div[1]/main/div[1]/form/button
    close browser
