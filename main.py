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

import yaml
import csv
import json
import codecs
import datetime
users = []
#чтение данных из файлов
with codecs.open('users.yaml', 'r', 'utf_8_sig') as f:
    yaml_data = yaml.safe_load(f)
with codecs.open('users.csv', 'r', 'utf_8_sig') as f:
    csv_data = csv.DictReader(f)
    for data in csv_data:
        user = {
        'id': data['id'],
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'fathers_name': data['fathers_name'],
        'date_of_birth': data['date_of_birth'],
}
users.append(user)



#создание списка словарей
users = []
for data in yaml_data['users']:
    user = {
        'id': data['id'],
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'fathers_name': data['fathers_name'],
        'date_of_birth': data['date_of_birth'],
}
    users.append(user)

#функция для расчёта возраста
def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - int(birth_date)
    print(age)
    return age

#добавление атрибута age к каждому пользователю
for user in users:
    age = calculate_age(user['date_of_birth'])
    user['age'] = age

#запись данных в файл
with open('users.json', 'w', encoding='utf-8') as f:
   json.dump(users, f, ensure_ascii=False)

#Функция add_user использует модуль json для чтения и записи данных в файл
def add_user(first_name, last_name, fathers_name, date_of_birth):
#Сначала мы открываем файл users.json на чтение и считываем из него данные в переменную data
    with open("users.json", "r") as file:
        data = json.load(file)
#Находим максимальный id в списке пользователей data и вычисляем новый id, увеличивая его на один
        max_id = max([user["id"] for user in data])
#Cоздаем словарь new_user, заполняя его данными о новом пользователе
    new_user = {
        "id": max_id + 1,
        "first_name": first_name,
        "last_name": last_name,
        "fathers_name": fathers_name,
        "date_of_birth": date_of_birth,
        "age": calculate_age(datetime.strptime(date_of_birth, '%Y-%m-%d'))
    }

    data.append(new_user)

    with open("users.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
