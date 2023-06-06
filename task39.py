# бежим по массиву

m1 = [3, 1, 3, 4, 2, 4, 12]
m2 = [4, 15, 43, 1, 15, 1]

for i in m1:
    print("элемент", i)
    print(m2.count(i))
    if m2.count(i) == 0:
        print(i)