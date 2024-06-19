import requests
import json

proxies = {'https' : "http://disrct:etsps2024401@10.224.200.26:8080"}

print()
nomeUser = input("First or full name > ")

url = f'https://api.agify.io/?name={nomeUser}'

resposta = requests.get(url, proxies=proxies).content

idade = json.loads(resposta)["age"]

print()
print(f'{nomeUser} is {idade} years old')