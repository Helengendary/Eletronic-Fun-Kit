import dht
from machine import Pin
import time
import urequests
import ujson
import network

# Configura o pino onde o DHT11 está conectado
dht_sensor = dht.DHT11(Pin(34))

amarelo = Pin(26, Pin.OUT)
verde = Pin(25, Pin.OUT)
ledAmarelo = Pin(27, Pin.OUT)

#Credenciais do WIFI
nome = "moto edge 30"
senha = "HelenaInteligentissima"

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
# Endereço do firebase
    url = "https://iiot-7276b-default-rtdb.firebaseio.com/Helena.json"

    response = urequests.put(url, data=ujson.dumps(data), headers=headers)
    print("Firebase Response:", response.text)
    response.close()

conectarWifi()

while True:
    
    amarelo.value(not amarelo.value())
    temp = dht_sensor.temperature()
    hum = dht_sensor.humidity()
    print("Temperatura: {}°C  Umidade: {}%".format(temp, hum))
    informacao = {
        
        "livingRoom": {
                "umid": f"{hum}",
                "temp": f"{temp}",
                "tv": "OFF",
                "principalLight":false
         },
        "office": {
                "umid": f"{hum}",
                "temp": f"{temp}",
                "tv": "OFF",
                "principalLight":false
         },
         "principalRoom": {
                "umid": f"{hum}",
                "temp": f"{temp}",
                "tv": "OFF",
                "principalLight":false
         }
    }
#     
    enviarFire(informacao)
    time.sleep(1)