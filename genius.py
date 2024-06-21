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
           botaoBlue = bB.value()
           botaoRed = bR.value()
           botaoGreen = bG.value()
           botaoYellow = bY.value()
           
           if botaoBlue == True:
               user = 1
               apertado = False
    #        else:
    #            blue.value(0)
           if botaoRed == True:
               user = 2
               apertado = False
    #        else:
    #            red.value(0)
           if botaoGreen == True:
               user = 3
               apertado = False
    #        else:
    #            green.value(0)
           if botaoYellow == True:
               user = 4  
               apertado = False
    #        else:
    #            yellow.value(0)
           time.sleep(0.5)
       if user != atual:
           print("Você perdeu")
           continue

    print(sorteados)
#     azul =  not bB.value()
    time.sleep(3)
