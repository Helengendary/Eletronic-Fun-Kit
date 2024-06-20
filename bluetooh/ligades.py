import uBlue as ublue
import _thread
import time
import machine
from machine import Pin
import urequests
import ujson
import network

#Dê um nome para o seu bluetooth
nome = "HELENA"

#Seta o pino do led padrão da esp32, podendo ser 2 ou 22
led = Pin(32, Pin.OUT)

#Credenciais do WIFI
nome = "Vivo-Internet-BF17"
senha = "78814222"

# Endereço do firebase
url = "https://iiot-7276b-default-rtdb.firebaseio.com/Helena.json"
SECRET_KEY = ""

estado = 0


def conectarWifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando no WiFi...")
        wlan.connect(nome, senha)
        while not wlan.isconnected():
            pass
    print("Wifi conectado... IP: {}".format(wlan.ifconfig()[0]))

def enviarFire(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + SECRET_KEY
    }

    response = urequests.put(url, data=ujson.dumps(data), headers=headers)
    print("Firebase Response:", response.text)
    response.close()

def funcaoA():
    ublue.ublueON(nome)

#Função facultativa para utilizar as informações recebidas

conectarWifi()
_thread.start_new_thread(funcaoA,())

while True:
    print(ublue.info)
    if (int(ublue.info) == 1): #Lógica invertida pois nessa esp32 usa-se o pull_up
        estado = 1
    elif (int(ublue.info) == 0):
        estado = 0
        
    informacao = {
        "LED": f"{estado}",
    }

    enviarFire(informacao)
    time.sleep(1)



# #Função obrigatória para iniciar o funcionamento do bluetooth
# def funcaoA():
#     ublue.ublueON(nome)
# 
# #Função facultativa para utilizar as informações recebidas
# def funcaoB():
#     while True: 
#         try:
#             print(ublue.info)
#             if (int(ublue.info) == 1): #Lógica invertida pois nessa esp32 usa-se o pull_up
#                 estado = 1
#             elif (int(ublue.info) == 0):
#                 estado = 0
#                         
#             informacao = {
#                 "LED": f"{estado}"
#             }
#             
#             enviarFire(informacao)
#         except ValueError:
#             print("Entre com um valor inteiro")
#             ublue.info = 0
#         time.sleep(1)
#         
# _thread.start_new_thread(funcaoA,())
# conectarWifi()
# _thread.start_new_thread(funcaoB,())
#     
