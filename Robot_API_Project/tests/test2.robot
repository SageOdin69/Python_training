*** Settings ***
Resource        C:/Python_training/Robot_API_Project/resources/equipment_keyword.resource

Suite Setup     Create API Session

*** Test Cases ***
TC1_GETAll
    log to Console      Test1 Started
    ${response} =       GET All Equipments        200
    ${data} =       Set Variable        ${response.json()}
    Should Be Equal As Integers     ${response.status_code}    200
    Length Should be        ${data}     3
TC2_GETEquipmentById
    log to Console      Test2 Started
    ${response} =       Get Equipment by id     101     200
    ${data} =       Set Variable        ${response.json()}
    Should Be Equal As Integers     ${response.status_code}    200
    should Be Equal As Integers     ${data}[id]     101
    #Length Should be        ${data}     4