import yaml
import csv
import json
import codecs
import datetime

users = []
# чтение данных из файлов
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

# создание списка словарей
users1 = []
for data in yaml_data['users']:
    user = {
        'id': data['id'],
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'fathers_name': data['fathers_name'],
        'date_of_birth': data['date_of_birth'],
        }
    users1.append(user)

# Объединяем 2 бъединяем два списка users и users1
users.extend(users1)


# функция для расчёта возраста
def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - int(birth_date)
    return age


# добавление атрибута age к каждому пользователю
for user in users:
    age = calculate_age(user['date_of_birth'])
    user['age'] = age

# запись данных в файл
with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False)


# Функция add_user использует модуль json для чтения и записи данных в файл
def add_user(first_name, last_name, fathers_name, date_of_birth):
    # Сначала мы открываем файл users.json на чтение и считываем из него данные в переменную data
    with codecs.open('users.json', 'r', 'utf_8_sig') as file:
        data = json.load(file)
        # Находим максимальный id в списке пользователей data и вычисляем новый id, увеличивая его на один
        max_id = max([int(user["id"]) for user in data])
    # Cоздаем словарь new_user, заполняя его данными о новом пользователе
    new_user = {
        "id": max_id + 1,
        "first_name": first_name,
        "last_name": last_name,
        "fathers_name": fathers_name,
        "date_of_birth": date_of_birth,
        "age": calculate_age(date_of_birth),
    }
    data.append(new_user)

    with open("users.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

add_user(
    'Евгений',
    'Кучко',
    'Николаевич',
    '1990',
)
