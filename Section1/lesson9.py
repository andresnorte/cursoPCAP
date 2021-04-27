spis = ["alfa", "beta", "gamma", "zeta"]
i = 0
while i < len(spis):
    print("Индекс элемента " , i, spis[i])
    i += 1

i = 0
i = int(input("Введите номер элемента от 0 до 3 :  "))
if i < len(spis):
    print("Вы ввели ", spis[i])
else:
    print("Элемента с таким индексом не существует")
