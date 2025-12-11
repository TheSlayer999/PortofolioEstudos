from os import system
from random import randint

while True:
    system("cls")
    print("--- Caça ao Número ---")
    print("1 - Modo Fácil (1-10, 3 tentativas)")
    print("2 - Modo Normal (1-20, 3 tentativas)")
    print("3 - Modo Dificil (1-40, 5 tentativas)")
    print("4 - Modo Extremo (1-100, 5 tentativas)")

    limite = 0
    tentativas = 0
    opcao = int(input("Escolhe uma opção: "))
    
    if opcao == 1:
        limite = 10
        tentativas = 3
    elif opcao == 2:
        limite = 20
        tentativas = 3
    elif opcao == 3:
        limite = 40
        tentativas = 5
    elif opcao == 4:
        limite = 100
        tentativas = 5
        
    while opcao < 1 or opcao > 4:
        system("cls")
        print("--- Caça ao Número ---")
        print("1 - Modo Fácil (1-10, 3 tentativas)")
        print("2 - Modo Normal (1-20, 3 tentativas)")
        print("3 - Modo Dificil (1-40, 5 tentativas)")
        print("4 - Modo Extremo (1-100, 5 tentativas)")
        print("Opção inválida. Escolhe (1-4).")
        opcao = int(input("Escolhe uma opção: "))
        if opcao == 1:
            limite = 10
            tentativas = 3
        elif opcao == 2:
            limite = 20
            tentativas = 3
        elif opcao == 3:
            limite = 40
            tentativas = 5
        elif opcao == 4:
            limite = 100
            tentativas = 5

    system("cls")
    print("--- Caça ao Número ---")
    print(f"Gerei um número aleatório entre 1 e {limite}. Tens {tentativas} tentativas. Boa sorte!")
    num_secreto = randint(1, limite) 
    tentativas_restantes = tentativas 
    escolhas = []

    while tentativas_restantes > 0:

        if len(escolhas) > 0:
            escolhas.sort()
            print(f"Escolhas anteriores: {escolhas}")
        escolha = int(input(f"Faz o teu palpite (1-{limite}): "))
        
        if escolha == num_secreto:
            escolhas.append(escolha)
            system("cls")
            print("--- Caça ao Número ---")
            print(f"Boa! Descobriste o número secreto! Era {num_secreto}. 🥳")
            break 
            
        elif escolha >= 1 and escolha <= limite: 
            escolhas.append(escolha)
            tentativas_restantes -= 1
            system("cls")
            print("--- Caça ao Número ---")
            if escolha > num_secreto:
                print(f"O número foi mais alto! Tens {tentativas_restantes} tentativas.")
            elif escolha < num_secreto:
                print(f"O número foi mais baixo! Tens {tentativas_restantes} tentativas.")
            
        else:
            system("cls")
            print("--- Caça ao Número ---")
            print(f"O teu palpite ({escolha}) está fora do intervalo (1-{limite}). Não perdeste nenhuma tentativa.")
            print(f"Tens {tentativas_restantes} tentativas.")

    if tentativas_restantes == 0:
        system("cls")
        print("--- Caça ao Número ---")
        print(f"Esgotaste as tentativas! O número era {num_secreto}.")
        print("Perdeste! ☠️")

    sair = input("Pretende jogar novamente? (s/n): ")
    if sair.lower() != "s":
        system("cls")
        break
    else:
        print("Carregando...")