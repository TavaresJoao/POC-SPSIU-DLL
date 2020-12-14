*** Settings ***
Library			../../pocSPSIU/pocSPSIU.py

*** Keywords ***
Que consiga realizar startup do dispositivo
    ${result_siu_start}=    Start Siu
    Set Global Variable     ${result_siu_start}

Validar se startup realizado com sucesso
    log                 ${result_siu_start}
    Should be True      ${result_siu_start} == 0

Que consiga realizar abertura do dispositivo
    ${result_siu_open}=     Open Siu
    Set Global Variable     ${result_siu_open}

Validar abertura realizada com sucesso
    log                 ${result_siu_open}
    Should Be true      ${result_siu_open} == 0

