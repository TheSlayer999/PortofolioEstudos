from os import system
def soma(n1,n2):
    return n1+n2

system("cls")
print("--- SOMA ---")
n1=float(input("Introduza o 1º número para a soma: "))
n2=float(input("Introduza o 2º número para a soma: "))
print(f"Resultado: {n1} + {n2} = {soma(n1,n2)}")