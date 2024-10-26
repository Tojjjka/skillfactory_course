# Задание
# Создайте программу, которая будет хранить и обрабатывать список, содержащий информацию о ваших коллегах.
#
# Создайте массив coworkers, в котором записаны имена ваших коллег, выведите имя первого и последнего коллеги,
# выведите имена каждого первого и каждого второго коллеги, выведите количество ваших коллег.
# Считайте с консоли имя нового коллеги и добавьте его в массив. Выведите полученный список ваших коллег и его длину.
# Считайте с консоли имя человека, проверьте, работает ли он с вами, и выведите соответствующее сообщение.

# Создайте файл с расширением .py, в котором будете выполнять задание.
# Создайте массив coworkers и запишите в него имена ваших коллег, минимум 5.
# Используя индексы, выведите первый и последний элемент списка.
# С помощью срезов выведите каждый первый и каждый второй элемент списка.
# С помощью метода len() выведите длину списка.
# Используя команду input() считайте с консоли имя нового коллеги и запишите его в массив с помощью метода append().
# И введите длину измененного списка.
# Считайте с консоли имя и с помощью конструкции if elem in list проверьте, есть ли полученное имя в вашем списке.
# Если имя есть, выведите в консоль сообщение, что имя есть в списке, если имени в списке нет — выведите сообщения, что имени в списке нет.

coworkers = ['Anton', 'Vika', 'Bodian', 'Katy', 'Alex']
print(coworkers[0], coworkers[-1])
print(coworkers[::2])
print(coworkers[1::2])
print(len(coworkers))
new_coworkers = input('Введите имя нового коллеги: ')
coworkers.append(new_coworkers)
print(len(coworkers))
verifiable_coworkers = input('Введите имя коллеги которого нужно проверить: ')
if verifiable_coworkers in coworkers:
    print(f'{verifiable_coworkers} есть в списке коллег.')
else:
    print(f'{verifiable_coworkers} имя этого коллеги отсутствует в списке.')