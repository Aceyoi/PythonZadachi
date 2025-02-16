from array import *
import random
import numpy as np

def testcheck():
    """Функция проверки"""

    pass

def image(matrix):
    """Функция вывода матрицы"""
    for row in matrix:
        print(row)
    pass

def transform(matrix, n):
    """Преобразование матрицы: строка n становится столбцом n, и наоборот."""
    transformed = matrix.copy()  # Создаем копию матрицы
    for i in range(matrix.shape[0]):
        transformed[i, n] = matrix[n, i]
        transformed[n, i] = matrix[i, n]
    return transformed