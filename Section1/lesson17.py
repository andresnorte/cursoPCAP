while True:
    i = int(input("Enter first number: "))
    k = int(input("Enter second number: "))

    try:
        if k == 0:
            raise Exception ("На ноль делить нельзя!")
    except ZeroDivisionError:
        print("Бесконечность")
    except Exception as exp:
        print(exp)
    else:
        c = i/k
        print(c)