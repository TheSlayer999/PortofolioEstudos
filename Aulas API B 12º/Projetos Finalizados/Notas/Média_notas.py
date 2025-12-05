from os import system
import statistics
import matplotlib.pyplot as plt
import numpy as np

while True:
    system("cls")
    print("--- Cálculo das Notas da Turma ---")
    notas_teste=[]
    n_notas=int(input("Quantas notas pertende introduzir?\n"))

    while n_notas>0:
        tamanho=len(notas_teste)
        system("cls")
        print("--- Cálculo das Notas da Turma ---")
        if tamanho>0:
            notas_teste.sort()
            print(notas_teste)
        print(f"Faltam {n_notas} notas.")
        print("Introduza as notas abaixo: ")
        adicionar=float(input())
        while adicionar<0 or adicionar>20:
            system("cls")
            print("--- Cálculo das Notas da Turma ---")
            notas_teste.sort()
            print(notas_teste)
            print(f"Faltam {n_notas} notas.")
            print("As notas têm que estar entre 0-20")
            print("Introduza as notas abaixo: ")
            adicionar=float(input())
        else:
            adicionard=notas_teste.append(adicionar)
            n_notas-=1

    system("cls")
    print("--- Cálculo das Notas da Turma ---")

    notas_teste.sort()
    print(notas_teste)

    tamanho=len(notas_teste)
    negativas=0
    positivas=0
    for i in range(tamanho):
        if notas_teste[i]>=9.5:
            positivas+=1
        else:
            negativas+=1
    if positivas==1 and negativas==1:
        print(f"Houve {positivas} positiva e {negativas} negativa.")
    elif positivas==1 and negativas>1 and negativas<=0:
        print(f"Houve {positivas} positiva e {negativas} negativas.")
    elif negativas==1 and positivas>1 and positivas<=0:
        print(f"Houve {positivas} positiva e {negativas} negativas.")
    else:
        print(f"Houve {positivas} positivas e {negativas} negativas.")

    média=statistics.median(notas_teste)
    print(f"A média foi {média}.")

    nota_alta=max(notas_teste)
    nota_baixa=min(notas_teste)
    print(f"A nota mais alta foi {nota_alta} e a nota mais baixa foi {nota_baixa}.")

    notas_acima=0
    for o in range(tamanho):
        if notas_teste[o]>média:
            notas_acima+=1
        else:
            notas_acima+=0
    lista_acima=[]
    for p in notas_teste:
        if p>média:
            lista_acima.append(p)
    lista_acima.sort()
    tamanho_acima=len(lista_acima)
    if tamanho_acima>1:
        print(f"E {notas_acima} notas foram acima da média, estas foram: {lista_acima}")
    elif tamanho_acima==0:
        print(f"E nenhuma nota foi acima da média.")
    else:
        print(f"E {notas_acima} nota foi acima da média, esta foi: {lista_acima}")

    gráfico=input("Pretende ver o gráfico? (s/n): ")
    if gráfico.lower()=="s":
        notas_teste.sort()
        alunos=list(range(1, len(notas_teste) + 1))
        plt.bar(alunos, notas_teste, color='purple')
        plt.title('Distribuição de Notas')
        plt.xlabel('Aluno')
        plt.ylabel('Notas')
        plt.ylim(0, 20) 
        plt.show()
        
    sair=(input("Pretende calcular novamente? (s/n): "))
    if sair.lower()!="s":
        print("A sair...")
        system("cls")
        break
    else:
        print("Carregando...")