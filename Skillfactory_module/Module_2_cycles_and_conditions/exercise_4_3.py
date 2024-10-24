# Задача: Напишите программу, которая выводит таблицу умножения от 1 до 10 для заданного числа.
number = input('Введите число: ')
for i in range(1,11):
    print(number, end = "\n" )
    print(f'{number} * {i} = {int(number) * i}')