from machine import Pin
import dht
from time import sleep_ms
import lcd1602

# Configuração do pino do sensor DHT11
dht_pin = 35

# Inicialização do sensor DHT11
dht_sensor = dht.DHT11(Pin(dht_pin, Pin.IN))

# Inicialização do LCD1602
lcd = LCD1602(rs=12, en=14, d4=14, d5=27, d6=26, d7=25)

def setup():
    dht_sensor.measure()
    lcd.putstr("DHT11\nHumidity/Temp.")

def loop():
    sleep_ms(2000)  # Aguarda dois segundos entre as medidas
    H = dht_sensor.humidity()  # Lê a umidade
    T = dht_sensor.temperature()  # Lê a temperatura em Celsius

    # Verifica se alguma leitura falhou
    if H is None or T is None:
        lcd.clear()
        lcd.putstr("Failed to read from DHT sensor!")
        return

    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Humidity: {}%".format(H))
    lcd.move_to(0, 1)
    lcd.putstr("Temp.: {}C".format(T))

while True:
    setup()
    loop()
