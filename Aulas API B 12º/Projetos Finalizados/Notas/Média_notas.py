from os import system
import statistics

while True:
    system("cls")
    notas_teste=[]
    n_notas=int(input("Quantas notas pertende introduzir?\n"))
    system("cls")

    print("Introduza as notas abaixo: ")
    while n_notas>0:
        adicionar=notas_teste.append(float(input()))
        n_notas-=1

    system("cls")
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

    sair=(input("Pretende calcular novamente? (s/n): "))
    if sair.lower()!="s":
        print("A sair...")
        system("cls")
        break
    else:
        print("Carregando...")