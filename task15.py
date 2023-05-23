
n = int(input("Введите число арбузов: 5 "))
ves = [3, 1, 2, 3, 9]
max_ar = ves[0]
min_ar = ves[0]

for i in ves:
    if i > max_ar:
        max_ar = i
    if i < min_ar:
        min_ar = i
print(max_ar)
print(min_ar)

