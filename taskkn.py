# крестики нолики

field = [0,1,2,3,4,5,6,7,8]

def fieldPrint(field):
    print(field[0], "", field[1], "", field[2])
    print(field[3], "", field[4], "", field[5])
    print(field[6], "", field[7], "", field[8])

def chW(field):
    if (field[2] == field[5] == field[8]== "X") or (field[1] == field[4] == field[7]== "X") or (field[0] == field[3] == field[6]== "X") or (field[2] == field[4] == field[6]== "X") or (field[0] == field[4] == field[8]== "X") or (field[0] == field[1] == field[2]== "X") or (field[3] == field[4] == field[5]== "X") or (field[6] == field[7] == field[8]== "X"):
        print("Вы выйграли, поздравляем")
        exit()
    if (field[2] == field[5] == field[8]== "O") or (field[1] == field[4] == field[7]== "O") or (field[0] == field[3] == field[6]== "O") or (field[2] == field[4] == field[6]== "O") or (field[0] == field[4] == field[8]== "O") or (field[0] == field[1] == field[2]== "O") or (field[3] == field[4] == field[5]== "O") or (field[6] == field[7] == field[8]== "O"):
        print("Вы проиграли самому искусственному интелекту, держитесь")
        exit()    
    else:
        return False
fieldPrint(field)

count = 0
win = False

while (win == False):

    if (count >= 3):
        win = chW(field)
    if count == 5:
        print("Поздравляю с ничьей")
        exit()
    print("Ваш ход, ставте в поле крестик : ")
    target = int(input())
    field[target] = "X"
    count += 1
    print(count)
    fieldPrint(field)
    print()
    print ("Ход искуственного интелекта")

    for i in range(0, 8):
        if field[0] == field[1] == "X" and field[2] != "O":
            field[2] = "O"
            break
        if field[0] == field[1] == "X" and field[0] != "O":
            field[1] = "O"
            break    
        if field[2] == field[3] == "X" and field[1] != "O":
            field[1] = "O"
            break
        if field[4] == field[5] == "X" and field[3] != "O":
            field[3] = "O"
            break
        if field[4] == field[3] == "X" and field[5] != "O":
            field[5] = "O"
            break
        if field[7] == field[8] == "X" and field[6] != "O":
            field[6] = "O"
            break
        if field[7] == field[6] == "X" and field[8] != "O":
            field[8] = "O"
            break
        if field[0] == field[3] == "X" and field[6] != "O":
            field[6] = "O"
            break
        if field[6] == field[3] == "X" and field[0] != "O":
            field[0] = "O"
            break
        if field[1] == field[4] == "X" and field[7] != "O":
            field[7] = "O"
            break
        if field[7] == field[4] == "X" and field[1] != "7":
            field[1] = "O"
            break
        if field[2] == field[5] == "X" and field[8] != "O":
            field[8] = "O"
            break
        if field[8] == field[5] == "X" and field[2] != "O":
            field[2] = "O"
            break
        if field[4] == field[0] == "X" and field[8] != "O":
            field[8] = "O"
            break
        if field[8] == field[4] == "X" and field[0] != "O":
            field[0] = "O"
            break
        if field[2] == field[4] == "X" and field[6] != "O":
            field[6] = "O"
            break
        if field[6] == field[4] == "X" and field[2] != "O":
            field[2] = "O"
            break
        if field[i] != "X" and field[i] != "O":
            field[i] = "O"
            break 
            

    fieldPrint(field)   

