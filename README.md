# API для yatube

## Описание
Можем постить записи\комментарии.
Реализована система подписок

## Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)

##### Реализован функционал дающий возможность:
* Подписываться на пользователя.
* Просматривать, создавать новые, удалять и изменять посты.
* Просматривать и создавать группы.
* Комментировать, смотреть, удалять и обновлять комментарии.
* Фильтровать по полям.

#### К API есть документация по адресу `http://localhost:8000/redoc/`
## Установка 
Клонируем репозиторий на локальную машину:

```$ git clone https://github.com/DariaKalinichenko/api_final_yatube.git```

 Создаем виртуальное окружение:
 
 ```$ python -m venv venv```
 
 Устанавливаем зависимости:

```$ pip install -r requirements.txt```

Создание и применение миграций:

```$ python manage.py makemigrations``` и ```$ python manage.py migrate```

Запускаем django сервер:

```$ python manage.py runserver```
