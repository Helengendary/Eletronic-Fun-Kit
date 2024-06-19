import dht
from machine import Pin
import time
import urequests
import ujson
import network

# Configura o pino onde o DHT11 está conectado
dht_sensor = dht.DHT11(Pin(32))

#Credenciais do WIFI
nome = "Vivo-Internet-BF17"
senha = "78814222"

# Endereço do firebase
FIREBASE_URL = "https://iiot-7276b-default-rtdb.firebaseio.com/"
SECRET_KEY = ""

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
    url = FIREBASE_URL + "/Helena.json"  # Coloque o seu nome

    response = urequests.put(url, data=ujson.dumps(data), headers=headers)
    print("Firebase Response:", response.text)
    response.close()

conectarWifi()

while True:
    
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    hum = dht_sensor.humidity()
    
    informacao = {
        "Temperatura": f"{temp}",
        "Umidade": f"{hum}"
    }
    
    enviarFire(informacao)
    time.sleep(1)