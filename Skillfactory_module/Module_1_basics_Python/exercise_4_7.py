# Задание 4.7
# Предположим, у вас есть некая целочисленная переменная, значение которой заранее вы не знаете.
# Выведите на печать ответ на вопрос, является ли значение переменной чётным или нечётным числом
# (разумеется, пока что вы будете знать значение, поскольку сами определите его в программе,
# но ничто не мешает нам пофантазировать, что мы получили это значение в ходе выполнения программы, верно?)

number = 2
if number % 2 == 0:
    print(f'Число {number} четное')
else:
    print(f'Число {number} не четное')