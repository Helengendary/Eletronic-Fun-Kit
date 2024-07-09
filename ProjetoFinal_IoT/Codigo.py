from time import sleep
import time
from machine import Timer, Pin
import network
import urequests
import ujson

class LcdHd44780:
    def __init__(self, rs, e, d):
        """Constructor. Set control and data pins of HD44780-based
        LCD and call the initialization sequence."""
        # Create machine.Pin objects within the constructor
        self.RS = Pin(rs, Pin.OUT)
        self.E = Pin(e, Pin.OUT)
        self.D = [Pin(pin_number, Pin.OUT) for pin_number in d]
        # Send initialization sequence
        self._init()

    def _init(self):
        """Initialization sequence of HD44780"""
        self.RS.off()
        time.sleep_ms(20)
        self._write_nibble(0x30)
        time.sleep_ms(5)
        self._write_nibble(0x30)
        time.sleep_ms(1)
        self._write_nibble(0x30)
        time.sleep_ms(1)
        self._write_nibble(0x20)
        time.sleep_ms(1)
        self.command(0x28)  # 4-bit, 2 lines, 5x7 pixels
        self.command(0x06)  # Increment, no shift
        self.command(0x01)  # Clear display
        # self.command(0x0f)  # Display on, cursor on and blinking
        self.command(0x0e)  # Display on, cursor on but not blinking
        self.command(0x0c)  # Display on, cursor off

    def _set_data_bits(self, val):
        """Set four data pins according to the parameter val"""
        for i in range(4):
            # For each pin, set the value according to the corresponding bit
            self.D[i].value(val & (1 << (i + 4)))

    def _write_nibble(self, val):
        """Write upper nibbble of the value byte"""
        self._set_data_bits(val)
        self.E.on()
        time.sleep_us(1)
        self.E.off()

    def _write_byte(self, val):
        """Write a byte of value to the LCD controller"""
        self._write_nibble(val)  # Write upper nibble
        self._write_nibble(val << 4)  # Write lower nibble

    def command(self, cmd):
        """Write a command to the LCD controller"""
        # RS pin = 0, write to command register
        self.RS.off()
        # Write the command
        self._write_byte(cmd)
        time.sleep_ms(2)

    def data(self, val):
        """Write data to the LCD controller"""
        # RS pin = 1, write to data register
        self.RS.on()
        # Write the data
        self._write_byte(val)

    def write(self, s):
        """Display a character string on the LCD"""
        for c in s:
            self.data(ord(c))

    def move_to(self, line, column):
        """Move cursor to a specified location of the display"""
        if line == 1:
            cmd = 0x80
        elif line == 2:
            cmd = 0xc0
        else:
            return

        if column < 1 or column > 20:
            return

        cmd += column - 1
        self.command(cmd)

    def custom_char(self, addr, charmap):
        """Write a character to one of the 8 CGRAM locations, available
        as chr(0) through chr(7).
        https://peppe8o.com/download/micropython/LCD/lcd_api.py
        https://microcontrollerslab.com/i2c-lcd-esp32-esp8266-micropython-tutorial/
        """
        addr = addr & 0x07
        self.command(0x40 | (addr << 3))  # Set CG RAM address
        time.sleep_us(40)
        for i in range(8):
            self.data(charmap[i])
            time.sleep_us(40)
        self.command(0x80)  # Move to origin of DD RAM address
        
def clear():
    lcd.command(0x01)
    
nome = 'Wifi Amilton'
senha = '87654321'
def conectarWifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando no WiFi...")
        wlan.connect(nome, senha)
        while not wlan.isconnected():
            pass
    print("Wifi conectado... IP: {}".format(wlan.ifconfig()[0]))

conectarWifi()
    
def receberFire():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "
    }

    url = "https://iiot-7276b-default-rtdb.firebaseio.com/Mariana.json"
    response = urequests.get(url, headers=headers)
    qualquer = ujson.loads(response.text)
    print("Resposta: ", response.text)
    response.close()
    return qualquer

button = Pin(5,  Pin.IN)
pacoca = True 

lcd = LcdHd44780(rs=14,e=13,d=[12,27,26,25])

# tim = Timer(0)
# tim.init(period=1000,mode=Timer.PERIODIC,callback=timer_call)
while True:
    fire = receberFire()
    passo = fire["Passos"]
    dia = fire["Dia"]
    mes = fire["Mes"]
    graus = fire["Temperatura"]
    batimento = fire["Batimentos"]
    ox = fire["Oxigenio"]
    horario = fire["Horario"]

    botaun = not button.value()
    
    if botaun:
        pacoca = not pacoca
        clear()
        
    if pacoca:
        lcd.move_to(1,1)
        lcd.write(f"{dia}, {mes}    {graus}C")
        lcd.move_to(2,1)
        lcd.write(f"Passos: {passo}")

    else:
        time.sleep(1)
        lcd.move_to(1,1)
        lcd.write(f"{batimento}bpm")
        lcd.move_to(2,1)
        lcd.write(f"Sp02: {ox}%")

    time.sleep(0.5)
