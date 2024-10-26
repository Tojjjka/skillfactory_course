# Задание
# Напишите программу для работы с ежедневником. Она должна уметь записывать,
# редактировать, удалять и выводить дела на каждый день недели.
#
# Инструкция к выполнению задания
# Создайте файл с расширением .py, в котором будете выполнять задание.
# Сгенерируйте двумерный массив размерностью 7×3 и заполните его нулевыми элементами.
# todo_list = [# утро  день  вечер
#             ['',    '',    ''], # понедельник
#             ['',    '',    ''], # вторник
#             ['',    '',    ''], # среда
#             ['',    '',    ''], # четверг
#             ['',    '',    ''], # пятница
#             ['',    '',    ''], # суббота
#             ['',    '',    ''], # воскресенье
#            ]
# С помощью вложенного цикла заполните ежедневник значениями, которые введет пользователь. Можно вводить пустые значения,
# если нет запланированных дел на определенные дни недели и промежутки времени.
# Удалите одну запись из ежедневника, индекс этой записи считайте с консоли.
# Считайте с консоли номер дня недели и новую запись и добавьте эту запись в соответствующий элемент списка.
# Выведите полученный ежедневник в консоль, используйте цикл for для вывода задач по каждому дню недели в отдельной строке.

todo_list = [# утро  день  вечер
            ['',    '',    ''], # понедельник
            ['',    '',    ''], # вторник
            ['',    '',    ''], # среда
            ['',    '',    ''], # четверг
            ['',    '',    ''], # пятница
            ['',    '',    ''], # суббота
            ['',    '',    ''], # воскресенье
           ]
day = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
time = ['утро', 'день', 'вечер']

for i in range(len(day)):
    for j in range(len(time)):
        todo_list[i][j] = input(f'День недели: {day[i]}\nВремя дня: {time[j]}\nЧто нужно сделать: \n')

for row in todo_list:
    print(f'{day[todo_list.index(row)]} = {row}')
print()
for d in day:
    print(f'\t\t{day.index(d)+1}.{d}')
day_todo = int(input('В какой день недели нужно удалить дело(нужно ввести номер): '))
for t in time:
    print(f'\t\t{time.index(t)+1}.{t}')
time_todo = int(input('В какое время дня нужно удалить дело(нужно ввести номер):'))
# todo_list[day_todo-1][time_todo-1] = ''
todo_list[day_todo-1].pop(time_todo-1)
print()
for row in todo_list:
    print(f'{day[todo_list.index(row)]} = {row}')
print()
new_todo = input('Введите новое дело: \n')
for d in day:
    print(f'\t\t{day.index(d)+1}.{d}')
day_todo = int(input('В какой день недели нужно добавить дело(нужно ввести номер): '))
for t in time:
    print(f'\t\t{time.index(t)+1}.{t}')
time_todo = int(input('В какое время дня нужно добавить дело(нужно ввести номер):'))
todo_list[day_todo-1][time_todo-1] = new_todo
print()
for row in todo_list:
    print(f'{day[todo_list.index(row)]} = {row}')

