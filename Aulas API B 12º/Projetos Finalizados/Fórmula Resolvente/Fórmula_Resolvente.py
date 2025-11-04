from math import sqrt
from os import system

while True:
    system("cls")
    print("--- Fórmula Resolvente ---")
    a=float(input("Coloca o a: "))
    b=float(input("Coloca o b: "))
    c=float(input("Coloca o c: "))
    binómio= ((b**2)-4*a*c)

    if binómio<0:
        solução1= "Impossível"
        solução2= "Impossível"
    else:
        solução1=((-b + sqrt(binómio)) / (2*a))
        solução2=((-b - sqrt(binómio)) / (2*a))
    
    system("cls")
    print("--- Fórmula Resolvente ---")
    print(f"O resultado é:\nx={solução1} e x={solução2}")
    sair=input("Pretende continuar? (s/n): ")
    if sair.lower()!="s":
        system("cls")
        break