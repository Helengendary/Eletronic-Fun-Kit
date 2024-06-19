# from machine import Pin
# import time

# pir_sensor = Pin(2, Pin.IN)

# def sensor():
#     while True:
#         if pir_sensor.value() == 1:
#             print("Movimento detectado!")
#         else:
#             print("Nenhum movimento")
#         time.sleep(1)
        
# sensor()

# ----------------------------------

from machine import Pin, ADC
import time
imort dht

dht_sensor = dht.DHT11(Pin (33))

# Configuração dos pinos do LCD
rs = Pin(14, Pin.OUT)
e = Pin(13, Pin.OUT)
d4 = Pin(12, Pin.OUT)
d5 = Pin(27, Pin.OUT)
d6 = Pin(26, Pin.OUT)
d7 = Pin(25, Pin.OUT)
#led = Pin(2,Pin.OUT)imort dht

dht_sensor = dht.DHT11(Pin (33))

#button= Pin(34, Pin.IN)
sensor = Pin(13,Pin.IN)

def pulse_enable():
    e.on()
    time.sleep_us(1)
    e.off()imort dht

dht_sensor = dht.DHT11(Pin (33))

    time.sleep_us(50)

def send_nibble(data):
    d4.value((data >> 0) & 1)
    d5.value((data >> 1) & 1)
    d6.value((data >> 2) & 1)
    d7.value((data >> 3) & 1)
    pulse_enable()

def send_byte(data, rs_value):
    rs.value(rs_value)
    send_nibble(data >> 4)  # Envia o nibble superior
    send_nibble(data & 0x0F)  # Envia o nibble inferior

def lcd_command(cmd):
    send_byte(cmd, 0)

def lcd_data(data):
    send_byte(data, 1)

def lcd_init():
    time.sleep(0.05)
    rs.off()
    e.off()
    send_nibble(0x03)
    time.sleep_ms(5)
    send_nibble(0x03)
    time.sleep_us(150)
    send_nibble(0x03)
    send_nibble(0x02)
    lcd_command(0x28)  # Função set: 4 bits, 2 linhas, 5x8 pontos
    lcd_command(0x0C)  # Display on, cursor off, blink off
    lcd_command(0x06)  # Entry mode set: incrementa e sem shift
    lcd_command(0x01)  # Limpa o display
    time.sleep_ms(2)

def lcd_puts(text):
    for char in text:
        lcd_data(ord(char))
        
def lcd_clear():
    lcd_command(0x01)
    time.sleep_ms(5)
        
def lcd_second_line(text):
    lcd_command(0xC0)
    lcd_puts(text)
    
def lcd_first_line(text):
    lcd_command(0x80)
    lcd_puts(text)
    
def rigth_left(text,value):
    lcd_command(0xC0)
    for i in range(value):
        lcd_command(0x14)
    time.sleep_ms(5)
    lcd_puts(text)
def first_left(text,value):
    lcd_command(0x80)
    for i in range(value):
        lcd_command(0x14)
    lcd_puts(text)

# Inicia LCD
lcd_init()
while True:
    lcd_clear()
    lcd_puts("  bu ")
    time.sleep(0.5)
    if(button.value()):
        lcd_clear()
        lcd_puts(" vo cmc ")
        while True:
            print(sensor.value())
            if(sensor.value()):
                lcd_clear()
                lcd_puts(" achei")
                time.sleep(2)
                break;
            time.sleep(0.5)
