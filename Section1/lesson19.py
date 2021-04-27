a = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())

    a.append(ele)

b = []
for k in a:
    if k < 0:
        b.append(k)

print(b)


