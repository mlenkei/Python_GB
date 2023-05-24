
n = int(input("Введите число арбузов: 5 "))
ves = [3, 1, 2, 3, 9]
max_arb = ves[0]
min_arb = ves[0]

for i in ves:
    if i > max_arb:
        max_arb = i
    if i < min_arb:
        min_arb = i
print(max_arb)
print(min_arb)

