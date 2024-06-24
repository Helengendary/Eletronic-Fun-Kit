import pyodbc
import json
import requests

url = "https://iiot-7276b-default-rtdb.firebaseio.com/Helena.json"
proxies = {'https' : "http://disrct:etsps2024401@10.224.200.26:8080"}

server = 'CA-C-00654\SQLEXPRESS'
database = 'helenis'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
cursor = cnxn.cursor()

def InserirBD(sinal):
    nome = sinal['jogador@']
    record = int(sinal['score'])
    cursor.execute(f"INSERT INTO Genius(jogador@, score) VALUES ('{nome}',{record})")
    cursor.commit()
    print("Inserido com sucesso!")

def TheBest():
    cursor.execute(f"SELECT * FROM Genius ORDER BY score DESC")
    return cursor.fetchall()

resposta = json.loads(requests.get(url, proxies=proxies).content)

InserirBD(resposta)
BestScore = TheBest()
print(f"Melhor Score: {BestScore[0]}")
