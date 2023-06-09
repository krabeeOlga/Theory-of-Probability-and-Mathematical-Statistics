# На соревновании по биатлону один из трех спортсменов стреляет 
# и попадает в мишень. Вероятность попадания для первого спортсмена 
# равна 0.9, для второго — 0.8, для третьего — 0.6. Найти вероятность 
# того, что выстрел произведен: a). первым спортсменом б). 
# вторым спортсменом в). третьим спортсменом.



# Находим полную вероятность:
P_a = (1/3 * 0.9) + (1/3 * 0.8) + (1/3 * 0.6)

# Находим вероятность, что выстрелил первый спортсмен (по ф-ле Байеса):
P_1 = round(((1/3 * 0.9) / P_a), 3)
print(f"Вероятность выстрела первым спортсменом = {P_1}")

# Находим вероятность, что выстрелил первый спортсмен (по ф-ле Байеса):
P_2 = round(((1/3 * 0.8) / P_a), 3)
print(f"Вероятность выстрела первым спортсменом = {P_2}")

# Находим вероятность, что выстрелил первый спортсмен по (ф-ле Байеса):
P_3 = round(((1/3 * 0.6) / P_a), 3)
print(f"Вероятность выстрела первым спортсменом = {P_3}")