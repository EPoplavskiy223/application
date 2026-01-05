# Домашняя работа № 22

## Приложение создано для запуска сервера на локальном компьютере 

### Запуск приложения:
1. Перейти в переменное окружение `.venv`
2. Загрузить все зависимости из [pyproject.toml](pyproject.toml)
3. Запустить в терминале  `python manage.py runserver`


### Что сделано:
1. Создан `Django-проект`.
2. Создано приложение `catalog`.
3. Приложение `catalog` зарегистрировано в [`INSTALLED_APPS`](config/settings.py).
4. Создан файл [urls.py](catalog/urls.py) в приложении [`catalog`](catalog).
5. Контроллер рендерит шаблоны функцией [render](catalog/views.py).
6. В основном URL-файле использован [include](config/urls.py) для подключения URL-файла приложения [`catalog`](catalog).