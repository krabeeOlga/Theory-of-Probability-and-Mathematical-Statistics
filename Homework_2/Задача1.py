# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, 
# равна 0.8. Стрелок выстрелил 100 раз. Найдите вероятность того, 
# что стрелок попадет в цель ровно 85 раз.

# Биномиальное распределение

import numpy as np

def combinations (n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

print((combinations (100,85)) * pow(0.8, 85) * pow(0.2, 15))