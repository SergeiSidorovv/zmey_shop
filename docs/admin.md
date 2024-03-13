# Работа с админ панелью

## Запуск админ панели на localhost

**Создаём суперпользователя, выполняем команду на одном уровне с файлом manage.py** 
```python
    python manage.py createsuperuser
``` 

## Запуск админ панели на localhost с Docker-compose
**Создаём суперпользователя, выполняем команду на одном уровне с файломами .gitignore, README и т.д.**
```python
    docker-compose run --rm web-app sh -c "python manage.py createsuperuser"
``` 