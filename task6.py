# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
# за проезд и получали билет с номером. Счастливым билетом называют такой билет
# с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

n = int(input('Ведите номер билета: '))

m = n % 1000
k = n // 1000

print(k, m)

m = m % 10 + m // 100 + (m % 100) // 10
k = k % 10 + k // 100 + (k % 100) // 10
     
print("Сумма первой и второй половинок билета: ", k, m)

if k == m:
    print("Билет счастливый, приятного апетита")
else:
    print("Счастье не в билетах, зато Вы не заяц!!!")