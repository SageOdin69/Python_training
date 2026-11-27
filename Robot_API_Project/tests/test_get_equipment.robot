*** Settings ***
Library     RequestsLibrary
 
*** Variables ***
${BASE_URL}     http://127.0.0.1:5000

*** Keywords ***
Create API Session
    Create session      Equipment_API       ${BASE_URL}
 
*** Test Cases ***
Tc001_Test Get All Equipment
    Create API Session
    ${response}=   GET on session       Equipment_API       /api/equipment
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}
 
Tc002_Test Get One
    Create API Session
    ${response}=   GET on session       Equipment_API       /api/equipment/101
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Tc003_Test Get One
    Create API Session
    ${response}=   GET on session       Equipment_API       /api/equipment/101
    Should Be Equal As Integers    ${response.status_code}    200
    ${data} =       Set Variable        ${response.json()}
    Should Be Equal As Integers     ${data}[id]     101
    Should Be Equal As Strings     ${data}[name]     Flight Control Unit
    Should Be Equal As Strings     ${data}[type]     FCV
    Should Be Equal As Strings     ${data}[status]     Operational
    Log To Console    ${response.json()}
    Log To Console      All Equipment Details: ${data}
