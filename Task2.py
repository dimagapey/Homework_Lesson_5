# 2. Написать программу которая вернет количество введенных пользователем слов и общее число символов.

x = str(input("Введите какой-либо текст: "))
sym_x = len(x)
words = x.count(' ') + 1
print("Количество символов", sym_x)
print("Количество слов", words)