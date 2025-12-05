notas_teste=[19, 11, 12, 8, 7, 6, 20, 15, 16]
tamanho=len(notas_teste)
negativas=0
positivas=0

for i in range(tamanho):
    if notas_teste[i]>=9.5:
        positivas+=1
    else:
        negativas+=1

print(f"Houve {positivas} positivas e {negativas} negativas!")
positivas_lista=[]
for notas in notas_teste:
    if notas>=9.5:
        positivas_lista.append(notas)
positivas_lista.sort()
print(f"As notas positivas foram: {positivas_lista}")

negativas_lista=[]
for notas in notas_teste:
    if notas<9.5:
        negativas_lista.append(notas)
negativas_lista.sort()
print(f"As notas negativas foram: {negativas_lista}")