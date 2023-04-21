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
