# Задание
# Напишите программу для работы с контактами в телефонной книге.
#
# Инструкция к выполнению задания
# Создайте словарь — телефонную книгу номеров ваших друзей, где ключом является имя,
#  а значением телефон. Выведите в консоль только имена ваших друзей (метод key ()),
#  выведите в консоль только номера телефонов (метод value()).
# Используя цикл, выведите записи из вашей телефонной книге вида:
#  Контакт: {Имя} Телефон: {Номер телефона} (метод items()).
# Добавьте с помощью консоли номера телефонов для двух новых друзей.
# Поменяйте номер телефона одного из ваших друзей на новый.
# Введите имя друга в консоли, если друг есть в вашей телефонной книжке — удалите запись,
#  если нет — добавьте запись, считав номер телефона с консоли.

phone_book = {'Vika': 897823144121, 'Bogdan': 8978123124412, 'Katy': 8213993120049}
print(phone_book.keys())
print(phone_book.values())
for k, v in phone_book.items():
    print(f'Контакт: {k} Телефон: {v}')
for _ in range(2):
    new_friends = input('Введите имя нового друга:\n')
    new_phone_number = int(input(f'Введите номер телефона {new_friends}:\n'))
    phone_book[new_friends] = new_phone_number
print()
for k, v in phone_book.items():
    print(f'Контакт: {k} Телефон: {v}')
print()
friends = input('Введите имя контакта которому нужно изменить номер телефона: ')
new_number_friends = int(input(f'Введите новый номер телефона для контакта:{friends}\n'))
phone_book[friends] = new_number_friends
print()
verification_friends = input('Введите имя контакта: ')
if verification_friends in phone_book.keys():
    del phone_book[verification_friends]
else:
    print(f'Контакта: {verification_friends} нет в телефонной книге.')
    verification_friends_number = int(input(f'Введите номер телефона для контакта: {verification_friends}\n'))
    phone_book[verification_friends] = verification_friends_number
print()
for k, v in phone_book.items():
    print(f'Контакт: {k} Телефон: {v}')