import math
def sqrt3(num):
 return num ** (1/3)

print("--- Mini Calculadora ---")
print("Operações disponíveis: ")
print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Quadrado de um número \n6 - Cubo de um número \n7 - Raízes \n8 - Potência")
opção=int(input("Escolhe a operação: "))
if opção==1:
    n1=float(input("Introduz o primeiro número: "))
    n2=float(input("Introduz o segundo número: "))
    print(f"{n1} + {n2} = {n1+n2:.2f}")
elif opção==2:
    n1=float(input("Introduz o primeiro número: "))
    n2=float(input("Introduz o segundo número: "))
    print(f"{n1} - {n2} = {n1-n2:.2f}")
elif opção==3:
    n1=float(input("Introduz o primeiro número: "))
    n2=float(input("Introduz o segundo número: "))
    print(f"{n1} x {n2} = {n1*n2}")
elif opção==4:
    n1=float(input("Introduz o primeiro número: "))
    n2=float(input("Introduz o segundo número: "))
    if n2!=0:
        print(f"{n1} : {n2} = {n1/n2}")
    else:
         print("Erro! Divisão por zero não é permitida.")
elif opção==5:
    n1=float(input("Introduz o número: "))
    print(f"{n1}² = {n1**2}") 
elif opção==6:
    n1=float(input("Introduz o número: "))
    print(f"{n1}³ = {n1**3}")
elif opção==7:
    print("Escolhe a raiz:")
    print("1 - Raiz quadrada")
    print("2 - Raiz cúbica")
    print("3 - Raiz quarta")
    opção_raiz=int(input("Opção de raiz: "))
    if opção_raiz==1:
       n1=float(input("Introduz o número: "))
       if n1>=0:
            print(f"√{n1} = {math.sqrt(n1):.2f}")
       else:
            print("Erro! Não existe raiz quadrada real de número negativo!")
    elif opção_raiz==2:
        n1=float(input("Introduz o número: "))
       # print(f"³√{n1} = {n1**(1/3)}")
        print(f"³√{n1} = {sqrt3(n1):.2f}")
    elif opção_raiz==3:
        n1=float(input("Introduz o número: "))
        if n1>=0:
            print(f"⁴√{n1} = {n1**0.25:.2f}")
        else:
            print("Erro! Não existe raiz quarta real de número negativo!")
elif opção==8:
    n1=float(input("Introduz a base: "))
    n2=float(input("Introduz o expoente: "))
    print(f"{n1}^{n2} = {math.pow(n1,n2):.2f}")
else:
    print(f"Erro! A opção {opção} não está disponível.")