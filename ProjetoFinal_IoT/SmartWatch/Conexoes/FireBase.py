import pyodbc
import time
import requests
import json

proxies = {'https': "http://disrct:etsps2024401@10.224.200.26:8080"}

url = 'https://iiot-7276b-default-rtdb.firebaseio.com/Mariana.json'

def InserirBD(sinal):
    server = 'CA-C-00657\SQLEXPRESS'
    database = 'SmartWatch'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    cursor = cnxn.cursor()
    cursor.execute(f"INSERT smartwatch (Temperatura, Umidade, Passos, Batimentos, Oxigenio, Horario, Semana, Dia, Mes) VALUES ({sinal[0]},{sinal[1]},{sinal[2]},{sinal[3]},{sinal[4]},'{sinal[5]}','{sinal[6]}',{sinal[7]},'{sinal[8]}')")
    cursor.commit()
    print("Inserido com sucesso!")

def apresentar(sinal):
    print(f"Temperatura: {sinal[0]}")
    print(f"Umidade: {sinal[1]}")
    print(f"Passos: {sinal[2]}")
    print(f"Batimentos: {sinal[3]}")
    print(f"Oxigenio: {sinal[4]}")
    print(f"Horario: {sinal[5]}")
    print(f"Semana: {sinal[6]}")
    print(f"Dia: {sinal[7]}")
    print(f"Mes: {sinal[8]}")

while True:
    meuJson = requests.get(url, proxies=proxies).content
    
    temperatura = json.loads(meuJson)['Temperatura']
    umidade = json.loads(meuJson)['Umidade']
    passos = json.loads(meuJson)['Passos']
    batimentos = json.loads(meuJson)['Batimentos']
    oxigenio = json.loads(meuJson)['Oxigenio']
    horario = json.loads(meuJson)['Horario']
    semana = json.loads(meuJson)['Semana']
    dia = json.loads(meuJson)['Dia']
    mes = json.loads(meuJson)['Mes']

    valores = (temperatura, umidade, passos, batimentos, oxigenio, horario, semana, dia, mes)
    apresentar(valores)
    InserirBD(valores)

    time.sleep(1)