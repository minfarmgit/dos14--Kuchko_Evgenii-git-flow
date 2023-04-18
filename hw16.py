from functools import reduce

first_name = ["2_Варвара", "6_Алина", "9_Владислав", "4_Владислав", "5_Анастасия", "3_Антон",
              "1_Марк", "8_Амелия", "7_Василиса", "10_София"]
last_name = ["2_Комарова", "5_Леонова", "10_Фадеева", "6_Соколова", "4_Назаров", "7_Дроздова",
             "8_Гордеева", "3_Смирнов", "9_Николаев", "1_Калашников"]
date_of_birth = ['1_1985', '3_1978', '4_2001', '10_1982', '5_1970', '6_1990', '8_1963',
                 '7_2004', '2_1996', '9_1966']

def transform_reducer_func(prev, curr):
    prev[curr[0]] = curr[1]
    return prev

def transform_strings(array):
    split_data = map(lambda item: item.split("_"), array)
#     for k in split_data:
#        print(k)
    return reduce(transform_reducer_func, split_data, {})

first_name_data = transform_strings(first_name)
#print(first_name_data)
last_name_data = transform_strings(last_name)
date_of_birth_data = transform_strings(date_of_birth)

def reducer_func(prev, key):
    item = {'id': key, 'first_name': first_name_data[key], 'last_name': last_name_data[key],
            'date_of_birth': date_of_birth_data[key]}
    prev.append(item)
    return prev

response = reduce(reducer_func, first_name_data.keys(), [])
sorted_response = sorted(response, key=lambda k: int(float(k['id'])))
for item in sorted_response:
    print(item)
