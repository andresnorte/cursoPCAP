def is_full_house(comb) -> True:

    for i in comb:
        if comb.count(i) != 2 and not any.comb != 3:
            continue
        return True


print(is_full_house(["8", "8", "K", "A", "A"]))

sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0

for numeros in seleccionados:
    if numeros in sorteados:
        aciertos += 1

print(aciertos)

miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5
Encontrado = False

for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar
    if Encontrado:
        break

if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []  #
# coloca tu código aquí
for i in miLista:
    if i in newList:
        continue
    newList.append(i)  #
print("La lista solo con elementos únicos:")
print(miLista)
print(newList
