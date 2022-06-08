*** Settings ***
Library     Browser

*** Test Cases ***
Perform Button Clicks
    New Browser     chromium        headless=false
    New Page        http://localhost:3000
    Get Title       ==  The Programming Mantis
    FOR     ${count}        IN RANGE        100
        Click       text="Go to Another"
        Click       text="Back"
    END