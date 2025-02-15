from Zadachi678modul import * # подключаем модуль
from array import *

print("""Задача: Дана действительная квадратная матрица, порядка n. Преобразовать матрицу по правилу: 
строку с номером n сделать столбцом с номером n, а столбец с номером n сделать строкой с номером n""")
testcheck()
n = int(input("Введите порядок матрицы n "))
matrix = randomi(n)

print("Начальная матрица:")
image(matrix)

x = int(input(f"Выберете строку с номером n для преобразования от 0 до {n-1} "))

if 0 <= x < n:
    transformed = transform(matrix, x)
    print("Изменённая матрица:")
    image(transformed)
else:
    print("Введите другую строку")