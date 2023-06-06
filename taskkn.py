# крестики нолики

field = [0,1,2,3,4,5,6,7,8]


def fieldPrint(feld):
    print(field[0], "", field[1], "", field[2])
    print(field[3], "", field[4], "", field[5])
    print(field[6], "", field[7], "", field[8])

def chW(field):
    if (field[0] == field[1] == field[2]) or (field[3] == field[4] == field[5]) or (field[6] == field[7] ==field[8]):
        return True
    else:
        return False
fieldPrint(field)

count = 0
win = False

while (win == False):

    if (count >= 5):
        win = chW(field)

    print("Ваш ход, крестик : ")
    target = int(input())
    field[target] = "X"
    count += 1
    print(count)
    fieldPrint(field)
    print()
    print ("ПК")

    for i in range(0, 8):
        if (field) != "X" and (field) != "O":
            field[i] = "O"
            break

    fieldPrint(field)    