from array import *
from Zadachi181modul import * # подключаем модуль

print("Задача: Даны целые числа a1,...a50. Получить сумму тех чисел данной последовательности, которые кратные 5;")
testcheck()
n = int(input("Введите натуральное число n "))
a = array('i',[ ])

print("Вы хотите ввести свои значения массива или случайные?")
check = input("Введите y если хотите ввести случайыне значения ")
if check == "y":
    randomi(n, a)
else:
    norandomi(n, a)

print(a)
print(suma(n, a))