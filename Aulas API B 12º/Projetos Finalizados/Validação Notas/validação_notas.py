from os import system
TESTE=0.6
PROJETO=0.3
ATITUDES=0.1

system("cls")
print("Cálculo de avaliação da disciplina de API-B")
teste=float(input("Indroduza a nota do teste: "))
while teste<0 or teste>20:
    system("cls")
    print("Cálculo de avaliação da disciplina de API-B\nA nota do teste tem que estar entre 0 e 20!")
    teste=float(input("Indroduza a nota do teste: "))
system("cls")
print("Cálculo de avaliação da disciplina de API-B")
projeto=float(input("Indroduza a nota do projeto: "))
while projeto<0 or projeto>20:
    system("cls")
    print("Cálculo de avaliação da disciplina de API-B\nA nota do projeto tem que estar entre 0 e 20!")
    projeto=float(input("Indroduza a nota do projeto: "))
system("cls")
print("Cálculo de avaliação da disciplina de API-B")
atitudes=float(input("Indroduza a nota das  atitudes: "))
while atitudes<0 or atitudes>20:
    system("cls")
    print("Cálculo de avaliação da disciplina de API-B\nA nota das atitudes tem que estar entre 0 e 20!")
    atitudes=float(input("Indroduza a nota das  atitudes: "))

media=(teste*TESTE)+(projeto*PROJETO)+(atitudes*ATITUDES)

if media>=0 and media<4:
    system("cls")
    print(f"Cálculo de avaliação da disciplina de API-B\nA tua média foi: {media:.2f}.\nTiveste fraco, chumbas-te. Esforça-te mais!")
elif media>=4 and media<9.5:
    system("cls")
    print(f"Cálculo de avaliação da disciplina de API-B\nA tua média foi: {media:.2f}.\nTiveste insuficiente, chumbas-te. Esforça-te mais um pouco!.")
elif media>=9.5 and media<13.5:
    system("cls")
    print(f"Cálculo de avaliação da disciplina de API-B\nA tua média foi: {media:.2f}.\nTiveste suficiente, passaste. Mas consegues melhor.")
elif media>=13.5 and media<17.5:
    system("cls")
    print(f"Cálculo de avaliação da disciplina de API-B\nA tua média foi: {media:.2f}.\nTiveste bom, passaste! Boa!")
elif media>=17.5 and media<=20:
    system("cls")
    print(f"Cálculo de avaliação da disciplina de API-B\nA tua média foi: {media:.2f}.\nTiveste muito bom, passaste! Continua assim!")