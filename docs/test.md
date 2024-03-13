# Тестирование

## Тестирование на localhost

**Запускаем все тесты, выполняем команду на одном уровне с файлом manage.py** 
```python
    python manage.py test
``` 
**Для запуска отдельного тестового файла, выполняем команду на одном уровне с файлом manage.py**

```python
    python manage.py test <путь к файлу в котором хоти запустить тесты, например:goods.tests.test_admin>
``` 

## Тестирование на localhost с Docker-compose

**Запускаем все тесты, выполняем команду на одном уровне с файломами .gitignore, README и т.д.** 
```python
    docker-compose run --rm web-app sh -c "python manage.py test"
``` 

**Для запуска отдельного тестового файла, выполняем команду на одном уровне с файломами .gitignore, README и т.д.**
```python
    docker-compose run --rm web-app sh -c "python manage.py test <и путь к файлу, например:goods.tests.test_admin>"
``` 

## Запуск coverage на localhost
**Запускаем тесты с помощью coverage, выполняем команду на одном уровне с файлом manage.py** 
```python
    coverage run --source='.' manage.py test 
``` 

**Для запуска отдельного тестового файла с помощью coverage, выполняем команду на одном уровне с файлом manage.py**
```python
    coverage run --source='.' manage.py test <и путь к файлу, например:goods.tests.test_admin>
``` 
**Получаем отчёт от coverage, выполняем команду на одном уровне с файлом manage.py** 
```python
    coverage report 
``` 
**Получаем отчёт от coverage в формате html, выполняем команду на одном уровне с файлом manage.py** 
```python
    coverage html 
``` 

## Запуск coverage на localhost с Docker-compose
**Запускаем тесты с помощью coverage, выполняем команду на одном уровне с файломами .gitignore, README и т.д.** 
```python
    docker-compose run --rm web-app sh -c "coverage run --source='.' manage.py test"
``` 
**Получаем отчёт от coverage, выполняем команду на одном уровне с файломами .gitignore, README и т.д.** 
```python
    docker-compose run --rm web-app sh -c "coverage report"
``` 
**Получаем отчёт от coverage в формате html, выполняем команду на одном уровне с файломами .gitignore, README и т.д.** 
```python
    docker-compose run --rm web-app sh -c "coverage html"
``` 