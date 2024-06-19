import machine
import time

# led = machine.Pin(33, machine.Pin.OUT)
# 
# while True:
#     led.value(not led.value())
#     time.sleep(1)
    
    
button = machine.Pin(14, machine.Pin.IN)

led = machine.Pin(33, machine.Pin.OUT)

while True:
    
    button_state = not(button.value())
    print("Estado do botão: ", button_state)
    
    if button_state == True:
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.1)        