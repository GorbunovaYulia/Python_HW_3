'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*
5
    1 2 3 4 5
    6
    -> 5
'''
from random import randint
n = int(input("Введите количество элементов в массиве: "))
list_1 = [randint(1, 20) for _ in range(n)]
print(list_1)
x = int(input("Введите число X: "))
rasnost = 0
temp = 10000
for i in range(n):
    rasnost = x - list_1[i]
    if rasnost < 0:
        rasnost *= -1
    if rasnost < temp:
        minNumber = list_1[i]
        temp = rasnost
    rasnost = 0
print(minNumber)
