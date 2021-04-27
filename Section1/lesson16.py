import func

a = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())

    a.append(ele)  # добавление элемента

while True:
    print("1 - максимум, 2 - минимум, 3 - сумма, 0 -выход")
    code = input("Введите команду:  ")
    if code == "0":
        exit(0)

    if code == "1":
        r = func.maks(a)
    elif code == "2":
        r = func.mini(a)
    elif code == "3":
        r = func.sumi(a)
    print("Результат:", r)
