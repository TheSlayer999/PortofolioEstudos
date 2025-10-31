from os import system
from random import randint
while True:
    system("cls")
    print("--- Caça ao número ---")
    print("1 - Jogar\n2 - Sair")
    opcao = int(input("Escolhe uma opção: "))
    
    while opcao < 1 or opcao > 2:
        opcao = int(input("Opção inválida! Escolhe outra opção: "))
    
    if opcao == 1:
        system("cls")
        print("--- Caça ao número ---")
        random = randint(1, 10)
        tentativas = 3
        
        while tentativas > 0:
            escolha = int(input("Introduz um número (1-10): "))
            
            if escolha > random:
                tentativas -= 1
                system("cls")
                print("--- Caça ao número ---")
                if tentativas > 0:
                    print(f"Demasiado alto! Tens {tentativas} tentativas restantes.")
            elif escolha < random:
                tentativas -= 1
                system("cls")
                print("--- Caça ao número ---")
                if tentativas > 0:
                    print(f"Demasiado baixo! Tens {tentativas} tentativas restantes.")
            elif random == escolha:
                system("cls")
                print("--- Caça ao número ---")
                print(f"Boa! Descobriste o número! Era {random}.")
                break
        
        if tentativas == 0:
            system("cls")
            print("--- Caça ao número ---")
            print("Esgotaste as tentativas!")
            print(f"O número era {random}.")
            
        input("Pressiona ENTER para voltar ao menu...")
    
    else:
        system("cls")
        print("--- Caça ao número ---")
        print("Saindo...")
        system("cls")
        break