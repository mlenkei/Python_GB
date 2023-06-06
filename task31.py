# Последовательность фибоначи
n = 5

def f(n):
    print(n)
    if n == 0 and n == 1:
        return 1
    return f(n-1) + f(n-2)



print(f(n - 2))