from os import system
from time import sleep
from funções_calculadora import *

while True:
    system("cls")
    print("--- Mini Calculadora ---")
    print("""Operações disponíveis: 
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Quadrado de um número
6 - Cubo de um número
7 - Raízes
8 - Potência
9 - Tabuada
10 - Sair""")
    opcao=int(input("Escolhe a operação: "))
    while opcao<1 or opcao>10:
        system("cls")
        print("--- Mini Calculadora ---")
        print("""Operações disponíveis: 
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Quadrado de um número
6 - Cubo de um número
7 - Raízes
8 - Potência
9 - Tabuada
10 - Sair""")
        opcao=int(input("Opção inválida! Escolhe outra: "))
    system("cls")
    print("--- Mini Calculadora ---")

    if opcao in (1, 2, 3, 4):
        n1 = float(input("Introduz o primeiro número: "))
        n2 = float(input("Introduz o segundo número: "))

        if opcao == 4:
            while n2 == 0:
                n2 = float(input("Divisão por zero não é permitida. \nEscolhe outro número pelo qual queres dividir: "))
                
        system("cls")
        print("--- Mini Calculadora ---")
        if opcao == 1:
            print(f"{n1} + {n2} = {soma(n1,n2):.2f}")
        elif opcao == 2:
            print(f"{n1} - {n2} = {subtracao(n1,n2):.2f}")
        elif opcao == 3:
            print(f"{n1} x {n2} = {multiplicacao(n1,n2):.2f}")
        else:
            print(f"{n1} ÷ {n2} = {divisao(n1,n2):.2f}")

    elif opcao in (5, 6):
        n1 = float(input("Introduz o número: "))
        system("cls")
        print("--- Mini Calculadora ---")
        if opcao == 5:
            print(f"{n1}² = {quadrado(n1):.2f}")
        else:
            print(f"{n1}³ = {cubo(n1):.2f}")

    elif opcao == 7:
        print("1 - Raiz quadrada\n2 - Raiz cúbica\n3 - Raiz quarta")
        opcao_raiz = int(input("Escolhe a opção da raiz: "))
        while opcao_raiz not in (1, 2, 3):
            print("Opção inválida!")
            opcao_raiz = int(input("Escolhe outra opção: "))

        system("cls")
        print("--- Mini Calculadora ---")
        n1 = float(input("Introduz o número: "))
        while opcao_raiz in (1, 3) and n1 < 0:
            print("Erro! Não existe raiz real de número negativo!")
            n1 = float(input("Introduz outro número: "))

        system("cls")
        print("--- Mini Calculadora ---")
        if opcao_raiz == 1:
            print(f"√{n1} = {sqrt(n1):.2f}")
        elif opcao_raiz == 2:
            print(f"³√{n1} = {sqrt3(n1):.2f}")
        else:
            print(f"⁴√{n1} = {sqrt4(n1):.2f}")

    elif opcao == 8:
        base = float(input("Introduz a base: "))
        exp = float(input("Introduz o expoente: "))
        system("cls")
        print("--- Mini Calculadora ---")
        print(f"{base}^{exp} = {potencia(base, exp):.2f}")
    
    elif opcao == 9:
        num=int(input("Escolhe um número: "))
        system("cls")
        print("--- Mini Calculadora ---")
        tabuada(num)

    if opcao == 10:
        system("cls")
        print("--- Mini Calculadora ---")
        print("Saindo...")
        creditos()
        sleep(3)
        system("cls")
        break

    else:
        input("Pressiona ENTER para reiniciar...")