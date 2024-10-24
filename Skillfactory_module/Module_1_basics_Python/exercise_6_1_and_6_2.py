# Задание 6.1
# Напишите программу, которая выводит в консоль приглашение «Введите IP-адрес:»
# и принимает от пользователя адрес в формате «255.255.255.255», то есть, например, 192.168.1.144.
# Полученный ответ нужно разбить на октеты и затем вывести на печать,
# использовав в качестве разделителя символ подчёркивания.
# Для приведённого примера результат должен выглядеть так: 192_168_1_144.

# ip_adres = input('Введите ip в формате 255.255.255.255: ')
#
# ip = ip_adres.split('.')
# ip1 = '_'.join(ip)
# print(ip1)
#
# print('_'.join(ip_adres.split('.')))
#
#
# print(ip_adres.replace('.', '_'))

# # ip_adre = '192.168.1.144'
#
#
#
#
#
#
# def func_ip(ip_adr):
#     list_ip = []
#     if len(ip_adr.split('.')) == 4:
#         for num in ip_adr.split('.'):
#             if int(num) > 0 and int(num) <= 255:
#                 list_ip.append(num)
#             else:
#                 return f'Число {num} должно входить в диапазон от 1 до 255'
#     else:
#         return 'Вы ввели не верный ip'
#     return f"Ваше ip: {'_'.join(list_ip)}"
#
# print(func_ip(input('Введите ip в формате 255.255.255.255: ')))
# # 192_168_1_144





# ip_adre = '192.168.123'


# def func_ip(ip_adr):
#     if len(ip_adr.split('.')) == 4:
#         if [num for num in ip_adr.split('.') if int(num) > 0 and int(num) <= 255]:
#             return '_'.join([num for num in ip_adr.split('.') ])
#         else:
#             return f'Число {num} должно входить в диапазон от 1 до 255'
#     else:
#         return 'Вы ввели не верный ip'
#
#
# print(func_ip(ip_adre))
# # 192_168_1_144









ip_address = '192.168.1.144'


def func_ip(address):
    ip_nums = address.split('.')
    if not len(ip_nums) == 4:
        return 'Вы ввели не верный ip'
    for num in ip_nums:
        if not  0 < int(num) <= 255:
            return f'Число {num} должно входить в диапазон от 1 до 255'
    else:
        return f"Ваше ip: {address.replace('.','_')}"

print(func_ip(ip_address))
# 192_168_1_144