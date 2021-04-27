a = input("Введите делимое: ")
b = input("Введите делитель: ")
if b !="0":
    d = float(a)/float(b)
    print(a, "/", b, "=", d)
else:
    d = str("Besconechnost")
    print(a, "/", b, "=", d)
