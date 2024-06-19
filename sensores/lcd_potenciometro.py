from machine import ADC, Pin
import machine
import time

# Configura o pino ADC onde o potenciômetro está conectado
adc = ADC(Pin(34))
adc.width(ADC.WIDTH_12BIT)  # Configura a resolução do ADC para 12 bits (0-4095)
adc.atten(ADC.ATTN_11DB)    # Configura a atenuação para o range de 0-3.6V

# Configuração dos pinos do LCD
rs = Pin(14, Pin.OUT)
e = Pin(12, Pin.OUT)
d4 = Pin(27, Pin.OUT)
d5 = Pin(26, Pin.OUT)
d6 = Pin(25, Pin.OUT)
d7 = Pin(33, Pin.OUT)

def pulse_enable():
    e.on()
    time.sleep_us(1)
    e.off()
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

def secondLine():
    lcd_command(0x80 | 0x40)
    
def firstLine():
    lcd_command(0x0C)
    
def change(value):
    lcd_command(128+value)
    
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
        
        
def write_char(self, char):
    self._send_byte(ord(char), True)

def set_cursor(self, col, row):
    row_offsets = [0x00, 0x40, 0x14, 0x54]
    self._send_byte(0x80 | (col + row_offsets[row]))

# Inicializa o LCD
lcd_init()


# Chama a função principal
while True:
#     set_cursor(0,2)
#     write_char('O')
    lcd_command(0x01)
    time.sleep(0.1)
    
    pot_value = round(adc.read()*15/4095)
    print("Valor do potenciômetro:", pot_value)
    
    change(pot_value)
    lcd_puts("j")

    time.sleep(1)

