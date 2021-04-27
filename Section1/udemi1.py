#p1 = str("   Bang!     ")
#p2 = str(" Bang!   ")
#print(p1)
#print(p2)

def whos_first(p1, p2):
    for i in p1:
        if i == "B":
            a = p1.index(i)
    for k in p2:
        if k == "B":
            b = p2.index(k)
    if a < b:
        return "Игрок 1"
    if a > b:
        return "Игрок 2"
    if a == b:
        return "tie"


print(whos_first("   Bang!     ", "        Bang!   "))


