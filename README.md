### Homework 14
1. Создать новый репозиторий **dos14-family_name-git-flow**
2. Создать 2 ветки **master develop**
3. Cоздать ветку **feature-hw-14**
4. Добавит информацию о репозитории в README.md
5. Сделать pull request в develop (после апрува
@ggramal смерджить) (cмерджить все ветки с
предыдущими домашками*)
6. Сделать из **develop** *release-v0.0.1*
7. Cмерджить в master и сделать тэг *v0.0.1*
8. Удалить **release-v0.0.1**

### Homework 15
1. Установить *python 3.11* через **pyenv**
2. Создать проект с помощью **poetry**
3. Добавить группу зависимостей **dev**, сделать её опциональной и добавить **black** пакет
4. Создать **main.py** с кодом - если перменная среды SHELL равна ‘/bin/bash’ напечатать в консоль Greetings bash если другое значение Hello <значение переменной среды>
5. Сделать **black ./**
5. Закоммитить все файлы (*pyptoject.toml*, *poetry.lock*, *main.py* etc) в feature ветку, слить ее с **develop** (без апрува)
6. По готовности сделать пулл реквест в master с апрувером @ggramal, отписаться в тг канале

### HOMEWORK16
1. База данных отдаёт 3 массива cтрок с информацией о пользователях. Все строки имеют вид -
"<id>_<атрибут пользователя>". Нужно обработать эти данные и создать массив из словарей
2. [
{id: "<some_id>", first_name: "<some_first_name>", last_name: "<some_last_name>", date_of_birth:<some_age>}
{id: "<some_id_2>", first_name: "<some_first_name_2>", last_name: "<some_last_name_2>", date_of_birth:
<some_age_2>}
]
3. вывести на экран
["2_Комарова", "5_Леонова", "10_Фадеева", "6_Соколова", "4_Назаров", "7_Дроздова", "8_Гордеева", "3_Смирнов",
"9_Николаев", "1_Калашников"]
["2_Варвара", "6_Алина", "9_Владислав", "4_Владислав", "5_Анастасия", "3_Антон", "1_Марк", "8_Амелия",
"7_Василиса", "10_София", ]
["2_Олеговна", "1_Анатольевич", "3_Эдуардович", "5_Валерьевна", "7_Игоревна", "6_Васильевна", "9_Иосифович",
"8_Александровна", "10_Игоревна", "4_Владимирович"]
['1_1985', '3_1978', '4_2001', '10_1982', '5_1970', '6_1990', '8_1963', '7_2004', '2_1996', '9_1966']

### HOMEWORK17
1. Прочитать информацию о пользователях из файлов yaml,csv 
2. Из полученных данных создать список из словарей с атрибутами пользователей *{"id": <id>, "first_name": <first_name>, "last_name": <last_name>, "fathers_name":   <fathers_name>, "date_of_birth": <data_of_birth>}*
3. Создать функцию для расчёта возраста пользователя 
4. Прогоняем на список через функцию расчёта возраста и добавляем новый атрибут age каждому словарю 
5. Записываем полученные данные в **users.json файл** 
6. Создать функцию для добавления пользователей
7. Функия должна принимать все атрибуты пользователя кроме id *(first_name, last_name, fathers_name, date_of_birth)* 
8. **id** вычисляется в функции, как наибольшее id пользователя (из списка) +1 
9. age вычисляется на основании функции **расчёта возраста пользователя** 
10. на основании полученных и вычесленных аттрибутов добавляем новый элемент в наш список словарей
11. записываем полученные данные в users.json файл
  
 ### Homework 18
 1. Создать класс **Permissions**
    - cоздать boolean свойства на чтение запись - *create,read,update,delete*
 2. Cоздать класс **Role**
    - создать свойство только на чтение строку name
    - cоздать свойство role которое является словарём, где ключ имена наших классов выполняющие бизнес логику **(Credit,Deposit,DebitAccount,CreditAccount,User,Organisation,Identity)**, а значение объекты *Permissions*
    - Либо класс Role должен принимать как ключ имена выше указанных классов и выдовать в качестве значений объекты **Permissions**
     >> a = Role("default",**dict_with_permissions)
     >> a.name
     default
     >> a["Credit].create
     False
     >> a["DebitAccount"].update
     False
3. Создать класс **Entity**
    - Создать свойство только на чтение - **entity_id** (оно должно быть int)
    - Cоздать свойcтво на чтение/запись - **role** с типом **Role**
4. Создать класс **User**
    - Унаследоваться от **Entity**
    - Добавить свойства только на чтение *first_name, last_name, fathers_name, date_of_birth*
    - Добавить свойство только на чтение *age*, которое высчитывается из *date_of_birth*
5. Создать класс **Organisation**
    - Унаследоваться от **Entity**
    - Добавить свойства *creation_date, unp, name*
6. Создать класс **App**
    - Унаследоваться от **Entity**
    - Добавить свойства *name*
7. Прочитать данные из файлов *users.json, apps.yaml, roles.yaml* и создать на основании их объекты
8. В функции *сreate_user* из предыдущего задания создаём не словарь а объект
  
  ### Homework 19
* Переименовываем entity_id в client_id во всех классах
* Переименовываем class Entity в Client
* Прочитать данные из файлов users.json, apps.yaml, roles.yaml и создать на основании их объекты 
* Устанавливаем Flask через poetry
* Наш сервис должен иметь следующий http интерфейс
  * GET /api/v1/users/<client_id> - получить данные о пользователе
    * Перед тем как получить данные посмотреть есть ли у пользователя права на чтение users
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
    * Если не нашли пользователя с таким client_id то возвращаем {"status": "error", "message": f"No user with id = {client_id}"}
 * GET /api/v1/organisations/<client_id> - получить данные об организации 
    * Перед тем как получить данные посмотреть есть ли у пользователя права на чтение organisations
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
    * Если не нашли организацию с таким client_id то возвращаем {"status": "error", "message": f"No organisation with id = {client_id}"}
  * GET /api/v1/users - получить данные о всех пользователях
    * Перед тем как получить данные посмотреть есть ли у пользователя права на чтение users
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
 * GET /api/v1/organisations - получить данные о всех организациях
    * Перед тем как получить данные посмотреть есть ли у пользователя права на чтение organisations
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
  * PUT /api/v1/users - создать пользователя используя {"first_name": "...", "role": "...", "last_name": "...", "fathers_name": "...", "date_of_birth": "..."}
    * Перед тем как получить данные посмотреть есть ли у пользователя права на запись users
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
    * Пишем в файл users.json
  * PUT /api/v1/organisations - создать организацию используя {"role": "", "creation_date": "", "unp": "", "name": ""}
    * Перед тем как получить данные посмотреть есть ли у пользователя права на запись organisations
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
    * Пишем в файл users.json
  * GET /api/v1/credits/authz/{create,read,update,delete}
  * GET /api/v1/deposits/authz/{create,read,update,delete}
  * GET /api/v1/debitaccounts/authz/{create,read,update,delete}
  * GET /api/v1/creditaccounts/authz/{create,read,update,delete}
  * GET /api/v1/users/authz/{create,read,update,delete}
  * GET /api/v1/organisations/authz/{create,read,update,delete}
  * GET /api/v1/identities/authz/{create,read,update,delete}
    * Для каждого из этих URI
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
      * Если есть 200 и {"status": "success", "message": "authorized"}
        * Если нет или, что то пошло не так то  403 {"status": "error", "message": "not authorized"}
  
  
