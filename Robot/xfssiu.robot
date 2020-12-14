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
    log     ('sucesso')

Validar start realizado com sucesso
    log     ('sucesso')

Realizar abertura do dispositivo
    log     ('sucesso')

Validar abertura realizada com sucesso
    log     ('sucesso')

