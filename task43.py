# Дан список чисел. Посчитать, сколько пар.

from random import randint

randomList = []
listLenght = 10

for i in range (0, listLenght):
    randomList.append(randint(1, 5))
print (randomList)
randomList = sorted(randomList)
print (randomList)
count = 0

for i in range (1, listLenght):
    
    if (randomList(i) == randomList (i - 1)):
        count = count + 1
        i = i + 1
    print(count)    


