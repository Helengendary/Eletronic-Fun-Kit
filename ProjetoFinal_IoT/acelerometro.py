from machine import Pin, I2C, sleep, ADC
import dht
import machine
from time import sleep
import time
import network
import dht
import ujson
import utime
import mpu6050 as mpu

diaSemana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

atual = utime.localtime()
ano = atual[0]
mes = meses[atual[1]-1]
dia = atual[2]
hora = atual[3]
min = atual[4]
weekday = diaSemana[atual[6]]

if hora < 10:
    hora = str(hora)
    hora = '0' + hora
    
if min < 10:
    min = str(min)
    min = '0' + min

Data = f"{weekday}, {dia} de {mes}"
HoraAtual = f"{hora}:{min}"

dht = dht.DHT11(Pin(32))

i2c = I2C (scl =Pin(22), sda = Pin(21))
mpu = mpu.accel(i2c)

passo = 0
xPeak = 20
xVale = -20
count = 0    
    
while True:
    temps = (mpu.get_values())

    x = round(temps["AcX"] * 2 / 1000,2) 
    y = round(temps["AcY"] * 2 / 1000,2) 
    z = round(temps["AcZ"] * 2 / 1000,2) 
    
    print('x: ', x)
    print('y: ', y)
    print('z: ', z)

    if z < 10 and z > -10:
        if x > xPeak or x < xVale:
            if count != 1:
                passo+=1
                count = 1
        else:
            count = 0
    

    xPast = x
    print('passo ',passo)
    sleep(0.05)