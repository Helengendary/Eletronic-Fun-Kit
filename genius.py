import machine
import time
import random

acerto = True
jogadas = 0
sorteados = []

red = machine.Pin(15, machine.Pin.OUT)
blue = machine.Pin(27, machine.Pin.OUT)
green = machine.Pin(18, machine.Pin.OUT)
yellow = machine.Pin(23, machine.Pin.OUT)

bY = machine.Pin(25, machine.Pin.IN)
bG = machine.Pin(32, machine.Pin.IN)
bR = machine.Pin(33, machine.Pin.IN)
bB = machine.Pin(26, machine.Pin.IN)

while acerto:
    jogadas += 1
    new = random.randint(1, 4)
    sorteados.append(new)
    
    print("Vez da máquina!\n")
    for i in range(len(sorteados)):
        atual = sorteados[i]
       
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
    
    print("Sua vez!")
    for i in range(len(sorteados)):
        atual = sorteados[i]
        apertado = True
       
        while apertado:

            botaoBlue = not not bB.value()
            botaoRed = not not bR.value()
            botaoGreen = not not bG.value()
            botaoYellow = not not bY.value()

            if botaoBlue == True:
                user = 1
                apertado = False
                print("Azul apertado")
            if botaoRed == True:
                user = 2
                print("Vermelho apertado")
                apertado = False
            if botaoGreen == True:
                user = 3
                apertado = False
                print("Verde apertado")
            if botaoYellow == True:
                user = 4  
                apertado = False
                print("Amarelo apertado")
            time.sleep(0.1)


        if user != atual:
            print("\nVocê perdeu")

            print('Sequência: ', end='')

            for l in range(len(sorteados)):
                current = sorteados[l]

                if current == 1:
                    print("Azul", end='')
                elif current == 2:
                    print("Vermelho", end='')
                elif current == 3:
                    print("Verde", end='')
                elif current == 4:
                    print("Amarelo", end='')

                if l == (len(sorteados))-1:
                    print(".\n")
                    continue
                else:
                    print(", ", end='')
                

            acerto = False
            break;
        
    if acerto == True:
        print("\n" * 10)
    time.sleep(2)
