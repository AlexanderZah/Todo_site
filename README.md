# Todo_site

## Установка на windows:
1) Клонировать репозиторий 
```sh
git clone https://github.com/AlexanderZah/Todo_site.git
```
2) Создать виртуальное окружение
```sh
python -m venv venv
```

3) Активировать виртуальное окружение
```sh
./venv/Scripts/activate.ps1
```

4) Установить зависимости
```sh
pip install -r requirements.txt
```

5) Отредактирвать settings.py 
```sh
Вставить свой SECRET_KEY
```

6) Запустить миграции
```sh
python manage.py migrate
python manage.py makemigrations
```

7) Запустить сервер 
```sh
python manage.py runserver
```


