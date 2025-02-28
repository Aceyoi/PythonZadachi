import random

def testcheck():
    """Функция проверки"""
    testarr = [1,2,3,4,5] # список из 5 чисел
    testarr1 = [4, 1, 3, 3, 7, 7, 2, 4, 6, 5] # список из 10 чисел
    testarr2 = [5, 9, 7, 3, 7, 5, 5, 1, 0, 7] # список из 10 чисел

    assert (suma(len(testarr), testarr) == 3) # проверка будели ли сумма равна 3 (len(testarr) - кол-во элементов массива)
    assert (suma(len(testarr1), testarr1) == 2) # проверка будели ли сумма равна 2 (len(testarr) - кол-во элементов массива)
    assert (suma(len(testarr2), testarr2) == -1) # проверка будели ли сумма равна -1 (len(testarr) - кол-во элементов массива)
    pass

def randomi(n, a):
    """Функция заполнения массива(список) случайными числами"""
    for i in range (0, n): # совместный цикл от 0 до n
        a.append (random.randint(0, 9)) # Функция библиотеки random для создания случайного числа от 0 до 9
    pass

def norandomi(n, a):
    """Функция заполнения массива(список) своими числами"""
    for i in range (0, n): # совместный цикл от 0 до n
        a.append(int(input(f"Ведите {i+1} число ")))
    pass

def suma(n, a):
    """Функция выполняет вычисление суммирование a1 - a2 + a3 - ... + (-1)^(n+1)*an"""
    sum = 0
    for i in range (0, n): # совместный цикл от 0 до n
        sum = sum + ((-1) ** i) * a[i] # суммирование
    return sum # Вывод результата