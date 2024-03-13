# Запуск проекта

## Запуск на localhost

1) Инициализируем git

```python
    git init
``` 

2) Клонируем код из репозитория 

```python
    git clone https://github.com/SergeiSidorovv/zmey_shop.git
``` 
3) Создаём виртуальное окружение на уровне файлов .gitignore Dockerfile и т.д.
   
```python

python -m venv <название виртуального окружения, например: venv>

```
4) Активируем виртуальное окружение на уровне файлов .gitignore Dockerfile и т.д.

```python
    Windows: <название виртуального окружения>/Scripts/activate
```
```python
    Linux: source <название виртуального окружения>/bin/activate
``` 
5) Создаём файл .env на уровне файлов .gitignore, README и т.д.

6) Добавляем в файл .env переменные
```python
    NAME_DB = <ваше имя базы данных>
    USER_DB = <ваш пользователь базы данных>
    PASSWORD_DB = <ваш пароль базы данных>
    HOST = <ваш хост который будет указан в settings.py в переменной DATABASES>
    PORT = <ваш порт который будет указан в settings.py в переменной DATABASES> 
    SECRET_KEY = <ваш секретный ключ который будет указан в settings.py в переменной        SECRET_KEY (можно получить путём создания django проекта)> 

    ADMIN = <ваш url по которому будет открываться админ панель>
    PGADMIN_EMAIL = <ваш email для pgadmin>
    PGADMIN_PASSWORD = <ваш пароль для pgadmin>
``` 

7) Устанавливаем все зависимости (Чтобы установить все зависимости нужно быть на одном уровне с файлом requirements.txt)
   
```python
    pip install -r requirements.txt
``` 

8) Запускаем проект (Чтобы запустить необходимо находиться на одном уровне с файлом manage.py)
   
```python
    python manage.py runserver
``` 
___
## Запуск на localhost с Docker-compose

**Чтобы запустить проект с Docker-compose необходимо включить Docker Desktop!!!** 

1) Инициализируем git

```python
    git init
``` 

2) Клонируем код из репозитория 

```python
    git clone https://github.com/SergeiSidorovv/zmey_shop.git
``` 
3) Создаём виртуальное окружение на уровне файлов .gitignore Dockerfile и т.д.
   
```python

python -m venv <название виртуального окружения, например: venv>

```
4) Активируем виртуальное окружение на уровне файлов .gitignore Dockerfile и т.д.

```python
    Windows: <название виртуального окружения>/Scripts/activate
```
```python
    Linux: source <название виртуального окружения>/bin/activate
``` 
5) Создаём файл .env на уровне файлов .gitignore, README и т.д.

6) Добавляем в файл .env переменные
```python
    NAME_DB = <ваше имя базы данных>
    USER_DB = <ваш пользователь базы данных>
    PASSWORD_DB = <ваш пароль базы данных>
    HOST = <ваш хост который будет указан в settings.py в переменной DATABASES>
    PORT = <ваш порт который будет указан в settings.py в переменной DATABASES> 
    SECRET_KEY = <ваш секретный ключ который будет указан в settings.py в переменной        SECRET_KEY (можно получить путём создания django проекта)> 

    ADMIN = <ваш url по которому будет открываться админ панель>
    PGADMIN_EMAIL = <ваш email для pgadmin>
    PGADMIN_PASSWORD = <ваш пароль для pgadmin>
``` 

7) Устанавливаем все зависимости (Чтобы установить все зависимости нужно быть на одном уровне с файлом requirements.txt)
   
```python
    pip install -r requirements.txt
``` 

8) Меняем настройки в settings.py, ваш CACHES должен выглядеть так (меняем LOCATION)
```python
    CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://redis:6379",
        "OPTIONS": {
            "db": "0",
            "pool_class": "redis.BlockingConnectionPool",
        },
    }
}
``` 
9) Комментируем в файле requirements.txt строчку psycopg2
```python
    # psycopg2==2.9.9
``` 

10) Запускаем сборку образа на уровне с файлом docker-compose.yaml
```python
    docker-compose build
``` 

11) Запускаем контейнер на уровне с файлом docker-compose.yaml
 ```python
    docker-compose up
```    
12) Создаём миграции в проекте 
```python
    docker-compose run --rm web-app sh -c "python manage.py migrate"
```   
