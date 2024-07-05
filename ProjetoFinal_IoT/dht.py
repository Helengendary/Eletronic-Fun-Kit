import dht
import time
from machine import Pin

sensor = dht.DHT22(Pin(32))

while True:
    sensor.measure() 
    temperatura = sensor.temperature()
    print(temperatura)
    time.sleep(1)