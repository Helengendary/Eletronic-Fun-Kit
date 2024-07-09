from machine import Pin, I2C, sleep, ADC
import dht
import machine
from time import sleep
import time
import network
import dht
import ujson
import urequests
import utime
import mpu6050 as mpu
import _thread
 
#-----------------------------------------------------------------------------------------

diaSemana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

i2c = I2C (scl =Pin(22), sda = Pin(21))
mpu = mpu.accel(i2c)

passo = 0
xPeak = 20
xVale = -20
count = 0
conta = 0

dht = dht.DHT11(Pin(32))

#-----------------------WIFI-----------------------------------------
nome = 'moto edge 30'
senha = 'HelenaInteligentissima'
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
        "Authorization": "Bearer "
    }
    url = "https://iiot-7276b-default-rtdb.firebaseio.com//Mariana.json"
    response = urequests.put(url, data=ujson.dumps(data), headers=headers)
    print("Firebase Response:", response.text)
    response.close()
    
conectarWifi()
#------------------------------------------------------------------
informacao = {
            "Temperatura": 0,
            "Umidade": 0,
            "Passos": 0,
            "Batimentos": 0,
            "Oxigenio": 0,
            "Horario": 0,
            "Semana": 0,
            "Dia": 0,
            "Mes": 0
        }
    
def sensores():
    conta = 0
    dht.measure()
    temperatura = dht.temperature()
    umidade = dht.humidity()
    passo = 0
    while True:
        temps = (mpu.get_values())
        
        x = round(temps["AcX"] * 2 / 500,2) 
        y = round(temps["AcY"] * 2 / 500,2) 
        z = round(temps["AcZ"] * 2 / 500,2) 
        
        print('x: ', x)
        print('y: ', y)
        print('z: ', z)

        if z < 120 and z > -120:
            if x > xPeak or x < xVale:
                if count != 1:
                    passo+=1
                    count = 1
            else:
                count = 0
        
        atual = utime.localtime()
        ano = atual[0]
        mes = meses[atual[1]-1]
        dia = atual[2]
        hora = atual[3]
        min = atual[4]
        weekday = diaSemana[atual[6]]
        
    #     if horario == "00:00":
    #         passo = 0
    #         
        if hora < 10:
            hora = str(hora)
            hora = '0' + hora
            
        if min < 10:
            min = str(min)
            min = '0' + min

        horario = f"{hora}:{min}"
        
        if conta == 20:
            dht.measure() 
            temperatura = dht.temperature()
            umidade = dht.humidity()

        batimentos = 18
        oxigenio = 90
        
        informacao["Temperatura"] = temperatura
        informacao["Umidade"] = umidade
        informacao["Passos"] = passo
        informacao["Batimentos"] = batimentos
        informacao["Oxigenio"] = oxigenio
        informacao["Horario"] = horario
        informacao["Semana"] = weekday
        informacao["Dia"] = dia
        informacao["Mes"] = mes
        
        if conta == 20:
            conta = 0
        
        conta+=1
        time.sleep(0.05)

_thread.start_new_thread(sensores, ())
while True:
    enviarFire(informacao)

    




