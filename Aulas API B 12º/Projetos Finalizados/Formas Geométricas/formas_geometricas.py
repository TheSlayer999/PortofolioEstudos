from funcoes import *
from os import system
from time import sleep

while True:
    system("cls")
    print("CÁLCULO DE ÁREAS E PERÍMETROS")
    print("\n1 - Círculo\n2 - Retângulo\n3 - Triângulo\n4 - Quadrado\n5 - Sair")
    opcao=int(input("Escolhe a opção que pretende: "))
    while opcao<1 or opcao>5:
        system("cls")
        print("CÁLCULO DE ÁREAS E PERÍMETROS")
        print("\n1 - Círculo\n2 - Retângulo\n3 - Triângulo\n4 - Quadrado\n5 - Sair")
        opcao=int(input("A opção tem de estar entre (1-4)\nEscolhe a opção que pretende: "))
    if opcao==1:
        system("cls")
        print("CÁLCULO DE ÁREAS E PERÍMETROS - Círculo")
        raio=float(input("\nQual o raio do círculo: "))
        print(f"\nA área do círculo é {round(area_circulo(raio),2)} e o perímetro é {round(p_circulo(raio),2)}")

    elif opcao==2:
        system("cls")
        print("CÁLCULO DE ÁREAS E PERÍMETROS - Retângulo")
        base=float(input("\nQual a base do retângulo: "))
        altura=float(input("Qual a altura do retângulo: "))
        print(f"\nA área do retângulo é {round(area_retangulo(base,altura),2)} e o perímetro é {round(p_retangulo(base,altura),2)}")

    elif opcao==3:
        system("cls")
        print("CÁLCULO DE ÁREAS E PERÍMETROS - Triângulo")
        print("\n1 - Equilátero\n2 - Isósceles\n3 - Escaleno")
        opcao_t=int(input("Esolhe uma opção:"))
        while opcao_t<1 or opcao_t>3:
            opcao_t=int(input("A opção tem de ser(1-3).\nEsolhe outra opção:"))
        if opcao_t==1:
            system("cls")
            print("CÁLCULO DE ÁREAS E PERÍMETROS - Triângulo Equilátero")
            lado=float(input("\nQual o tamanho de um dos lados: "))
            print(f"\nA área do triângulo é {round(area_triangulo(lado,lado,lado),2)} e o perímetro é {round(p_triangulo(lado,lado,lado),2)}")
        elif opcao_t==2:
            system("cls")
            print("CÁLCULO DE ÁREAS E PERÍMETROS - Triângulo Isósceles")
            lado_igual=float(input("\nQual o tamanho do lado igual: "))
            lado_diferente=float(input("Qual o tamanho do outro lado: "))
            print(f"\nA área do triângulo é {round(area_triangulo(lado_igual,lado_igual,lado_diferente),2)} e o perímetro é {round(p_triangulo(lado,lado,lado),2)}")
        else:
            system("cls")
            print("CÁLCULO DE ÁREAS E PERÍMETROS - Triângulo Escaleno")
            lado1=float(input("\nQual o tamanho do primeiro lado: "))
            lado2=float(input("Qual o tamanho do segundo lado: "))
            lado3=float(input("Qual o tamanho do tereceiro lado: "))
            print(f"\nA área do triângulo é {round(area_triangulo(lado1,lado2,lado3),2)} e o perímetro é {round(p_triangulo(lado1,lado2,lado3),2)}")
        
    elif opcao==4:
        system("cls")
        print("CÁLCULO DE ÁREAS E PERÍMETROS - Quadrado")
        lado=float(input("\nQual o tamanho do lado do quadrado: "))

        print(f"\nA área do quadrado é {round(area_quadrado(lado),2)} e o perímetro é {round(p_quadrado(lado),2)}")
    
    else:
        system("cls")
        print("CÁLCULO DE ÁREAS E PERÍMETROS")
        print("\nSaindo...")
        creditos()
        sleep(3)
        system("cls")
        break

    if opcao>0 or opcao<5:
        continuar=input("Pressione qualquer tecla para voltar ao menu...")