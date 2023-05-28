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

n = int(input("Введите N - колличество элементов в массиве : "))

b= b1 = b2 = int(input("Введите число, которое Вы бы хотели проверить, соответсвенно найдем ближайшие к нему строки в массиве: "))
rand_list = []
c=1
k=0

for i in range(n):
    rand_list.append(random.randint(0,100))
try:
    for i in range(n):
        b1 = b1 - c   
        b2 = b2 + c   
        for i in range(n):
            min_z = b1
            max_z = b2
            print(rand_list, min_z, max_z)
            k = rand_list[i]
            print(k, min_z, max_z)
            if k == min_z or k == max_z:
                print("Ближайшее число в этом массиве к ", b, "это число ", k) 
                raise StopIteration
except StopIteration:
    pass
 