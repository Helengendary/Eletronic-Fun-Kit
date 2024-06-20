import matplotlib.pyplot as plt
import pyodbc

# Conectar com a API
url = "https://iiot-7276b-default-rtdb.firebaseio.com/Helena.json"
proxies = {'https' : "http://disrct:etsps2024401@10.224.200.26:8080"}

server = 'CA-C-00654\SQLEXPRESS'
database = 'helenis'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
cursor = cnxn.cursor()

# Funções para pegar as informações da tabela
def lerTable():
    cursor.execute(f"SELECT * FROM Sensor")
    return cursor.fetchall()

def ler(tipo):
    cursor.execute(f"SELECT {tipo} FROM Sensor")
    return [row[0] for row in cursor.fetchall()]

def apresentar(sinal):
    print(f"Temperatura: {sinal['Temperatura']}")
    print(f"Umidade: {sinal['Umidade']}")


# Print para saber a quantidade de coisas na tabela
data = lerTable()
print(len(data))

dfdfan = ler('Umidade')
gdsgsd = ler('DISTINCT LEFT(CONVERT(VARCHAR, timestamp, 108), 5)')
jjkjkh = ler('Temperatura')

print(dfdfan)
print(gdsgsd)
print(jjkjkh)

#----------------------------------------------
# dfdfan = ler('Umidade')
# gdsgsd = ler('DISTINCT LEFT(CONVERT(VARCHAR, timestamp, 108), 5)')
# humanidade = []
# times = []


# for j in dfdfan:
#     for h in j:
#         humanidade.append(h)

# for i in range(len(gdsgsd)):
#     times.append(gdsgsd[i])

# print(times)
#----------------------------------------------

# Criação do gráfico
def GraficoPontos(x, y, cor, labele, labex):
    plt.scatter(x, y, color=cor, label=labele)
    plt.xlabel(labex)
    plt.ylabel(labele)
    plt.legend()
    plt.grid()
    plt.show()
    plt.close()

GraficoPontos(ler('timestamp'), ler('Umidade'), 'red', 'Umidade', 'Horário')
GraficoPontos(ler('timestamp'), ler('Temperatura'), 'hotpink', 'Temperatura', 'Horário')

width = 0.4
plt.bar(gdsgsd, dfdfan, label='Umidade', align='edge', width=-width)
plt.bar(gdsgsd, jjkjkh, color='red', label='Temperatura', align='edge', width=width)
plt.show()
plt.close()

# help(plt.scatter) # informa os comandos existentes
