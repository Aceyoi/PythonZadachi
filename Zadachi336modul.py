
def testcheck():
    """Функция проверки"""
    assert (float('{:.2f}'.format(suma(5, 5.0))) == 37.32)
    assert (float('{:.2f}'.format(suma(10, -7))) == 120.85)
    assert (float('{:.2f}'.format(suma(10, 55.0))) == 195.24)
    assert (float('{:.2f}'.format(suma(1, 1))) == 3.0)
    pass

def suma(n, x):
    """Функция выполняет вычисление суммирования (2i|+|x|/i^2|)"""
    sum = .0
    for i in range (1, n+1): # совместный цикл от 0 до n
        sum = sum + ( (2 * i + abs( abs(x)) / i ** 2 )) # суммирование
    return sum # Вывод результата