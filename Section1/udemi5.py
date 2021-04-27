l = 10
count1 = 0
count2 = 0
while l >= 1:
    print("В игре", l, "палочек")
    a1 = int(input("Ваня, Сколько палочек берешь? :  "))
    l = l - a1
    count1 +=1
    print("В игре", l, "палочек")
    a2 = int(input("Петя, Сколько палочек берешь? :  "))
    l = l - a2
    count2 +=1
if count1 > count2:
    print("Выиграл игрок 2")
else:
    print("Выиграл игрок 1")
