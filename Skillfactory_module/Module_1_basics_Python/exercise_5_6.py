# Задание 5.6
# Напишите программу-однострочник, удаляющую последовательность символов --+-- с конца строки.
# Удаляться должна именно последовательность в таком виде, в котором она указана.
# Например, строка «--+-- Запись номер 1 --+--» после обработки должна выглядеть так:
# «--+-- Запись номер 1».

string = '--+-- Запись номер 1 --+--'
print(string.removesuffix(' --+--'))