import json
import yaml
from datetime import datetime, date
import codecs
from flask import Flask, request, jsonify


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


class Client:
    def __init__(self, client_id, role):
        self._client_id = client_id
        self._role = role

    @property
    def client_id(self):
        return self._client_id

    @property
    def role(self):
        return self._role


class User(Client):
    def __init__(self, client_id, role, first_name, last_name, fathers_name, date_of_birth):
        super().__init__(client_id, role)
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
            'client_id': self._client_id,
            'role': self._role.get_obj,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'fathers_name': self._fathers_name,
            'date_of_birth': self._date_of_birth,
        }


class Organisation(Client):
    def __init__(self, client_id, role, creation_date, unp, name):
        super().__init__(client_id, role)
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
            'client_id': self._client_id,
            'role': self._role.get_obj,
            'creation_date': self._creation_date,
            'unp': self._unp,
            'name': self._name,
        }


class App(Client):
    def __init__(self, client_id, role, name):
        super().__init__(client_id, role)
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
    max_id = max([int(user_item._client_id) for user_item in users])
    users.append(User(
        max_id + 1,
        roles[data['role_name']],
        data['first_name'],
        data['last_name'],
        data['fathers_name'],
        data['date_of_birth'],
    ))

with codecs.open('roles.yaml', 'r', 'utf_8_sig') as f:
    roles_data = yaml.load(f, Loader=yaml.FullLoader)
    for roleK, roleV in roles_data.items():
        newRole = {}
        roles[roleK] = Role(roleK, roleV)
    print(roles['bank']['creditaccounts'].read)

with codecs.open('users.json', 'r', 'utf_8_sig') as f:
    json_data = json.load(f)
    users_data = json_data['Users']
    for user in users_data:
        users.append(
            User(user['client_id'], roles[user['role']], user['first_name'], user['last_name'], user['fathers_name'],
                 int(user['date_of_birth'])))
    organisations_data = json_data['Organisations']
    for organisation in organisations_data:
        organisations.append(
            Organisation(organisation['client_id'], roles[organisation['role']], organisation['creation_date'],
                         organisation['unp'], organisation['name']))

with codecs.open('app.yaml', 'r', 'utf_8_sig') as f:
    apps_data = yaml.load(f, Loader=yaml.FullLoader)['Apps']
    apps = []
    for app in apps_data:
        apps.append(App(app['client_id'], app['role'], app['name']))


app = Flask(__name__)
@app.route('/api/v1/users/<int:client_id>', methods=['GET'])
def get_user(client_id):
    try:
        # Check if the user has permission to read users
        token = request.headers.get('users')
        if not token:
            return jsonify({"status": "error", "message": "Token header not found"}), 400
        token_data = json.loads(token)
        if token_data.get('client_id') != client_id:
            return jsonify({"status": "error", "message": "User does not have permission to read users"}), 403

        # Find the user with the specified client_id
        user = next((u for u in users if u['client_id'] == client_id), None)
        if not user:
            return jsonify({"status": "error", "message": f"No user with id = {client_id}"}), 404

        # Check if the user's role has access to read users
        if user['role'] != 'role':
            return jsonify({"status": "error", "message": "User does not have permission to read users"}), 403

        # Return the user data
        return jsonify(user)
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "An error occurred"}), 500

@app.route('/api/v1/organisations/<client_id>', methods=['GET'])
def get_organisation(client_id):

    try:
            # Check if the user has permission to access organizations
        if not has_permission(request.headers.get('Organisations')):
             return jsonify(
                {'status': 'error', 'message': 'User does not have permission to access organizations'}), 403

            # Check if the token header is present
        token_header = request.headers.get('Organisations')
        if not token_header:
            return jsonify({'status': 'error', 'message': 'Token header not found'}), 400


            # Check if the client_id in the token matches the client_id in the URL
        if token_data.get('client_id') != client_id:
            return jsonify({'status': 'error', 'message': 'Token client_id does not match URL client_id'}), 400

            # Find the organization with the given client_id
        organization = find_organization(client_id)
        if not organization:
            return jsonify({'status': 'error', 'message': f'No organization with id = {client_id}'}), 404

            # Check if the user has permission to access the organization
        if not has_organization_permission(request.headers.get('Organisations'), organization):
            return jsonify(
                {'status': 'error', 'message': 'User does not have permission to access this organization'}), 403

            # Return the organization data
        return jsonify(organization)

    except Exception as e:
            # Log the error
        app.logger.error(str(e))
        return jsonify({'status': 'error', 'message': 'An error occurred while processing the request'}), 500


@app.route('/api/v1/users', methods=['GET'])
def get_users():

    try:
        # Check if token header exists
        if 'token' not in request.headers:
            raise ValueError("Token header not found")

        # Check if client has permission to view users
        token = request.headers['users']
        client_id = request.json['client_id']
        user = next((u for u in users if u['client_id'] == client_id), None)
        if not user:
            raise ValueError("User not found")
        if user['role'] != 'role':
            raise ValueError("User does not have permission to view users")

        # Return all users
        return jsonify(users)
    except ValueError as e:
        # Log the error
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400


@app.route('/api/v1/organisations', methods=['GET'])
def get_organisations():

    try:
        # Check if the user has permission to read organisations
        token = request.headers.get('Organisations')
        if not token:
            return jsonify({"status": "error", "message": "Token header not found"}), 400

        token_data = json.loads(token)
        client_id = token_data.get('client_id')
        if not client_id:
            return jsonify({"status": "error", "message": "Client ID not found in token header"}), 400

        # Find the organisation with the given ID
        organisation = next((org for org in organisations if org['client_id'] == client_id), None)
        if not organisation:
            return jsonify({"status": "error", "message": "Organisation not found"}), 404

        # Check if the user has the permission to read organisations
        if organisation['role'] != 'role':
            return jsonify({"status": "error", "message": "User does not have permission to read organisations"}), 403

        # Return data about all organisations
        return jsonify(organisations)
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500


@app.route('/api/v1/users', methods=['PUT'])
def create_user():

    try:
        # Get the token header
        token_header = request.headers.get('users')

        # Check if the token header exists
        if not token_header:
            return jsonify({'status': 'error', 'message': 'Token header not found'}), 400

        # Get the client ID from the token header
        client_id = json.loads(token_header)['client_id']

        # Check if the user has write access to the users resource
        user = get_user_by_id(client_id)
        if 'write' not in user['role']:
            return jsonify({'status': 'error', 'message': 'User does not have write access to users resource'}), 403

        # Get the user data from the request body
        user_data = request.get_json()

        # Write the user data to the JSON file
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(user_data, f)

        # Return a success message
        return jsonify({'status': 'success', 'message': 'User created successfully'}), 201
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': 'An error occurred while creating the user'}), 500


@app.route('/api/v1/organisations', methods=['PUT'])
def create_organisation():

    try:
        # Get the token from the header
        token = request.headers.get('Organisations')
        if not token:
            return jsonify({"status": "error", "message": "Token header not found"}), 400

        # Check if the user has permission to write to organizations
        client_id = request.headers.get('client_id')
        with open('users.json', 'r') as f:
            users = json.load(f)
        user = next((u for u in users if u['client_id'] == client_id), None)
        if not user or 'write_organizations' not in user['role']:
            return jsonify(
                {"status": "error", "message": "User does not have permission to write to organizations"}), 403

        # Get the organization data from the request body
        data = request.get_json()
        if not data or not all(key in data for key in ['role', 'creation_date', 'unp', 'name']):
            return jsonify({"status": "error", "message": "Invalid organization data provided"}), 400

        # Write the organization to the file
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)

        return jsonify({"status": "success", "message": "Organization created successfully"}), 200
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "An error occurred while creating the organization"}), 500



@app.route('/api/v1/credits/authz/<string:action>', methods=['GET'])
@app.route('/api/v1/deposits/authz/<string:action>', methods=['GET'])
@app.route('/api/v1/debitaccounts/authz/<string:action>', methods=['GET'])
@app.route('/api/v1/creditaccounts/authz/<string:action>', methods=['GET'])
@app.route('/api/v1/users/authz/<string:action>', methods=['GET'])
@app.route('/api/v1/organisations/authz/<string:action>', methods=['GET'])
@app.route('/api/v1/identities/authz/<string:action>', methods=['GET'])

def check_authorization(action):

    try:
        # Check if the token header is present
        token_header = request.headers.get('Users')
        if not token_header:
            raise ValueError("Token header not found")

        # Check if the client_id is present in the token header
        token_json = json.loads(token_header)
        client_id = token_json.get('client_id')
        if not client_id:
            raise ValueError("Client ID not found in token header")


        authorized = True

        # Return the appropriate response
        if authorized:
            return jsonify({"status": "success", "message": "authorized"}), 200
        else:
            return jsonify({"status": "error", "message": "not authorized"}), 403
    except ValueError as e:
        # Log the error
        app.logger.error(str(e))
        return jsonify({"status": "error", "message": str(e)}), 400
