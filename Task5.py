a = int(input('Сторона квадрата: '))
def square(a):
    my_perimeter = 4 * a
    my_square = a * a
    my_diag = (a ** 2) / 2
    my_diag = my_diag ** 0.5

    k = (my_perimeter, my_square, my_diag)

    return k

print(square(a))