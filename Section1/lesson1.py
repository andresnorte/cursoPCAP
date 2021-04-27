def is_full_house(comb):
    new = set(comb)

    print(new)

k = is_full_house(["8", "8", "A", "8", "A"])
print(k)

def is_full_house(comb):
    for i in comb:
        if comb.count(i) == 2 and any([comb.count(i) == 3]):
            return True
        else:
            return False


k = is_full_house(["8", "8", "8", "A", "A"])
print(k)

miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []  #
# coloca tu código aquí
for i in miLista:
    if i in newList:
        continue
    newList.append(i)  #
print("La lista solo con elementos únicos:")
print(miLista)
print(newList)