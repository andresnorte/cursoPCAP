x = 0
while True:
    k = input("Введите число, Sum или Quit: ")
    if k != "Sum" and k != "Quit" and k != " ":
        x = x + float(k)

    if k == "Sum":
        print("Сумма введенных чисел", "=", x)
        x = 0

    if k == "Quit":
        exit(0)








