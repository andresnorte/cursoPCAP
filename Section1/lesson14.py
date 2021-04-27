x = int(input("Enter number: "))
def even(x):
    if x%2 == 0:
        return True
    else:
        return False
print(even(x))

print("___________________")

def getmax(mas):
    max = mas[0]
    for i in mas:
        if i > max:
            max = i
    return max

print(getmax([54,57,897,678]))

print("___________________")

b = [4,5,6]
print(len(b))

def arif(*numbers):
    ads = 0
    for n in numbers:
        ads = ads + n
    ads = ads/len(numbers)
    return ads

print(arif(3,4,5,7,6))