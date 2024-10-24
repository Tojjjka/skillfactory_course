# Задача: Напишите программу, которая вычисляет четность и нечетность числа, знак числа и выводит результат в консоль.

number = input('Введите число: ')
if int(number) % 2 == 0 and int(number) > 0:
    print(f'Число {number} положительное, четное.')
elif int(number) % 2 == 0 and int(number) < 0:
    print(f'Число {number} отрицательное, четное.')
elif int(number) % 2 != 0 and int(number) > 0:
    print(f'Число {number} положительное, нечетное.')
elif int(number) % 2 != 0 and int(number) < 0:
    print(f'Число {number} отрицательное, нечетное.')
else:
    int(number) == 0
    print('Число = 0')
