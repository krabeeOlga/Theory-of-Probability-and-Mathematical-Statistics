# Даны значения зарплат из выборки выпускников: 
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических методов 
# наподобие std, var, mean) среднее арифметическое, среднее квадратичное
# отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.


import math

def calculate_mean(my_list):               # расчет средн. арифм.
    return((sum(my_list) / len(my_list)))   

def calculate_variance_1(my_list):           # расчет несмещенной дисперсии
    diff = [(i - mean) for i in my_list]   
    sqr_diff = [j**2 for j in diff]  
    sum_sqr_diff = sum(sqr_diff)    
    return(sum_sqr_diff / (len(my_list) - 1))

def calculate_variance_2(my_list):           # расчет смещенной дисперсии
    diff = [(i - mean) for i in my_list]   
    sqr_diff = [j**2 for j in diff]  
    sum_sqr_diff = sum(sqr_diff)    
    return(sum_sqr_diff / len(my_list))

def calculate_quadratic_mean(my_list):      # расчет СКО
    return(math.sqrt(variance_1))


my_list = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
sorted(my_list)   # сортировка списка по возрастанию

mean = calculate_mean(my_list)      
print(f"Среднее арифм. = {mean}")  

variance_1 = calculate_variance_1(my_list)   
print(f"Несмещенная дисперсия = {variance_1}")

variance_2 = calculate_variance_2(my_list)   
print(f"Смещенная дисперсия = {variance_2}")

quadr_mean = calculate_quadratic_mean(my_list)
print(f"СКО = {quadr_mean}")












# def probability (x,y):
#     return round(x / y, 4)

# x = combinations (13,4)     # 13 карт "крести" в колоде, 4 любых карты достаем
# y = combinations (52,4)     # число всех исходов - любые 4 карты из 52

# print(x)
# print(y)
# print(f"Вероятность равна: {probability (x,y)}")