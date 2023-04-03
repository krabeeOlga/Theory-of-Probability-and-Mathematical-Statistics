# На входной двери подъезда установлен кодовый замок, 
# содержащий десять кнопок с цифрами от 0 до 9. 
# Код содержит три цифры, которые нужно нажать одновременно . 
# Какова вероятность того, что человек, не знающий код, 
# откроет дверь с первой попытки?

import numpy as np

def combinations (n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

def probability (x,y):
    return round(x / y, 4)

x = 1                    # 1 благоприятный исход события (угадал код с первой попытки)
y = combinations (10,3)  # число всех возможных сочетаний 3х цифр

print(x)
print(y)
print(f"Вероятность равна: {probability (x,y)}")