import time
import pyodbc
import json
import requests

url = "https://iiot-7276b-default-rtdb.firebaseio.com/Helena.json"
proxies = {'https' : "http://disrct:etsps2024401@10.224.200.26:8080"}

def InserirBD(sinal):
    server = 'CA-C-00654\SQLEXPRESS'
    database = 'helenis'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    cursor = cnxn.cursor()
    cursor.execute(f"INSERT Sensor (Temperatura, Umidade) VALUES ({sinal['Temperatura']},{sinal['Umidade']})")
    cursor.commit()
    print("Inserido com sucesso!")

def apresentar(sinal):
    print(f"Temperatura: {sinal['Temperatura']}")
    print(f"Umidade: {sinal['Umidade']}")
    
while True:
    resposta = json.loads(requests.get(url, proxies=proxies).content)
    apresentar(resposta)
    InserirBD(resposta)
    time.sleep(120)