# Задача: Используя условный цикл while, напишите программу, которая будет считать сумму чисел от 1 до заданного числа..
#
# Инструкция к выполнению задания:
#
# Дана переменная number в которой записано число. number > 1.
# Создайте переменную summ = 0, в которой будете считать итоговую сумму.
# С помощью цикла while посчитайте сумму чисел от 1 до number.
# Выведите полученную сумму в консоль: print(summ).
# Критерии оценки: Программа корректно считает сумму чисел от 1 до введенного числа при разных входных данных.
number = 5
summ = 0
i = 1

while i <= number:
    summ += i
    i += 1

print(summ)
