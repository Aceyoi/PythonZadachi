from array import *
import random

def testcheck():
    """Функция проверки"""

    pass

def randomi(n):
    """Функция создания и заполнения матрицы случайными числами"""
    return [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

def image(matrix):
    """Функция вывода матрицы"""
    for row in matrix:
        print(row)
    pass

def transform(matrix, n):
    """Преобразование матрицы: строка n становится столбцом n, и наоборот."""
    transformed = [row[:] for row in matrix]  # Создаем копию матрицы
    for i in range(len(matrix)):
        transformed[i][n] = matrix[n][i]
        transformed[n][i] = matrix[i][n]
    return transformed