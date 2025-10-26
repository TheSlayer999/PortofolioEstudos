from math import sqrt, pow
from os import system

def sqrt3(num):
 return num ** (1/3)
def sqrt4(num):
 return num ** (1/4)

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
9 - Sair""")
    opcao=int(input("Escolhe a operação: "))
    while opcao<1 or opcao>9:
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
9 - Sair""")
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
            print(f"{n1} + {n2} = {n1 + n2:.2f}")
        elif opcao == 2:
            print(f"{n1} - {n2} = {n1 - n2:.2f}")
        elif opcao == 3:
            print(f"{n1} x {n2} = {n1 * n2:.2f}")
        else:
            print(f"{n1} ÷ {n2} = {n1 / n2:.2f}")

    elif opcao in (5, 6):
        n1 = float(input("Introduz o número: "))
        system("cls")
        print("--- Mini Calculadora ---")
        if opcao == 5:
            print(f"{n1}² = {n1 ** 2:.2f}")
        else:
            print(f"{n1}³ = {n1 ** 3:.2f}")

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
        print(f"{base}^{exp} = {pow(base, exp):.2f}")

    if opcao == 9:
        system("cls")
        print("Saindo...")
        system("cls")
        break

    else:
        input("Pressiona ENTER para reiniciar...")