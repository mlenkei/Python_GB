# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить ровно k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите количество долек шоколада в ширину: "))
m = int(input("Введите количество долек шоколада в длину: "))
k = int(input("Введите какое количество долек от шоколада хотите отделить: "))

s = m * n # максимальное количество долек

if k < s and n != 1 or m != 1:
    n = n - 1
    m = m - 1
    print("От Шоколадки возможно отделить : ", m, "или", n, "долек")
    if k == n or k == m:
        print("Да, именно ", k, "долек можно отделить от шоколадки")
    
    else:
         print("Не удасться разделить шоколадку всем поровну")
else:
    print("Не удасться разделить шоколадку")