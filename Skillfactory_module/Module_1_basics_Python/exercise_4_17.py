# Задание 4.14
# У вас есть переменная seconds_since_birthdate, в которой записано количество секунд с
# момента рождения человека. Количество секунд не может быть эквивалентно более чем 200 годам.
# Напишите код, который будет выводить в консоль количество полных лет, прожитых этим человеком.

seconds_since_birthdate = 200034300


print(seconds_since_birthdate // (60 * 60 * 24 * 365))
print(int(seconds_since_birthdate // (60 * 60 * 24 * 365)))
print(round(seconds_since_birthdate // (60 * 60 * 24 * 365)))

