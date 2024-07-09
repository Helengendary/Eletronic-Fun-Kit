import machine
import time

# Definindo o endereço I2C do sensor MAX30100
MAX30100_I2C_ADDRESS = 0x57

# Registradores do MAX30100
REG_MODE_CONFIG = 0x06
REG_SPO2_CONFIG = 0x07
REG_LED_CONFIG = 0x09
REG_FIFO_WR_PTR = 0x04
REG_FIFO_RD_PTR = 0x06
REG_FIFO_DATA = 0x07

# Configurações de limite
MIN_HEART_RATE = 40
MAX_HEART_RATE = 180

# Inicializando o I2C
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(25))

def write_register(register, value):
    i2c.writeto_mem(MAX30100_I2C_ADDRESS, register, bytes([value]))

def read_register(register, length):
    return i2c.readfrom_mem(MAX30100_I2C_ADDRESS, register, length)

def get_heart_rate(ir, red):
    # Aqui você pode implementar a lógica para calcular a frequência cardíaca
    # Baseado nos valores IR e Red do sensor MAX30100
    return 60  # Exemplo simples, substitua pela lógica real

# Configurando o sensor MAX30100
write_register(REG_MODE_CONFIG, 0x03)  # Modo SpO2 e frequência cardíaca
write_register(REG_SPO2_CONFIG, 0x27)  # 1600us, 50Hz
write_register(REG_LED_CONFIG, 0x1F)   # Corrente LED vermelho e infravermelho em 50mA

# Loop para ler os dados do sensor
while True:
    # Ler dados da FIFO
    fifo_data = read_register(REG_FIFO_DATA, 4)
    
    # Processar os dados lidos
    ir = (fifo_data[0] << 8) | fifo_data[1]
    red = (fifo_data[2] << 8) | fifo_data[3]

    # Calcular a frequência cardíaca (substitua pelo método adequado)
    heart_rate = get_heart_rate(ir, red)

    # Aplicar limites à frequência cardíaca
    if heart_rate < MIN_HEART_RATE:
        heart_rate = MIN_HEART_RATE
    elif heart_rate > MAX_HEART_RATE:
        heart_rate = MAX_HEART_RATE

    print("Frequência Cardíaca:", heart_rate)

    # Atraso para evitar leituras muito rápidas
    time.sleep(1)
