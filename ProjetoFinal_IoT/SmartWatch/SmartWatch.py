import urequests
import ujson
import network
import time

diaSemana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

atual = utime.localtime()
ano = atual[0]
mes = meses[atual[1]-1]
dia = atual[2]
hora = atual[3]
min = atual[4]
weekday = diaSemana[atual[6]]

if hora < 10:
    hora = str(hora)
    hora = '0' + hora
    
if min < 10:
    min = str(min)
    min = '0' + min

horario = f"{hora}:{min}"

dht = dht.DHT11(Pin(32))

#Credenciais do WIFI
nome = "moto edge 30"
senha = "HelenaInteligentissima"

# Endereço do firebase
FIREBASE_URL = "https://iiot-7276b-default-rtdb.firebaseio.com/"
SECRET_KEY = ""

def conectarWifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando no WiFi...")
        wlan.connect(nome, senha)
        while not wlan.isconnected():
            pass
    print("Wifi conectado... IP: {}".format(wlan.ifconfig()[0]))

def enviarFire(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + SECRET_KEY
    }
    url = FIREBASE_URL + "/Mariana.json"

    response = urequests.put(url, data=ujson.dumps(data), headers=headers)
    print("Firebase Response:", response.text)
    response.close()

conectarWifi()



def main():
    while True:
        dht.measure() 
        temperatura = dht.temperature()
        umidade = dht.humidity()
        passos = 2067
        batimentos = 90
        oxigenio = 92
        
        informacao = {
            "Temperatura": f"{temperatura}",
            "Umidade": f"{umidade}",
            "Passos": f"{passos}",
            "Batimentos": f"{batimentos}",
            "Oxigenio": f"{oxigenio}",
            "Horario": horario,
            "Semana": weekday,
            "Dia": f"{dia}",
            "Mes": mes
        }

        enviarFire(informacao)
        
        time.sleep(1)

main()

    



