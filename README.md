# Todo_site

# Установка (windows):
1) Клонировать репозиторий 
git clone
2) Создать виртуальное окружение
python -m venv venv
3) Активировать виртуальное окружение
./venv/Scripts/activate.ps1
4) Установить необходимые пакеты
pip instal -r requerements.txt
5) Отредактирвать settings.py 
Вставить свой SECRET_KEY
6) Запустить миграции
python manage.py migrate
python manage.py makemigrations
7) Запустить сервер 
python manage.py runserver

