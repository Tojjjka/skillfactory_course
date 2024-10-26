# Самостоятельная работа
# Доработайте код итогового проекта, расширив его список команд.
#
# Добавьте возможность удалять и редактировать данные по оценкам, предметам и ученикам.
# Добавьте вывод информации по всем оценкам для определенного ученика.
# Добавьте вывод среднего балла по каждому предмету по определенному ученику.
# Добавьте еще команды, которые, на ваш взгляд, могут быть полезны для этой задачи.
import random

commends = ('''
                                                Список команд:
        
        1. Добавить оценки ученика по предмету                          8.Добавить предмет в журнал
        2. Вывести средний балл по всем предметам по каждому ученику    9.Переименовать предмет в журнале
        3. Вывести все оценки по всем ученикам                          10.Удалить оценку из журнала
        4.Удалить ученика из журнала                                    11.Изменить оценку в журнале
        5.Добавить ученика в журнал                                     12.Вывод всех оценок по предметам ученика
        6.Переименовать ученика в журнале                               13.Вывод среднего балла по предметам ученика
        7.Удалить предмет из журнала
                                              14. Выход из программы
        ''')

students = ['Вика', 'Катя', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
            {students_marks[student]}''')
print(commends)


def output_in_number(lst: list, string: str):
    print(f'\tСписок {string}:')
    for char in lst:
        print(f'\t\t{lst.index(char)+1}.{char}')


def get_number(text: str) -> int:
    while True:
        num = input(text)
        if num.isdigit():
            num = int(num)
            return num
        else:
            print('\t\t\tВвод выполнен неверно!!\n\t\t\tПопробуйте еще раз:')


def resolution() -> int:
    while True:
        res = get_number('Желаете продолжить?\n1.Да/2.Нет')
        if res == 1 or res == 2:
            return res
        else:
            print('\t\t\t\t!!!Неверный ввод!!!')


def check_for_inclusion_in_list(list: list, text1: str, text2: str, text3: str) -> str:
    while True:
        print(text1)
        output_in_number(list, text2)
        i = get_number(text3) - 1
        if i in range(len(list)):
            return list[i]
        else:
            print('\t\t\t!!!Введен неверный номер!!!')


while True:
    command = get_number('Введите номер: \n')
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        name_stud = check_for_inclusion_in_list(students, 'Выберите студента: ', 'учеников', 'Введите номер ученика: ')
        name_clas = check_for_inclusion_in_list(classes, 'Выберите предмет: ', 'предметов', 'Введите номер предмета: ')
        while True:
            mark = get_number('Введите новую оценку: ')
            if 0 < mark < 6:
                students_marks[name_stud][name_clas].append(mark)
                print(f'Для {name_stud} по предмету {name_clas} добавлена оценка {mark}')
                print()
                break
            else:
                    print('\t\t\t!!!Учеников оценивают по пятибалльной шкале!!!')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for stud in students:
            print(stud)
            for clas in classes:
                marks_sum = sum(students_marks[stud][clas])
                if marks_sum == 0:
                    marks_sum = 1
                marks_count = len(students_marks[stud][clas])
                if marks_count == 0:
                    marks_count = 1
                print(f'{clas} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for stud in students:
            print(stud)
            for clas in classes:
                print(f'\t{clas} - {students_marks[stud][clas]}')
            print()
    elif command == 4:
        print('4.Удалить ученика из журнала')
        stud_name = check_for_inclusion_in_list(students, 'Выберите студента: ', 'учеников', 'Введите номер ученика: ')
        students.remove(stud_name)
        del students_marks[stud_name]
        output_in_number(students,'учеников')
        print()
    elif command == 5:
        print('5.Добавить ученика в журнал')
        while True:
            output_in_number(students, 'учеников')
            new_student_name = input('Введи имя нового ученика:\n')
            if new_student_name.isalpha():
                if not new_student_name in students:
                    students.append(new_student_name)
                    students.sort()
                    students_marks[new_student_name] = {}
                    for clas in classes:
                        students_marks[new_student_name][clas] = []
                    output_in_number(students,'учеников')
                    print()
                    break
                else:
                    print('\t\t\t!!!Ученик с таким именем уже есть в журнале!!!')
            else:
                print('\t\t\t!!!Имя не должно содержать цифр!!!')
    elif command == 6:
        print('6.Переименовать ученика в журнале')
        student_name = check_for_inclusion_in_list(students, 'Выберите студента: ', 'учеников', 'Введите номер ученика: ')
        student_index = students.index(student_name)
        while True:
            new_student_name = input('Введи новое имя ученика:\n')
            if new_student_name.isalpha():
                if not new_student_name in students:
                    students[student_index] = new_student_name
                    students.sort()
                    students_marks[new_student_name] = {}
                    for clas in classes:
                        students_marks[new_student_name][clas] = students_marks[student_name][clas]
                    del students_marks[student_name]
                    output_in_number(students,'учеников')
                    print()
                    break
                else:
                    print('\t\t\t!!!Ученик с таким именем уже есть в журнале!!!')
            else:
                print('\t\t\t!!!Имя не должно содержать цифр!!!')
    elif command == 7:
        print('7.Удалить предмет из журнала')
        while True:
            output_in_number(classes,'предметов')
            clas_index = get_number('Выберите предмет: ') - 1
            if clas_index in range(len(classes)):
                name_clas = classes[clas_index - 1]
                classes.pop(clas_index)
                output_in_number(classes,'предметов')
                print()
                break
            else:
                print('Неверный ввод!')
    elif command == 8:
        print('8.Добавить предмет в журнал')
        quantity_clas = get_number('Укажите число добавляемых предметов: ')
        if quantity_clas == 0:
            continue
        elif quantity_clas == 1:
            output_in_number(classes, 'предметов')
            new_clas = input('Введите название нового предмета:\n')
            if new_clas in classes:
                print('Такой предмет уже есть!')
            else:
                classes.append(new_clas)
                for stud in students:
                    students_marks[stud][new_clas] = []
                output_in_number(classes, 'предметов')
        elif quantity_clas >= 1:
            list_new_clas = []
            for i in range(quantity_clas):
                new_clas = input(f'Введите название {i+1} предмета:\n')
                if new_clas in classes:
                    print('Такой предмет уже есть!')
                else:
                    list_new_clas.append(new_clas)
                    classes.append(new_clas)
            for stud in students:
                for clas in list_new_clas:
                    students_marks[stud][clas] = []
            output_in_number(classes, 'предметов')
        print()
    elif command == 9:
        print('9.Переименовать предмет в журнале')
        name_old_clas = check_for_inclusion_in_list(classes,'Выберите предмет', 'предметов', 'Введите номер предмета: ')
        index_old_clas = classes.index(name_old_clas)
        while True:
            new_name_clas = input('Введите новое название предмета:\n')
            if not new_name_clas in classes:
                classes[index_old_clas] = new_name_clas
                for stud in students:
                    students_marks[stud][new_name_clas] = students_marks[stud][name_old_clas]
                    del students_marks[stud][name_old_clas]
                output_in_number(classes, 'предметов')
                print()
                break
            else:
                print('Такой предмет уже есть в журнале!')
    elif command == 10:
        print('10.Удалить оценку из журнала')
        name_stud = check_for_inclusion_in_list(students,'Выберите студента', 'учеников', 'Введите номер ученика: ')
        name_clas = check_for_inclusion_in_list(classes,'Выберите предмет', 'предметов', 'Введите номер предмета: ')
        while True:
            for i in range(len(students_marks[name_stud][name_clas])):
                print(f'{i + 1}.{students_marks[name_stud][name_clas][i]}')
            number_mark = get_number('Выберите номер удаляемой оценки: ')
            if number_mark - 1 in range(len(students_marks[name_stud][name_clas])):
                students_marks[name_stud][name_clas].pop(number_mark-1)
                print(f'{name_stud} - {name_clas} = {students_marks[name_stud][name_clas]}')
                print()
                break
            else:
                print('Неверный ввод!')
    elif command == 11:
        print('11.Изменить оценку в журнале')
        name_stud = check_for_inclusion_in_list(students,'Выберите студента', 'учеников', 'Введите номер ученика: ')
        name_clas = check_for_inclusion_in_list(classes,'Выберите предмет', 'предметов', 'Введите номер предмета: ')
        while True:
            print('\tВыберите оценку')
            for i in range(len(students_marks[name_stud][name_clas])):
                print(f'{i + 1}.{students_marks[name_stud][name_clas][i]}')
            index_mark = get_number('Выберите номер оценки которую нужно изменить: ') - 1
            if index_mark in range(len(students_marks[name_stud][name_clas])):
                while True:
                    new_mark = get_number('Введите новую оценку: ')
                    if 0 < new_mark < 6:
                        students_marks[name_stud][name_clas][index_mark] = new_mark
                        print(f'{name_stud} - {name_clas} = {students_marks[name_stud][name_clas]}')
                        print()
                        break
                    else:
                        print('\t\t\t!!!Учеников оценивают по пятибалльной шкале!!!')
                break
            else:
                print('Неверный ввод!')
    elif command == 12:
        print('12.Вывод всех оценок по предметам ученика')
        name_stud = check_for_inclusion_in_list(students,'Выберите студента', 'учеников', 'Введите номер ученика: ')
        print(name_stud)
        for clas in classes:
            print(f'\t\t{clas} - {students_marks[name_stud][clas]}')
        print()
    elif command == 13:
        print('13.Вывод среднего балла по предметам ученика')
        name_stud = check_for_inclusion_in_list(students,'Выберите студента', 'учеников', 'Введите номер ученика: ')
        print(name_stud)
        for clas in classes:
            marks_sum = sum(students_marks[name_stud][clas])
            if marks_sum == 0:
                marks_sum = 1
            marks_count = len(students_marks[stud][clas])
            if marks_count == 0:
                marks_count = 1
            print(f'\t\t{clas} - {marks_sum // marks_count}')
        print()
    elif command == 14:
        print('14. Выход из программы')
        break
    result = resolution()
    if result == 1:
        print(commends)
        continue
    else:
        break
