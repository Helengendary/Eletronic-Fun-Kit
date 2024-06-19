from machine import ADC, Pin
import time

# Configura o pino ADC onde o potenciômetro está conectado
adc = ADC(Pin(34))
adc.width(ADC.WIDTH_12BIT)  # Configura a resolução do ADC para 12 bits (0-4095)
adc.atten(ADC.ATTN_11DB)    # Configura a atenuação para o range de 0-3.6V

# Função principal para ler o potenciômetro
def read_potentiometer():
    while True:
        # Lê o valor do ADC (potenciômetro)
        pot_value = round(adc.read()*15/4095)
        print("Valor do potenciômetro:", pot_value)
        
        # Aguarda um segundo antes de ler novamente
        time.sleep(1)

# Chama a função principal
read_potentiometer()
