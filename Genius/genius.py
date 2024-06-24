import machine
import time
import random

acerto = True
jogadas = 0
sorteados = []


red = machine.Pin(15, machine.Pin.OUT)
blue = machine.Pin(13, machine.Pin.OUT)
green = machine.Pin(18, machine.Pin.OUT)
yellow = machine.Pin(23, machine.Pin.OUT)

bY = machine.Pin(25, machine.Pin.IN)
bG = machine.Pin(32, machine.Pin.IN)
bR = machine.Pin(35, machine.Pin.IN)
bB = machine.Pin(34, machine.Pin.IN)

while acerto:
    jogadas += 1
    new = random.randint(1, 4)
    sorteados.append(new)
    
    for i in range(len(sorteados)):
       atual = sorteados[i]
       print(atual)
       
       if atual == 1:
           blue.value(1)
           time.sleep(1)
           blue.value(0)
           time.sleep(0.5)
       else:
           blue.value(0)
       if atual == 2:
           red.value(1)
           time.sleep(1)
           red.value(0)
           time.sleep(0.5)
       else:
           red.value(0)
       if atual == 3:
           green.value(1)
           time.sleep(1)
           green.value(0)
           time.sleep(0.5)
       else:
           green.value(0)
       if atual == 4:
           yellow.value(1)
           time.sleep(1)
           yellow.value(0)
           time.sleep(0.5)
       else:
           yellow.value(0)
    
    for i in range(len(sorteados)):
       atual = sorteados[i]
       apertado = True
       
       while apertado:
           botaoBlue = not not bB.value()
           botaoRed = not not bR.value()
           botaoGreen = not not bG.value()
           botaoYellow = not not bY.value()
           
           if botaoBlue == True:
               blue.value(1)
               time.sleep(0.5)
               blue.value(0)
               user = 1
               apertado = False
           if botaoRed == True:
               red.value(1)
               time.sleep(0.5)
               red.value(0)
               user = 2
               apertado = False
           if botaoGreen == True:
               green.value(1)
               time.sleep(0.5)
               green.value(0)
               user = 3
               apertado = False
           if botaoYellow == True:
               yellow.value(1)
               time.sleep(0.5)
               yellow.value(0)
               user = 4  
               apertado = False
           time.sleep(0.5)
           
       if user != atual:        
           blue.value(1)
           yellow.value(1)
           green.value(1)
           red.value(1)
           time.sleep(0.5)
           blue.value(0)
           yellow.value(0)
           green.value(0)
           red.value(0)
           time.sleep(0.5)
           
           blue.value(1)
           yellow.value(1)
           green.value(1)
           red.value(1)
           time.sleep(0.5)
           blue.value(0)
           yellow.value(0)
           green.value(0)
           red.value(0)
           
           print("Você perdeu")
           acerto = False
    
    time.sleep(2)
    
print(sorteados)
