import network
import dht
from machine import Pin, Timer
import urequests
import ujson
import utime
import time

# Configura o pino onde o DHT11 está conectado
dht_sensor = dht.DHT11(Pin(34))

amarelo = Pin(16, Pin.OUT)
verde = Pin(4, Pin.OUT)
vermelho = Pin(17, Pin.OUT)

amarelotv = Pin(33, Pin.OUT)
verdetv = Pin(25, Pin.OUT)
vermelhotv = Pin(32, Pin.OUT)

luzvermelho = Pin(13, Pin.IN)
luzverde = Pin(15, Pin.IN)
luzamarelo = Pin(18, Pin.IN)

tvverde = Pin(23, Pin.IN)
tvvermelho = Pin(19, Pin.IN)
tvamarelo = Pin(22, Pin.IN)

#Credenciais do WIFI
# nome = "moto edge 30"
# senha = "HelenaInteligentissima"

#  ---------------------------------------------------------------------------------------- >>>>HELENA ARRUMA UM EMPREGO PFV
#  ---------------------------------------------------------------------------------------- >>>>NÃO TÔ AFIM ASS: HELENA

SECRET_KEY = ""

def conectarWifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando no WiFi...")
        wlan.connect("moto edge 30", "HelenaInteligentissima")
        while not wlan.isconnected():
            pass
    print("Wifi conectado... IP: {}".format(wlan.ifconfig()[0]))
    
conectarWifi()

def enviarFire(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + SECRET_KEY
    }
# Endereço do firebase
    url = "https://iiot-7276b-default-rtdb.firebaseio.com/Helena.json"
    response = urequests.put(url, data=ujson.dumps(data), headers=headers)
    print("Enviado:", response.text)
    response.close()
    
def receberFire():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + SECRET_KEY
    }
    
# Endereço do firebase
    url = "https://iiot-7276b-default-rtdb.firebaseio.com/Helena.json"
    response = urequests.get(url, headers=headers)
    qualquer = ujson.loads(response.text)
    response.close()
    return qualquer

while True:
    fireBase = receberFire()

    temp = dht_sensor.temperature()
    hum = dht_sensor.humidity()
    
    luzLiving = fireBase["livingRoom"]["principalLight"]
    
    tvLiving = fireBase["livingRoom"]["tv"]
    
    luzOffice = fireBase["office"]["principalLight"]
    
    tvOffice = fireBase["office"]["tv"]
    
    luzPrincipal = fireBase["principalRoom"]["principalLight"]
    
    tvPrincipal = fireBase["principalRoom"]["tv"]

    if luzvermelho.value() == 1:
        luzLiving = not luzLiving
        
    if luzverde.value() == 1:
        luzOffice = not luzOffice
        
    if luzamarelo.value() == 1:
        luzPrincipal = not luzPrincipal
        
    if tvverde.value() == 1:
        tvOffice = not tvOffice
        
    if tvvermelho.value() == 1:
        tvLiving = not tvLiving
        
    if tvamarelo.value() == 1:
        tvPrincipal = not tvPrincipal
         
    informacao = {
        
        "livingRoom": {
                "umid": f"{hum}",
                "temp": f"{temp}",
                "tv": tvLiving,
                "principalLight":luzLiving
         },
        "office": {
                "umid": f"{hum}",
                "temp": f"{temp}",
                "tv": tvOffice,
                "principalLight":luzOffice
         },
         "principalRoom": {
                "umid": f"{hum}",
                "temp": f"{temp}",
                "tv": tvPrincipal,
                "principalLight":luzPrincipal
         }
    }
    
    enviarFire(informacao)
    
    if luzPrincipal:
        amarelo.value(1)
    else:
        amarelo.value(0)
  
    if luzOffice:
        verde.value(1)
    else:
        verde.value(0)
        
    if luzLiving:
        vermelho.value(1)
    else:
        vermelho.value(0)
    
    # tvs
    if tvPrincipal:
        amarelotv.value(1)
    else:
        amarelotv.value(0)
  
    if tvOffice:
        verdetv.value(1)
    else:
        verdetv.value(0)
        
    if tvLiving:
        vermelhotv.value(1)
    else:
        vermelhotv.value(0)