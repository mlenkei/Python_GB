# Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов
# первого множества. m — кол-во элементов второго
# множества. Затем пользователь вводит сами элементы множеств.

import random

n = int(input("Введите n - колличество элементов первого множества: "))
m = int(input("Введите m - колличество элементов второго множества: "))
rand_listn = []
rand_listm = []

for i in range(n):
    rand_listn.append(random.randint(0,99))
for i in range(m):
    rand_listm.append(random.randint(0,99))
print(rand_listn, rand_listm)
set_n = set(rand_listn)
set_m = set(rand_listm)
print(set_n, set_m)
pok = set_n & set_m
kool = list(pok)
kool.sort()
print(pok, kool)
for i in kool:
    print(i, end='')

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# print(mol, n, m, set_1, list_1)
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# print(a, k, set_1)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# print(b, k1, set_2)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# print(lok, kool)
# for i in kool:
#     print(i, end='')
