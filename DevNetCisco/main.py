#########Configuracion de Placa SBC Board Cisco pk ################


#con este codigo la placa abrira a traves del sensor de movimiento
#la puerta y tambien enciende la maquina de cafe
#cuando esta en movimiento

from gpio import *
from time import *


sensor=9
door=7
coffe = 5


def main():
	while True:
		pinMode(door, OUT)
		
		if digitalRead(sensor==HIGH):
			customWrite(door, "1")
			customWrite(coffe, "1")
			print("Persona Acercandose")
			delay(3000)
		else:
			customWrite(door, "0")
			customWrite(coffe, "0")
	
if __name__ == "__main__":
	main()
