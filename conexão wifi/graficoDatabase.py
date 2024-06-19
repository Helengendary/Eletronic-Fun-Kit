import matplotlib.pyplot as plt
import requests
import json
import pyodbc

url = "https://iiot-7276b-default-rtdb.firebaseio.com/Helena.json"
proxies = {'https' : "http://disrct:etsps2024401@10.224.200.26:8080"}

server = 'CA-C-00654\SQLEXPRESS'
database = 'helenis'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
cursor = cnxn.cursor()

def lerTable():
    cursor.execute(f"SELECT * FROM Sensor")
    return cursor.fetchall()

def ler(tipo):
    cursor.execute(f"SELECT {tipo} FROM Sensor")
    return cursor.fetchall()

def apresentar(sinal):
    print(f"Temperatura: {sinal['Temperatura']}")
    print(f"Umidade: {sinal['Umidade']}")

data = lerTable()

print(len(data))

plt.scatter(ler('Umidade'), ler('Temperatura'))
plt.show()

plt.scatter(ler('timestamp'), ler('Temperatura'))
plt.show()

# help(plt.bar) # informa os comandos existentes