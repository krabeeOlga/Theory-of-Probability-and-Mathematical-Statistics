# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации,
# равна 0.0004. В жилом комплексе после ремонта в один день включили 
# 5000 новых лампочек. Какова вероятность, что ни одна из них не перегорит 
# в первый день? Какова вероятность, что перегорят ровно две?

# Распределение Пуассона

import numpy as np

def probability (p,n,m):
    return pow(n*p, m) * np.math.exp(-(n*p)) / np.math.factorial(m)

print(probability (0.0004, 5000, 0))
print(probability (0.0004, 5000, 2))