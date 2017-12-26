*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL} =  https://flipkart.com

*** Test Cases ***
Testcase for Way2Automation site
    [Documentation]
    [Tags]
    OpenBrowser  ${URL}  firefox
    sleep  3s
    CloseBrowser

*** Keywords ***
