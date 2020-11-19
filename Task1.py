#1. Написать функцию `is_prime`, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую `True`, если оно простое, и `False` - иначе.
# (Простые числа - те которые делятся без остатка только на само себя или 1, например 2, 3, 5, 7, 11...)

from cmath import sqrt


def is_prime(number):
    # Все четные числа кроме 2 непростые
    if number % 2 == 0 and number != 2:
        return False
    # 0 и 1 не являются простыми
    if number == 0 or number == 1:
        return False
    # Перебираем числа от 3 до корня из введенного, шаг - 2
    for n in range(3, int(sqrt(number).real) + 1, 2):
        if number % n == 0:  # Если число делится нацело, то оно непростое
            return False
    return True  # Остальные числа простые

n = int(input('Введите число до 1000: '))
print(is_prime(n))