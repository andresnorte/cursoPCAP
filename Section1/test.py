def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(10))
print(data)



def f(n):
    a, b = 0, 1
    for i in range(n):
        if a % 2 == 0:
             yield a
        a, b = b, a + b

data = list(f(10))
print(data)

def f(n):
    a, b = 0, 1
    for i in range(n):
        if a % 2 == 0:
            yield a
        a, b = b, a + b

data = list(f(8))
print(data)

def f(n):
    a, b = 0, 1
    i = 0
      while i <= n:
        if a % 2 == 0:
            yield a
        a, b = b, a + b
        i += 1
data = list(fi(8))
print(data)