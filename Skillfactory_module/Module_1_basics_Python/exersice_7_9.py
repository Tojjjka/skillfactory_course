# Задание 7.9
# Напишите 3 варианта, как в эту строку вместо подчёркиваний можно подставить числа 4 и 4
# (автомобиля и омнибуса) и название моста «Саутуарк»:
# "Сегодня утром __ автомобиля и __ омнибуса проехали по мосту __."

count = 4
name = 'Саутуарк'
print("Сегодня утром %d автомобиля и %d омнибуса проехали по мосту %s." % (4, 4, 'Саутуарк'))
print(f"Сегодня утром {count} автомобиля и {count} омнибуса проехали по мосту {name}.")
print("Сегодня утром {} автомобиля и {} омнибуса проехали по мосту {}.".format(4, 4, 'Саутуарк'))