from os import system

while True:
    system("cls")
    print("--- Tabuada ---")
    num=int(input("Escolhe um número: "))
    vezes=1
    while vezes<=12:
        print(f"{num} x {vezes} = {num*vezes:.2f}")
        vezes+=1
    sair=(input("Pretende calcular outra tabuada? (s/n): "))
    if sair.lower()!="s":
        system("cls")
        break