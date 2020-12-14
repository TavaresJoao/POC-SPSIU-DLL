*** Settings ***
Library			../pocSPSIU/pocSPSIU.py


*** Test Cases ***
O sistema deve realizar start no dispositivo com sucesso
	[tags]									start_sucesso
	Realizar start do dispositivo
	Validar start realizado com sucesso

O sistema deve abrir o dispositivo com sucesso
	[tags]									open_sucesso
	Realizar abertura do dispositivo
	Validar abertura realizada com sucesso


*** Keywords ***
Realizar start do dispositivo
    ${result_siu_start}=    Start Siu
    Set Global Variable     ${result_siu_start}

Validar start realizado com sucesso
    log                 ${result_siu_start}
    Should be True      ${result_siu_start} == 0


Realizar abertura do dispositivo
    ${result_siu_open}=     Open Siu
    Set Global Variable     ${result_siu_open}

Validar abertura realizada com sucesso
    log                 ${result_siu_open}
    Should Be true      ${result_siu_open} == 0

