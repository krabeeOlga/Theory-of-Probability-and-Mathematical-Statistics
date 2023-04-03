# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

import numpy as np

def combinations (n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

def probability (x,y):
    return round(x / y, 4) 

# Найдем вероятность того, что все 4 извлекаемых карты - не тузы

x = combinations (48,4)     # 48 "не тузов" в колоде, 4 любых карты достаем
y = combinations (52,4)     # число всех исходов - любые 4 карты из 52

print(x)
print(y)
print(f'Вероятность извлечения "не тузов" равна: {probability (x,y)}')

# Соответственно вероятность извлечь хотя бы один туз:

print(f'Вероятность извлечения "хотя бы одного туза" равна: {1 - probability (x,y)}')