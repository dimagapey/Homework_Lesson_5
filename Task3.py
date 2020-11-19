# 3. Написать функцию которая вернет площадь фигуры: по-умолчанию треугольника, опционально квадрата.
# На входе 2 величины и параметр типа фигуры.


print("Triangle, Square")
parameter = input("Выберите фигуру: ")

def area(a, h, parameter = 'Triangle'):
    s = None
    if parameter == 'Triangle':
        s = 0.5 * a * h
    else:
        s = a ** 2
    return s, parameter


a = int(input("Сторона фигуры = "))
h = int(input("h = "))
print(area(a, h, parameter))
