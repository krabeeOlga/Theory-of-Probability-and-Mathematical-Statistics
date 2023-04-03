# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# a) Найти вероятность того, что все 4 карты – крести. 

import numpy as np

def combinations (n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

def probability (x,y):
    return round(x / y, 4)

x = combinations (13,4)     # 13 карт "крести" в колоде, 4 любых карты достаем
y = combinations (52,4)     # число всех исходов - любые 4 карты из 52

print(x)
print(y)
print(f"Вероятность равна: {probability (x,y)}")