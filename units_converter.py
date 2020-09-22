print('Введите исходные единицы имерения')
print('Доступные: lea, mi, yd, ft, in')
measure_1 = str(input())
print('Введите новые единицы измерения')
print('Доступные: lea, mi, yd, ft, in')
measure_2 = str(input())
print('Сколько?')
num_begin = int(input())
dict_to_measures = {'lea': 190081, 'mi': 63360, 'yd': 36, 'ft': 12, 'in': 1}
num_end = num_begin * dict_to_measures[measure_1] / dict_to_measures[measure_2]
print(num_end)
