from math import sqrt
from math import pow
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
    opção=int(input("Escolhe a operação: "))
    while opção<1 or opção>9:
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
        opção=int(input("Opção inválida! Escolhe outra: "))
    match opção:
        case 1:
            system("cls")
            print("--- Mini Calculadora ---")
            n1=float(input("Introduz o primeiro número: "))
            system("cls")
            print("--- Mini Calculadora ---")
            n2=float(input("Introduz o segundo número: "))
            system("cls")
            print("--- Mini Calculadora ---")
            print(f"{n1} + {n2} = {n1+n2:.2f}")
        case 2:
            system("cls")
            print("--- Mini Calculadora ---")
            n1=float(input("Introduz o primeiro número: "))
            system("cls")
            print("--- Mini Calculadora ---")
            n2=float(input("Introduz o segundo número: "))
            system("cls")
            print("--- Mini Calculadora ---")
            print(f"{n1} - {n2} = {n1-n2:.2f}")
        case 3:
            system("cls")
            print("--- Mini Calculadora ---")
            n1=float(input("Introduz o primeiro número: "))
            system("cls")
            print("--- Mini Calculadora ---")
            n2=float(input("Introduz o segundo número: "))
            system("cls")
            print("--- Mini Calculadora ---")
            print(f"{n1} x {n2} = {n1*n2:.2f}")
        case 4:
            system("cls")
            print("--- Mini Calculadora ---")
            n1=float(input("Introduz o número: "))
            system("cls")
            print("--- Mini Calculadora ---")
            n2=float(input("Introduz outro número: "))
            while n2==0:
                system("cls")
                print("--- Mini Calculadora ---")
                print("Erro! Divisão por zero não é permitida. Escolhe outro número, por o qual queres dividir: ")
                n2=float(input("Introduz o número: "))
                system("cls")
                print("--- Mini Calculadora ---")
                print(f"{n1} / {n2} = {n1/n2:.2f}")
            system("cls")
            print("--- Mini Calculadora ---")
            print(f"{n1} / {n2} = {n1/n2:.2f}")
        case 5:
            system("cls")
            print("--- Mini Calculadora ---")
            n1=float(input("Introduz o número: "))
            system("cls")
            print("--- Mini Calculadora ---")
            print(f"{n1}² = {n1**2:.2f}") 
        case 6:
            system("cls")
            print("--- Mini Calculadora ---")
            n1=float(input("Introduz o número: "))
            system("cls")
            print("--- Mini Calculadora ---")
            print(f"{n1}³ = {n1**3:.2f}")
        case 7:
            system("cls")
            print("--- Mini Calculadora ---")
            print("Escolhe a raiz:")
            print("1 - Raiz quadrada")
            print("2 - Raiz cúbica")
            print("3 - Raiz quarta")
            opção_raiz=int(input("Opção de raiz: "))

            while opção_raiz < 1 or opção_raiz > 3:
                system("cls")
                print("--- Mini Calculadora ---")
                print("Opção inválida! Escolhe outra:")
                print("1 - Raiz quadrada")
                print("2 - Raiz cúbica")
                print("3 - Raiz quarta")
                opção_raiz = int(input("Opção de raiz: "))
            match opção_raiz:
                case 1:
                    system("cls")
                    print("--- Mini Calculadora ---")
                    n1=float(input("Introduz o número: "))
                    while n1<0:
                        system("cls")
                        print("--- Mini Calculadora ---")
                        print("Erro! Não existe raiz quadrada real de número negativo!")
                        n1=float(input("Introduz o número: "))
                    system("cls")
                    print("--- Mini Calculadora ---")
                    print(f"√{n1} = {sqrt(n1):.2f}")
                case 2:
                    system("cls")
                    print("--- Mini Calculadora ---")
                    n1=float(input("Introduz o número: "))
                    system("cls")
                    print("--- Mini Calculadora ---")
                    print(f"³√{n1} = {sqrt3(n1):.2f}")
                case 3:
                    system("cls")
                    n1=float(input("Introduz o número: "))
                    while n1<0:
                        system("cls")
                        print("--- Mini Calculadora ---")
                        print("Erro! Não existe raiz quarta real de número negativo!")
                        n1=float(input("Introduz outro número: "))
                    system("cls")
                    print("--- Mini Calculadora ---")
                    print(f"⁴√{n1} = {sqrt4(n1):.2f}")
        case 8:
            system("cls")
            print("--- Mini Calculadora ---")
            n1=float(input("Introduz a base: "))
            system("cls")
            print("--- Mini Calculadora ---")
            n2=float(input("Introduz o expoente: "))
            system("cls")
            print("--- Mini Calculadora ---")
            print(f"{n1}^{n2} = {pow(n1,n2):.2f}")
        case 9:
            system("cls")
            print("--- Mini Calculadora ---")
            print("Saindo...")
            system("cls")
            break
    if opção != 9:
        input("Pressiona ENTER para reiniciar...")