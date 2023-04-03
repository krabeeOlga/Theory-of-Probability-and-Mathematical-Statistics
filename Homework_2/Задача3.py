# Монету подбросили 144 раза. 
# Какова вероятность, что орел выпадет ровно 70 раз?

# Биномиальное распределение

import numpy as np

def combinations (n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

print((combinations (144,70)) * pow(0.5, 70) * pow(0.5, 74))