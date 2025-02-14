def zad10():
    h = int(input("Введите высоту h "))

    if h < 0:
        t = -1
        print("Высота должна быть положительной")
    else:
        t = (2*h/9.8) ** (1/2)
        print(str(f"Время равно {t:.2f} секунд"))
    # Проверка
    h1 = 10
    h1 = (2 * h / 9.8) ** (1 / 2)
    assert (int(h1) == 1)

    h1 = -1
    assert (h1 == -1)

    pass
#
#
def zad35():
    x = float(input("Введите x "))
    y = float(input("Введите y "))
    z = float(input("Введите z "))

    max1 = x + y + (z/2)
    max2 = x * y * z

    if max1 > max2:
        max = (max1 ** 2) +1
    else:
        max = (max2 ** 2) + 1
    print(str(f"Максимальное число равняется {max}"))

    # Проверка
    x = 5
    y = 5
    z = 2
    max1 = x + y + (z/2)
    max2 = x * y * z
    assert(max1 < max2)
    max = (max2 ** 2) + 1
    assert(max == 2501.0)

    pass
#
#
def zad73():
    k = int(input("Введите число k "))
    i = int(input("Введите число i "))

    if k == i:
        k = 0
        i = 0
    elif k > i:
        i = k
    else:
        k = i

    print(str(f"k = {k}, i = {i}"))
    pass
#
#
def zad115():
    n = int(input("Введите число n "))
    if n < 0:
        print("n должно быть положительным")
    else:
        i = 1
        sum = 0

        while i <= n:
            sum = sum +(1/((2 * i + 1) ** 2))
            i+=1

        print(str(f"Сумма равна {sum:.2f}"))
    pass
#
#
zad = input("Введите номер задачи ")

if zad == "10":
    print(zad10())
elif zad == "35":
    print(zad35())
elif zad == "73":
    print(zad73())
elif zad == "115":
    print(zad115())