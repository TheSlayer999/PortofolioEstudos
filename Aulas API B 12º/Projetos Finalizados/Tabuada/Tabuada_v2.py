from os import system

while True:
    system("cls")
    print("--- Tabuada ---")
    num=int(input("Escolhe um número: "))
    for i in range (1,13):
        print(f"{num} x {i} = {num*i:.2f}")
    sair=(input("Pretende calcular outra tabuada? (s/n): "))
    if sair.lower()!="s":
        system("cls")
        break
    else:
        print("Carregando...")