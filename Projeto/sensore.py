from machine import Pin, I2C, sleep
import dht
import machine
from time import sleep
import time
import network
import dht
import ujson
import utime

atual = utime.localtime()
print(atual.year)

dht = dht.DHT11(Pin(32))

class accel():
    def __init__(self, i2c, addr=0x68):
        self.iic = i2c
        self.addr = addr
        self.iic.start()
        self.iic.writeto(self.addr, bytearray([107, 0]))
        self.iic.stop()

    def get_raw_values(self):
        self.iic.start()
        a = self.iic.readfrom_mem(self.addr, 0x3B, 14)
        self.iic.stop()
        return a

    def get_ints(self):
        b = self.get_raw_values()
        c = []
        for i in b:
            c.append(i)
        return c

    def bytes_toint(self, firstbyte, secondbyte):
        if not firstbyte & 0x80:
            return firstbyte << 8 | secondbyte
        return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255) + 1)

    def get_values(self):
        raw_ints = self.get_raw_values()
        vals = {}
        vals["AcX"] = self.bytes_toint(raw_ints[0], raw_ints[1])
        vals["AcY"] = self.bytes_toint(raw_ints[2], raw_ints[3])
        vals["AcZ"] = self.bytes_toint(raw_ints[4], raw_ints[5])
        vals["Tmp"] = self.bytes_toint(raw_ints[6], raw_ints[7]) / 340.00 + 36.53
        return vals  # returned in range of Int16
        # -32768 to 32767

# nome = "moto edge 30"
# senha = "HelenaInteligentissima"

# SECRET_KEY = ""

# def conectarWifi():
#     wlan = network.WLAN(network.STA_IF)
#     wlan.active(True)
#     if not wlan.isconnected():
#         print("Conectando no WiFi...")
#         wlan.connect(nome, senha)
#         while not wlan.isconnected():
#             pass
#     print("Wifi conectado... IP: {}".format(wlan.ifconfig()[0]))

# def enviarFire(data):
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer " + SECRET_KEY
#     }
# # Endereço do firebase
#     url = "https://iiot-7276b-default-rtdb.firebaseio.com/smartwatch.json"

#     response = urequests.put(url, data=ujson.dumps(data), headers=headers)
#     print("Firebase Response:", response.text)
#     response.close()

# conectarWifi()
######################################

i2c = I2C (scl =Pin(23), sda = Pin(22))
mpu = accel(i2c)

prev_Acelerometro = []

while True:
    temps = (mpu.get_values())

    dht.measure() 
    temperatura = dht.temperature()
    umidade = dht.humidity()

    xAcelerometro = round(temps["AcX"] * 2 / 32767,2) 
    yAcelerometro = round(temps["AcY"] * 2 / 32767,2) 
    zAcelerometro = round(temps["AcZ"] * 2 / 32767,2) 

    if [xAcelerometro, yAcelerometro, zAcelerometro] != prev_Acelerometro:
        print("Acelerometro")
        message = ujson.dumps({
            "xAcelerometro": xAcelerometro,
            "yAcelerometro": yAcelerometro,
            "zAcelerometro": zAcelerometro,
        })
        
        print(message)
        print(f"Temperatura: {temperatura}")
        print(f"Umidade: {umidade}")
        # enviarFire(message)
        prev_Acelerometro = [xAcelerometro, yAcelerometro, zAcelerometro]

    sleep(1)
