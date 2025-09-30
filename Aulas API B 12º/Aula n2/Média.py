n1=float(input("Escreve a nota do teste nº1: "))
n2=float(input("Escreve a nota do teste nº2: "))

media=(n1+n2)/2

""" print("A tua média é: ",media) ou
print(f"A tua média é: {media}") """

if media>=0 and media<9.5: 
    print(f"A tua média é: {media}")
    print("Ups! Tiveste negativa!")

elif media>=9.5 and media<14.5:
    print(f"A tua média é: {media}")
    print("Passaste! Tiveste suficiente.")

elif media>=14.5 and media<17.5:
    print(f"A tua média é: {media}")
    print("Boa! Tiveste bom!")

elif media>=17.5 and media<=20:
    print(f"A tua média é: {media}")
    print("Parabéns! Tiveste excelente!")

else:
    print("ERRO")

#if é igual a se
#elif se quisermos adicionar mais ses
#else é igual a senão