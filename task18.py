# Задача 18: Требуется найти в массиве A[1..N] самый близкий
# по величине элемент к заданному числу X. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
import random

n = int(input("Введите N - колличество элементов в массиве: "))
b = int(input("Введите число, которое Вы бы хотели проверить, в массиве есть ли оно и ближайшие к нему строки в массиве: "))
rand_list = []
c=0
k=0

for i in range(n):
    rand_list.append(random.randint(0,10))

min_z = abs(b - rand_list[0])
print(rand_list, min_z)
k = abs(b - rand_list[i])
if k < min_z:
    min_z = k      
    c = i
print("Ближайшее число к Вашему числу в массиве равно: ", rand_list[c], "их разница составляет: ", b - rand_list[c])
print(rand_list)

