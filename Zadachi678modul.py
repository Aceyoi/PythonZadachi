import numpy as np, array

def testcheck():
    """Функция проверки"""
    matrix1 = np.matrix([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

    transformed1 = transform(matrix1, 1)
    transformedtest1 = np.matrix([[1, 4, 3],
                                  [2, 5, 8],
                                  [7, 6, 9]])
    assert(np.array_equal(transformed1, transformedtest1))

    matrix2 = np.matrix([[72, 50, 28, 26, 90],[20, 58, 28, 65, 54],[46, 82, 50, 74, 41],[18, 56, 31, 26, 14],[57,  1, 48,  3, 62]])

    transformed2 = transform(matrix2, 1)
    transformedtest2 = np.matrix([[72, 20, 28, 26, 90],[50, 58, 82, 56,  1],[46, 28, 50, 74, 41],[18, 65, 31, 26, 14],[57, 54, 48,  3, 62]])
    assert(np.array_equal(transformed2, transformedtest2))

    matrix3 = np.matrix([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

    transformed3 = transform(matrix3, 1)
    transformedtest3 = np.matrix([[1, 4, 3],
                                 [2, 5, 8],
                                 [7, 6, 9]])
    assert(np.array_equal(transformed3, transformedtest3))


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