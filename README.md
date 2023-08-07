# Тестовое задание

Это тестовое задание для веб-приложения "Курс валют", созданного на Django. Приложение отображает текущие курсы рубля к доллару и евро и позволяет пользователям выбрать конкретный день (сегодня, вчера или позавчера), чтобы увидеть курс за этот день. В приложение также включены модульные тесты для функций вывода и обновления курсов валют.

### Чтобы запустить веб-приложение "Курс валют" локально, выполните следующие действия:

#### Необходимые условия

- Python 3.8 и выше
- Redis
- Docker и Docker compose (опционально, для альтернативного развертывания)

#### Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/NurlanEmilbekuulu/currency-exchange-app.git
```

2. Измените каталог на папку проекта:

```
cd currency-exchange-app
```

3. Создайте `.env` файл с таким данными

```
DEBUG=True
SECRET_KEY="3cb97653047d99a2ffb1b880ee5a472d7adf3842c5542ae4d06ef9f634e87b75"
ALLOWED_HOSTS='["localhost"]'

CELERY_BROKER_URL="redis://localhost:6379/0"
CELERY_RESULT_BACKEND="redis://localhost:6379/0"

EXCHANGE_API_TOKEN="a0d1e2958c6a5ed2e7dbbb0b"
```

4. Установите необходимые зависимости:

```
pipenv install
```

#### Запуск приложения

```
python manage.py runserver
```

Приложение будет доступно по адресу http://localhost:8000/

#### Запуск тестов

Чтобы запустить модульные тесты для приложения, выполните следующую команду:

```
python manage.py test
```

### Развертывание (Docker compose)

Приложение также можно развернуть с помощью Docker и Docker-compose. Убедитесь, что на вашей машине установлен Docker и Docker-compose.

1. Измените каталог на папку проекта:

```
cd currency-exchange-app
```

2. Поменяйте `.env` file

```
DEBUG=True
SECRET_KEY="3cb97653047d99a2ffb1b880ee5a472d7adf3842c5542ae4d06ef9f634e87b75"
ALLOWED_HOSTS='["localhost"]'

CELERY_BROKER_URL="redis://redis:6379/0"
CELERY_RESULT_BACKEND="redis://redis:6379/0"

EXCHANGE_API_TOKEN="a0d1e2958c6a5ed2e7dbbb0b"
```

3. Запустите docker-compose

```
docker-compose up -d
```

---

Для получения курса валют я использовал сервис https://app.exchangerate-api.com/. Токен может быть не валидным.
