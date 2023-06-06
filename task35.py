# проверка простого числа

n = input("Введите число для проверки: ")
def prime_check(n):
    i = 2
    is_prime = True

    while i < n and is_prime:
        if n % i == 0:
            is_prime = False
        i+=1
    if is_prime:
        return "Простое"
    return "не простое"

print(is_prime)
