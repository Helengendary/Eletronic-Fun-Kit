from machine import Pin, SoftI2C
import time
import array

# Endereço I2C do MAX30100
I2C_ADDR = 0x57

# Inicializar o I2C usando SoftI2C
i2c = SoftI2C(scl=Pin(22), sda=Pin(23), freq=100000)

# Buffer para armazenar os dados
buffer_size = 100
ir_buffer = array.array('H', [0]*buffer_size)

# Funções para ler e escrever nos registradores do sensor
def read_register(register):
    return i2c.readfrom_mem(I2C_ADDR, register, 1)[0]

def write_register(register, value):
    i2c.writeto_mem(I2C_ADDR, register, bytearray([value]))

def check_sensor():
    try:
        part_id = read_register(0xFF)  # Registrar do ID do sensor
        print("Sensor ID:", part_id)
        return True
    except OSError as e:
        print("Erro ao verificar o sensor:", e)
        return False

def setup():
    # Verificar se o sensor está respondendo
    if not check_sensor():
        print("Sensor não encontrado. Verifique as conexões.")
        return
    
    # Configurar o modo e inicializar o sensor
    write_register(0x06, 0x03)  # Modo SpO2
    write_register(0x07, 0x27)  # Configuração do sensor
    write_register(0x09, 0x00)  # Tolerância de interrupção
    write_register(0x01, 0x03)  # Ativar os LEDs

def read_sensor():
    # Ler dados do sensor
    ir_led = read_register(0x03) << 8 | read_register(0x02)
    return ir_led

def moving_average(data, window_size):
    avg_data = [sum(data[:window_size]) / window_size]
    for i in range(1, len(data) - window_size + 1):
        avg_data.append(sum(data[i:i + window_size]) / window_size)
    return avg_data

def low_pass_filter(data, alpha=0.60):
    filtered_data = [0]*len(data)
    filtered_data[0] = data[0]
    for i in range(1, len(data)):
        filtered_data[i] = alpha * filtered_data[i-1] + (1 - alpha) * data[i]
    return filtered_data

def detect_peaks(data, threshold, min_distance):
    peaks = []
    last_peak = -min_distance
    for i in range(1, len(data) - 1):
        if data[i] > threshold and data[i] > data[i-1] and data[i] > data[i+1]:
            if i - last_peak >= min_distance:
                peaks.append(i)
                last_peak = i
    return peaks

def calculate_bpm(ir_buffer, sample_rate):
    filtered_ir = low_pass_filter(ir_buffer)
    avg_ir = moving_average(filtered_ir, 5)  # Aplicar média móvel com janela de 5
    peak_threshold = max(avg_ir) * 0.6  # Ajuste o limiar de pico
    min_distance = int(1.0 / sample_rate)  # Distância mínima entre picos
    
    peaks = detect_peaks(avg_ir, peak_threshold, min_distance)
    
    if len(peaks) >= 2:
        peak_intervals = [peaks[i] - peaks[i-1] for i in range(1, len(peaks))]
        avg_peak_interval = sum(peak_intervals) / len(peak_intervals)
        bpm = 60 / (avg_peak_interval * sample_rate)
        return bpm
    else:
        return None

# Configurar o sensor
setup()

# Taxa de amostragem (em segundos)
sample_rate = 0.02

# Tamanho da janela de média móvel
window_size = 5
bpm_values = []

while True:
    ir_buffer = []
    for _ in range(buffer_size):
        ir_buffer.append(read_sensor())
#         print(read_sensor())
        time.sleep(sample_rate)
    
    bpm = calculate_bpm(ir_buffer, sample_rate)
    if bpm:
        bpm_values.append(bpm)
        if len(bpm_values) > window_size:
            bpm_values.pop(0)
        avg_bpm = sum(bpm_values) / len(bpm_values)
        print("BPM:", avg_bpm)
    else:
        print("Não foi possível detectar os batimentos")
