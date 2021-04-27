mydict = {"Name":"Без имени", "Age":-1}
i = input("Enter your name:  ")
k = input("Enter your age:  ")
mydict["Name"] = i
mydict["Age"] = k
for key in mydict:
    print(key, "=", mydict[key])
