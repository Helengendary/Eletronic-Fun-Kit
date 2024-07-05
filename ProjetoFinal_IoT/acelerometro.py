from machine import Pin, I2C, sleep, ADC
import dht
import machine
from time import sleep
import time
import network
import dht
import ujson
import utime

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
        return vals


i2c = I2C (scl =Pin(23), sda = Pin(22))
mpu = accel(i2c)

passo = 0
xPeak = 15
xVale = -5
xPast = 0
picado = False
valuedado = False
count = 0    
    
while True:
    temps = (mpu.get_values())

    x = round(temps["AcX"] * 2 / 500,2) 
    y = round(temps["AcY"] * 2 / 500,2) 
    z = round(temps["AcZ"] * 2 / 500,2) 
    
    print('x: ', x)
    print('y: ', y)
    print('z: ', z)
    
    
    if xPast > xPeak:
        
        if x < xVale:
            passo+=1
    
    xPast = x
#     print("entrou if")
#     if z < 120 and z > -120:
#         print('z')

    print('passo ',passo)
    time.sleep(0.2)