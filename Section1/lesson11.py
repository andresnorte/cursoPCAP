import random

i = int(input("Введите количество элементов списка :  "))
arr = [int(random.random() * 100) for k in range(0, i)]
print(arr)

print("---------------")
b = 0
while b < len(arr):
    print(arr[b])
    b += 1

print("---------------")

myset = list(set(arr))
print(myset)
for k in myset:
    print(k)