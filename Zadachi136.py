from Zadachi136modul import * # подключаем модуль

print("Задача: Даны натуральное число n, действительные числа a1,..., an. Вычислить: a1 - a2 + a3 - ... + (-1)^(n+1)*an;")
testcheck()
n = int(input("Введите натуральное число n "))
a = []

print("Вы хотите ввести свои значения массива или случайные?")
check = input("Введите y если хотите ввести случайыне значения ")
if check == "y":
    randomi(n, a)
else:
    norandomi(n, a)

print(a)
print(suma(n, a))


