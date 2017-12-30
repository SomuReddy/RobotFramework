*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL} =  http://www.way2automation.com
${BROWSER} =  firefox

*** Test Cases ***
Testcase for Way2Automation site
    [Documentation]
    [Tags]
    Set  set log level  Debug
    OpenBrowser  ${URL}  ${BROWSER}
    sleep  3s
    CloseBrowser

*** Keywords ***
