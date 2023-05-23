
temper = [-20, 30, -40, 50, 10, -10]
schet = 0
max_dlina = 0

for i in temper:
    if i >0:
        schet += 1
        print("Счет равно: ", max_dlina)
    else:
        if schet > max_dlina:
            max_dlina = schet
            print("Макс равен: ", max_dlina)
        schet = 0
print("Максимальное кол дней: ", max_dlina)