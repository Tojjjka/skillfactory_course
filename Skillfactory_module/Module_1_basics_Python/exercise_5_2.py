# Задание 5.2
# Напишите программу, которая проверяет, являются ли все символы строки символами,
# входящими в набор символов ASCII. Если да, программа должна напечатать True,
# если нет — False. Если строка нулевой длины, тоже напечатать False.

string = 'asdsad'

if len(string) == 0:
    print(False)
else:
    print(string.isascii())