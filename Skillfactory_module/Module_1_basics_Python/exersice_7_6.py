# Задание 7.6
# С помощью Python вычислите математическое выражение 0.33 * 18.42 так,
# чтобы ответом было число 6.0786 (именно с таким количеством знаков после запятой).

from decimal import Decimal

print(Decimal("0.33") * Decimal("18.42"))