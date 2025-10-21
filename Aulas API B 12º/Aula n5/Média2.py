TESTE=0.6
PROJETO=0.3
ATITUDES=0.1

print("Cálculo de avaliação da disciplina de API-B")
teste=float(input("Indroduza a nota do teste: "))
projeto=float(input("Indroduza a nota do projeto: "))
atitudes=float(input("Indroduza a nota das  atitudes: "))
media=(teste*TESTE)+(projeto*PROJETO)+(atitudes*ATITUDES)

if media>=0 and media<4:
    print(f"A tua média foi: {media:.2f}.\nTiveste fraco, chumbas-te,esforça-te mais!")
elif media>=4 and media<9.5:
    print(f"A tua média foi: {media:.2f}.\nTiveste insuficiente, chumbas-te, esforça-te mais um pouco!.")
elif media>=9.5 and media<13.5:
    print(f"A tua média foi: {media:.2f}.\nTiveste suficiente, passaste, mas consegues melhor!")
elif media>=13.5 and media<17.5:
    print(f"A tua média foi: {media:.2f}.\nTiveste bom, passaste, boa!")
elif media>=17.5 and media<19.5:
    print(f"A tua média foi: {media:.2f}.\nTiveste muito bom, passaste! Continua assim!")
elif media>=19.5 and media<=20:
    print(f"A tua média foi: {media:.2f}.\nTiveste excelente, passaste! Continua assim! Parabéns!")
else:
    print("ERRO")