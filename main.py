import json
import yaml
from datetime import datetime, date
import codecs

roles = {}
users = []
organisations = []


class Permissions:
    def __init__(self, create=False, read=False, update=False, delete=False):
        self._create = create
        self._read = read
        self._update = update
        self._delete = delete

    @property
    def create(self):
        return self._create

    @property
    def read(self):
        return self._read

    @property
    def update(self):
        return self._update

    @property
    def delete(self):
        return self._delete

    @property
    def get_obj(self):
        return {
            'create': self._create,
            'read': self._read,
            'update': self._update,
            'delete': self._delete,
        }


class Role:
    def __init__(self, name, permissions_dict):
        self._name = name
        self._role = {}
        for key, value in permissions_dict.items():
            self._role[key] = Permissions(**value)

    @property
    def name(self):
        return self._name

    def __getitem__(self, key):
        return self._role[key]

    @property
    def get_obj(self):
        permissions = {}
        for key, value in self._role.items():
            permissions[key] = value.get_obj
        return {
            'name': self._name,
            'permissions': permissions
        }


class Entity:
    def __init__(self, entity_id, role):
        self._entity_id = entity_id
        self._role = role

    @property
    def entity_id(self):
        return self._entity_id

    @property
    def role(self):
        return self._role


class User(Entity):
    def __init__(self, entity_id, role, first_name, last_name, fathers_name, date_of_birth):
        super().__init__(entity_id, role)
        self._first_name = first_name
        self._last_name = last_name
        self._fathers_name = fathers_name
        self._date_of_birth = date_of_birth

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def fathers_name(self):
        return self._fathers_name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def age(self):
        today = date.today()
        return today.year - self._date_of_birth.year

    @property
    def get_obj(self):
        return {
            'entity_id': self._entity_id,
            'role': self._role.get_obj,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'fathers_name': self._fathers_name,
            'date_of_birth': self._date_of_birth,
        }


class Organisation(Entity):
    def __init__(self, entity_id, role, creation_date, unp, name):
        super().__init__(entity_id, role)
        self._creation_date = creation_date
        self._unp = unp
        self._name = name

    @property
    def creation_date(self):
        return self._creation_date

    @property
    def unp(self):
        return self._unp

    @property
    def name(self):
        return self._name

    @property
    def get_obj(self):
        return {
            'entity_id': self._entity_id,
            'role': self._role.get_obj,
            'creation_date': self._creation_date,
            'unp': self._unp,
            'name': self._name,
        }


class App(Entity):
    def __init__(self, entity_id, role, name):
        super().__init__(entity_id, role)
        self._name = name

    @property
    def name(self):
        return self._name


# Функция add_users использует модуль json для записи данных в файл
def save_permissions_data(users_data_input, organisations_data_input):
    data_to_save = {
        'users': [],
        'organisations': [],
    }
    for user_item in users_data_input:
        data_to_save['users'].append(user_item.get_obj)
    for organisation_item in organisations_data_input:
        data_to_save['organisations'].append(organisation_item.get_obj)
    with open("users-data.json", "w", encoding='utf-8') as file:
        json.dump(data_to_save, file, ensure_ascii=False)


def user_add(data):
    max_id = max([int(user_item.entity_id) for user_item in users])
    users.append(User(
        max_id + 1,
        roles[data['role_name']],
        data['first_name'],
        data['last_name'],
        data['fathers_name'],
        data['date_of_birth'],
    ))


# Чтение данных из файлов users.json, apps.yaml, roles.yaml и создание объектов

with codecs.open('roles.yaml', 'r', 'utf_8_sig') as f:
    roles_data = yaml.load(f, Loader=yaml.FullLoader)
    for roleK, roleV in roles_data.items():
        newRole = {}
        roles[roleK] = Role(roleK, roleV)
    print(roles['bank']['CreditAccount'].read)

with codecs.open('users.json', 'r', 'utf_8_sig') as f:
    json_data = json.load(f)
    users_data = json_data['Users']
    for user in users_data:
        users.append(
            User(user['entity_id'], roles[user['role']], user['first_name'], user['last_name'], user['fathers_name'],
                 int(user['date_of_birth'])))
    organisations_data = json_data['Organisations']
    for organisation in organisations_data:
        organisations.append(
            Organisation(organisation['entity_id'], roles[organisation['role']], organisation['creation_date'],
                         organisation['unp'], organisation['name']))

with codecs.open('app.yaml', 'r', 'utf_8_sig') as f:
    apps_data = yaml.load(f, Loader=yaml.FullLoader)['Apps']
    apps = []
    for app in apps_data:
        apps.append(App(app['entity_id'], app['role'], app['name']))

user_add({
    'first_name': 'Евгений',
    'role_name': 'default',
    'last_name': 'Кучко',
    'fathers_name': 'Николаевич',
    'date_of_birth': '1990',
})

save_permissions_data(users, organisations)
