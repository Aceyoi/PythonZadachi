from array import *
import random

def testcheck():
    """Функция проверки"""
    testarr = array('i', [1,2,3,4,5]) # массив из 5 чисел
    assert (suma(len(testarr), testarr) == 3) # проверка будели ли сумма равна 3 (len(testarr) - кол-во элементов массива)
    pass

def randomi(n, a):
    """Функция заполнения массива случайными числами"""
    for i in range (0, n): # совместный цикл от 0 до n
        a.append (random.randint(0, 9)) # Функция библиотеки random для создания случайного числа от 0 до 9
    pass

def norandomi(n, a):
    """Функция заполнения массива своими числами"""
    for i in range (0, n): # совместный цикл от 0 до n
        a.append(int(input(f"Ведите {i+1} число ")))
    pass

def suma(n, a):
    """Функция выполняет вычисление"""
    sum = 0
    for i in range (0, n): # совместный цикл от 0 до n
        sum = sum + ((-1) ** i) * a[i] # суммирование
    return sum # Вывод результата