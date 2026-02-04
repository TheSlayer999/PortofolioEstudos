import os
from perguntas import *
import random
from time import sleep

def embaralhar_quiz(perguntas):
    random.shuffle(perguntas)

    """ for pergunta in perguntas:
        resposta_certa = pergunta["respostas"][pergunta["certa"]]
        random.shuffe(pergunta["respostas"])
        pergunta["certa"] = pergunta["respostas"].index(resposta_certa) """

embaralhar_quiz(pr)
n_perguntas=10
certas=0
erradas=0

os.system("cls" if os.name=="nt" else"clear")
print("--- Quiz de Cidadania ---\n")
print("Bem-vindo ao Quiz de Cidadania, o quiz conciste num conjunto de 10 perguntas relacionadas com a disciplina de cidadania.\nBoa Sorte!")
sleep(7)

for i in range (len(pr)):
    os.system("cls" if os.name=="nt" else"clear")
    print("--- Quiz de Cidadania ---\n")
    print(f"{i+1} - {pr[i]['pergunta']}\n")
    for o in range (len(pr[i]["respostas"])):
        print(f"{pr[i]['respostas'][o]}")
    resposta=input("\nQual a resposta certa?: ")
    while resposta.lower()!="a" and resposta.lower()!="b" and resposta.lower()!="c" and resposta.lower()!="d":
        print("\nResposta inválida!")
        resposta=input("Qual a resposta certa?: ")

    if resposta.lower() == pr[i]["certa"][0]:
        certas+=1
    else:
        erradas+=1
        

score=n_perguntas-erradas
os.system("cls" if os.name=="nt" else"clear")
print("--- Quiz de Cidadania ---")
print(f"\nParabéns por concluires o quiz!\nA tua pontuação foi: {score}/{n_perguntas}")
sair=input("\nPressione para qualquer tecla para encerrar...")

os.system("cls" if os.name=="nt" else"clear")
print("--- Quiz de Cidadania ---\n")
creditos()
sleep(3)
os.system("cls" if os.name=="nt" else"clear")