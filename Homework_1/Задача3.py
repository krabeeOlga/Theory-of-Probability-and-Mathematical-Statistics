# В ящике имеется 15 деталей, из которых 9 окрашены. 
# Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все 3 извлеченные детали окрашены?

import numpy as np

def combinations (n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

def probability (x,y):
    return round(x / y, 4)

x = combinations (9,3)     # 9 окрашенных деталей, 3 любые детали достаем
y = combinations (15,3)     # число всех исходов - любые 3 детали из 15

print(x)
print(y)
print(f"Вероятность равна: {probability (x,y)}")