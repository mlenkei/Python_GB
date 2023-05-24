
# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой,
# а некоторые – гербом.
# Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, 
# которые нужно перевернуть

import random

n = int(input("Введите колличество монет для разброса их по столу: "))
rand_list = []
k=0
a=0
b=0
for i in range(n):
    rand_list.append(random.randint(0,1))
    if rand_list[k] == 0 and k < n:
        rand_list[k] = str("решка")
        k = k+1
        a = a +1
    else:
        rand_list[k] = str("орел")
        k = k + 1
        b = b + 1
print("Брошенные на стол монетки выпали в следующем порядке: ", rand_list)
print("Количество решек: ", a)
print("Количество орлов: ", b)       
        
        
if a < b:
    print("Минимальное количество монет с решками нужно перевернуть, чтоб все стали орлами: ", a, "шт.")
else:
    print("Минимальное количество монет с орлами нужно перевернуть, чтоб все стали решками: ", b, "шт.")
