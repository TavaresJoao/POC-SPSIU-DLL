*** Settings ***
Resource			resources/BDDpt-br.robot
Resource			resources/resources.robot

*** Test Cases ***
O sistema deve realizar start no dispositivo com sucesso
	[tags]									start_sucesso
	Dado que consiga realizar startup do dispositivo
	Então validar se startup realizado com sucesso

O sistema deve abrir o dispositivo com sucesso
	[tags]									open_sucesso
	Dado que consiga realizar abertura do dispositivo
	Então Validar abertura realizada com sucesso

