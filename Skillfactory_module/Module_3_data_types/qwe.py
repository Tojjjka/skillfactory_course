
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']


def int_number(lst: list) -> tuple[int, str]:
    num = input('Введите номер: \n')
    if num.isdigit():
        num = int(num)
        return num, lst[num-1]
    else:
        print('\t\t\tВвод выполнен неверно!!\n\t\tПопробуйте еще раз:')
        return int_number(lst)

a, b = int_number(students)
print(a)
print(b)
print(type(a))
print(type(b))
# def int_number() -> int:
#     num = input('Введите номер: \n')
#     if num.isdigit():
#         num = int(num)
#         return num
#     else:
#         print('\t\t\tВвод выполнен неверно!!\n\t\t\tПопробуйте еще раз:')
#         return int_number()
#
# def resolution() -> int:
#     print('Желаете продолжить?\n1.Да/2.Нет')
#     res = int_number()
#     if res == 1:
#         return res
#     elif res == 2:
#         return res
#     else:
#         print('\t\t\t\t!!!Неверный ввод!!!')
#         resolution()
#
#
# a = resolution()
# print(a)
# print(type(a))


