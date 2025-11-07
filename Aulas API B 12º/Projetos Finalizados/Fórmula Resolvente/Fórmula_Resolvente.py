from math import sqrt
from os import system

while True:
    system("cls")
    print("--- Fórmula Resolvente ---")
    a=float(input("Coloca o a: "))
    while a==0:
        print("a não poder ser igual a 0!")
        a=float(input("Coloca um a diferente de 0: "))
    b=float(input("Coloca o b: "))
    c=float(input("Coloca o c: "))
    delta= ((b**2)-4*a*c)

    if delta<0:
        system("cls")
        print("--- Fórmula Resolvente ---")
        print(f"O resultado é:\nImpossível")
    elif delta==0:
        system("cls")
        print("--- Fórmula Resolvente ---")
        solucao=(-b/(2*a))
        print(f"O resultado é:\nx={solucao:.2f}")
    else:
        solucao1=((-b + sqrt(delta)) / (2*a))
        solucao2=((-b - sqrt(delta)) / (2*a))
        system("cls")
        print("--- Fórmula Resolvente ---")
        print(f"O resultado é:\nx={solucao1:.2f} ou x={solucao2:.2f}")

    sair=input("Pretende calcular novamente? (s/n): ")
    if sair.lower()!="s":
        system("cls")
        break