import json
import yaml
from datetime import datetime
import codecs

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


class App(Entity):
    def __init__(self, entity_id, role, name):
        super().__init__(entity_id, role)
        self._name = name

    @property
    def name(self):
        return self._name

def create_user(entity_id, role, first_name, last_name, fathers_name, date_of_birth):
    return {'entity_id': entity_id, 'role': role, 'first_name': first_name, 'last_name': last_name, 'fathers_name': fathers_name, 'date_of_birth': date_of_birth}

# Чтение данных из файлов users.json, apps.yaml, roles.yaml и создание объектов

with codecs.open('users.json', 'r', 'utf_8_sig') as f:
    users_data = json.load(f)['Users']
    users = []
    for user in users_data:
        users.append(User(user['entity_id'], user['role'], user['first_name'], user['last_name'], user['fathers_name'], int(user['date_of_birth'])))

with codecs.open('app.yaml', 'r', 'utf_8_sig') as f:
    apps_data = yaml.load(f, Loader=yaml.FullLoader)['Apps']
    apps = []
    for app in apps_data:
        apps.append(App(app['entity_id'], app['role'], app['name']))

with codecs.open('roles.yaml', 'r', 'utf_8_sig') as f:
    roles_data = yaml.load(f, Loader=yaml.FullLoader)
    roles = {}
    for roleK, roleV in roles_data.items():
        newRole = {}
        roles[roleK] = Role(roleK, roleV)
    print(roles['bank']['CreditAccount'].read)
