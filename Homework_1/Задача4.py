# В лотерее 100 билетов. Из них 2 выигрышных. 
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

import numpy as np

def combinations (n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

def probability (x,y):
    return round(x / y, 4)

x = 1                    # 1 благоприятный исход события (оба билета выигрышны)
y = combinations (100,2)  # число всех возможных сочетаний 3х цифр

print(x)
print(y)
print(f"Вероятность равна: {probability (x,y)}")