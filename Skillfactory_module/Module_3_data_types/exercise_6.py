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


def output_in_numder(lst: list, string: str) -> str:
    print(f'\tСписок {string}:')
    for char in lst:
        print(f'\t\t{lst.index(char)+1}.{char}')


def int_number() -> int:
    num = input('Введите номер: \n')
    if num.isdigit():
        num = int(num)
        return num
    else:
        print('\t\t\tВвод выполнен неверно!!\n\t\t\tПопробуйте еще раз:')
        return int_number()

def int_name_number(lst: list) -> tuple[int, str]:
    num = input('Введите номер: \n')
    if num.isdigit():
        num = int(num)
        return num, lst[num-1]
    else:
        print('\t\t\tВвод выполнен неверно!!\n\t\tПопробуйте еще раз:')
        return int_number(lst)

def resolution() -> int:
    print('Желаете продолжить?\n1.Да/2.Нет')
    res = int_number()
    if res == 1:
        return res
    elif res == 2:
        return res
    else:
        print('\t\t\t\t!!!Неверный ввод!!!')
        resolution()


while True:
    command = input('Введите команду: ')
    if command.isdigit():
        command = int(command)
    else:
        print('\t\tВвод выполнен неверно!')
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        print('\tВыберите студента:')
        output_in_numder(students, 'учеников')
        number_stud, name_stud = int_name_number(students)
        print('\tВыберите предмет:')
        output_in_numder(classes, 'предметов')
        number_clas, name_clas = int_name_number(classes)
        while True:
            print('Введите новую оценку: ')
            mark = int_number()
            if 0 < mark < 6:
                students_marks[name_stud][name_clas].append(mark)
                print(f'Для {name_stud} по предмету {name_clas} добавлена оценка {mark}')
                print()
                break
            else:
                print('\t\t\t!!!Учеников оценивают по пятибалльной шкале!!! ')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for stud in students:
            print(stud)
            for clas in classes:
                marks_sum = sum(students_marks[stud][clas])
                marks_count = len(students_marks[stud][clas])
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
        output_in_numder(students,'учеников')
        print()
        print('\tВведите номер студента которого нужно удалить:')
        student_number, student_name = int_name_number(students)
        students.remove(student_name)
        del students_marks[student_name]
        output_in_numder(students,'учеников')
        print()
    elif command == 5:
        print('5.Добавить ученика в журнал')
        new_student_name = input('Введи имя нового ученика:\n')
        students.append(new_student_name)
        students.sort()
        students_marks[new_student_name] = {}
        for clas in classes:
            students_marks[new_student_name][clas] = []
        output_in_numder(students,'учеников')
        print()
    elif command == 6:
        print('6.Переименовать ученика в журнале')
        output_in_numder(students,'учеников')
        print('\t\t\tВыберите ученика которого нужно переименовать:')
        student_number, student_name = int_name_number(students)
        new_student_name = input('Введи новое имя ученика:\n')
        students[student_number] = new_student_name
        students.sort()
        students_marks[new_student_name] = {}
        for clas in classes:
            students_marks[new_student_name][clas] = students_marks[student_name][clas]
        del students_marks[student_name]
        output_in_numder(students,'учеников')
        print()
    elif command == 7:
        print('7.Удалить предмет из журнала')
        output_in_numder(classes,'предметов')
        print('\tВыберите предмет:')
        clas_number = int_number()
        classes.pop(clas_number-1)
        output_in_numder(classes,'предметов')
        print()
    elif command == 8:
        print('8.Добавить предмет в журнал')
        print('\tУкажите число добавляемых предметов: ')
        quantity_clas = int_number()
        if quantity_clas == 0:
            continue
        elif quantity_clas == 1:
            output_in_numder(classes, 'предметов')
            new_clas = input('Введите название нового предмета:\n')
            if new_clas in classes:
                print('Такой предмет уже есть!')
            else:
                classes.append(new_clas)
                for stud in students:
                    students_marks[stud][new_clas] = []
                output_in_numder(classes, 'предметов')
        elif quantity_clas >= 1:
            list_new_clas = []
            for i in range(quantity_clas):
                new_clas = input('Введите название нового предмета:\n')
                if new_clas in classes:
                    print('Такой предмет уже есть!')
                else:
                    list_new_clas.append(new_clas)
                    classes.append(new_clas)
            for stud in students:
                for clas in list_new_clas:
                    students_marks[stud][clas] = []
            output_in_numder(classes, 'предметов')
        print()
    elif command == 9:
        print('9.Переименовать предмет в журнале')
        print('\tВыберите предмет:')
        output_in_numder(classes, 'предметов')
        number_old_clas, name_old_clas = int_name_number(classes)
        new_name_clas = input('Введите новое название предмета:\n')
        classes[number_old_clas] = new_name_clas
        for stud in students:
            students_marks[stud][new_name_clas] = students_marks[stud][name_old_clas]
            del students_marks[stud][name_old_clas]
        output_in_numder(classes, 'предметов')
        print()
    elif command == 10:
        print('10.Удалить оценку из журнала')
        print('\tВыберите студента:')
        output_in_numder(students, 'учеников')
        number_stud, name_stud = int_name_number(students)
        print('\tВыберите предмет:')
        output_in_numder(classes, 'предметов')
        number_clas, name_clas = int_name_number(classes)
        print('\tВыберите оценку')
        output_in_numder(students_marks[name_stud][name_clas], 'оценок')
        number_mark = int_number()
        students_marks[name_stud][name_clas].pop(number_mark-1)
        print(f'{name_stud} - {name_clas} = {students_marks[name_stud][name_clas]}')
        print()
    elif command == 11:
        print('11.Изменить оценку в журнале')
        print('\tВыберите студента:')
        output_in_numder(students, 'учеников')
        number_stud, name_stud = int_name_number(students)
        print('\tВыберите предмет:')
        output_in_numder(classes, 'предметов')
        number_clas, name_clas = int_name_number(classes)
        print('\tВыберите оценку')
        output_in_numder(students_marks[name_stud][name_clas], 'оценок')
        number_mark = int_number()
        print('\tВведите новую оценку')
        new_mark = int_number()
        students_marks[name_stud][name_clas][number_mark-1] = new_mark
        print(f'{name_stud} - {name_clas} = {students_marks[name_stud][name_clas]}')
        print()
    elif command == 12:
        print('12.Вывод всех оценок по предметам ученика')
        print('\tВыберите ученика:')
        output_in_numder(students, 'учеников')
        number_name_stud, name_stud = int_name_number(students)
        print(name_stud)
        for clas in classes:
            print(f'\t\t{clas} - {students_marks[name_stud][clas]}')
        print()
    elif command == 13:
        print('13.Вывод среднего балла по предметам ученика')
        print('\tВыберите ученика:')
        output_in_numder(students, 'учеников')
        number_name_stud, name_stud = int_number(students)
        print(name_stud)
        for clas in classes:
            marks_sum = sum(students_marks[name_stud][clas])
            marks_count = len(students_marks[name_stud][clas])
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
