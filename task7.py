
i = int(input("Введите год: "))

if i % 4 == 0 and i % 100 > 0 or i % 400 == 0:
    print("№год високосный")
else:
    print("не високосный") 