# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа
# сделали одинаковое количество журавликов, а Катя сделала в два раза
# больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input('Введите какое колличество журавликов вы бы хотели получить от Пети, Кати и Сережи: '))
print('Катя сделала: ', (s // 6) * 4)
print('Петя и Сережа сделали по: ', s // 6)
print('Если Вы считаете, что вам дети не додали журавликов и разница составляет около: ', (s+2) - (((s // 6) * 4) + (2*( s // 6))), 'журавликов, то предлагаю спросить их у учителя детей, они раньше наделали)))')
