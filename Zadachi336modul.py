
def testcheck():
    """Функция проверки"""
    assert (suma(5, 5.0) == 37.32)
    assert (suma(10, -7) == 120.85)
    pass

def suma(n, x):
    """Функция выполняет вычисление"""
    sum = .0
    for i in range (1, n+1): # совместный цикл от 0 до n
        sum = sum + ( (2 * i + abs( abs(x)) / i ** 2 )) # суммирование
    sum = float('{:.2f}'.format(sum))
    return sum # Вывод результата