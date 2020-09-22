import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
import datetime


GPIO.setmode( GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
m=open("registro.txt","w")

def luz1On():
	GPIO.output(7, True)
	time.sleep
	mqttc.publish("mdpilatuna.fie@gmail.com/WEB")
	m.write(horaActual +str(" Boton Encendido Sensor 1") +"\n")
	c=("sensor1 encendido ")
	mqttc.publish("mdpilatuna.fie@unach.edu.ec/WEB", c)

def luzOff():
	GPIO.output(7, False)
	time.sleep(0.5)
	mqttc.publish("mdpilatuna.fie@unach.edu.ec/WEB")
	m.write(horaActual +str(" Boton Apagado Sensor 1") +"\n")
	c=("sensor1 Apagado ")
	mqttc.publish("mdpilatuna.fie@unach.edu.ec/WEB", c)

def luz2On():
	GPIO.output(11,True)
	time.sleep
	mqttc.publish("mdpilatuna.fie@unach.edu.ec/WEB")
	m.write(horaActual +str(" Boton Encendido Sensor 2") +"\n")
	c=("sensor2 encendido ")
	mqttc.publish("mdpilatuna.fie@unach.edu.ec/WEB", c)

def luz2Off():
	GPIO.output(11, False)
	time.sleep(0.5)
	mqttc.publish("mdpilatuna.fie@unach.edu.ec/WEB")
	m.write(horaActual +str(" Boton Apagado Sensor 2") +"\n")
	c=("sensor2 Apagado ")
	mqttc.publish("mdpilatuna.fie@unach.edu.ec/WEB", c )

def on_message(client, obj, msg):
	accion=(msg.payload.decode("utf-8"))
	print(accion)
	if accion=="L10":
		luz1On()
	if accion== "L1N":
		luzOff()
	if accion=="L2O":
		luz2On()
	if accion== "L2N":
		luz2Off()

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.username_pw_set("mdpilatuna.fie@unach.edu.ec", "quitociudadhermosa")
mqttc.connect("maqiatto.com",1883)
mqttc.subscribe("mdpilatuna.fie@unach.edu.ec/RASP", 0)

rc=0
print("conectado..")
i=0

while rc==0:
	time.sleep(2)
	rc = mqttc.loop()
	i=i+1
	horaActual=datetime.datetime.now().strftime("%H : %M : %S")
	print(horaActual)

	
        
       
        

