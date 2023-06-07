# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е.
# не меньше заданного минимума и не больше заданного максимума)
import random
rand_list_1 = []

n = int(input("Введите длину массива, n = "))
for i in range(n):
    rand_list_1.append(random.randint(-10,11))
print(rand_list_1)

min_number = int(input("Введите минимальное число в диапазоне: "))
max_number = int(input("Введите максимальное число в диапазоне: "))
arr = list()
for i in range(n):
    if min_number <= rand_list_1[i] <= max_number:
        arr.append(rand_list_1[i])
        print("Индекс элемента заданного массива", i)
print("Числа в диапазоне: от ", min_number, "до", max_number, arr)
