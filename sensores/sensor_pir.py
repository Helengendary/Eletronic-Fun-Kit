from machine import Pin
import time

pir_sensor = Pin(14, Pin.IN)

buzzer = Pin(12, Pin.OUT)

def read_pir_sensor():
    while True:
        print(pir_sensor.value())
        if pir_sensor.value() == 1  :
            print("Movimento detectado!")
            buzzer.on()
        else:
            print("Nenhum movimeto!")
            buzzer.off()
        time.sleep(1)
        
buzzer.off()
read_pir_sensor()
buzzer.off()