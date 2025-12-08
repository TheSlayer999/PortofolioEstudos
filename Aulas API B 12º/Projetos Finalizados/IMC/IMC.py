from os import system
import matplotlib.pyplot as plt

system("cls")
print("--- Cálculo do IMC ---")
dados=[{"Nome": "David", "Altura": 1.80, "Peso": 62},
        {"Nome": "Ana", "Altura": 1.65, "Peso": 48.0},
        {"Nome": "João", "Altura": 1.75, "Peso": 55.0},
        {"Nome": "Verónica", "Altura": 1.68, "Peso": 65.0},
        {"Nome": "Rui", "Altura": 1.70, "Peso": 68.5}, 
        {"Nome": "Marta", "Altura": 1.58, "Peso": 59.0},
        {"Nome": "Luís", "Altura": 1.85, "Peso": 80.0},
        {"Nome": "Vanessa", "Altura": 1.72, "Peso": 64.0},
        {"Nome": "Pedro", "Altura": 1.79, "Peso": 75.0},
        {"Nome": "Tiago", "Altura": 1.74, "Peso": 80.0}
        ]

tamanho=len(dados)
abaixo=0
ideal=0
acima=0

nomes = []
valores_imc = []
cores_barras = []

for i in range (tamanho):
    
    imc=dados[i]["Peso"]/(dados[i]["Altura"]*dados[i]["Altura"])
    dados[i]["imc_dados"]=imc

    if dados[i]["imc_dados"]<18.5:
        classificacao="Abaixo do peso"
        cores_barras.append('blue')
    elif dados[i]["imc_dados"]>=18.5 and dados[i]["imc_dados"]<25:
        classificacao="Peso ideal"
        cores_barras.append('green')
    elif dados[i]["imc_dados"]>=25:
        classificacao="Acima do peso"
        cores_barras.append('red')
    dados[i]["imc_classificacao"]=classificacao
    if classificacao=="Abaixo do peso":
                abaixo+=1
    elif classificacao=="Peso ideal":
                ideal+=1
    elif classificacao=="Acima do peso":
                acima+=1

    nomes.append(dados[i]["Nome"])
    valores_imc.append(imc)
    print(f"O IMC de {[dados[i]["Nome"]]} é: {imc:.2f}. Esta pessoa pertence a classificação: {classificacao}")
print(f"Há {abaixo} abaixo do peso, {ideal} no peso ideal e {acima} acima do peso.")

gráfico=input("Pretende ver um gráfico? (s/n): ")
if gráfico.lower()=="s":
        plt.title('Distribuição de IMC por Pessoa')
        plt.xlabel('Nome do Participante')
        plt.ylabel('IMC (Índice de Massa Corporal)')
        plt.bar(nomes, valores_imc, color=cores_barras)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()