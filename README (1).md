# TechStore 🛒

Каталог техники на Django — учебный проект, сделанный за 12 дней обучения с нуля до деплоя.

## 🚀 Стек

- **Python 3.13** + **Django 5.2**
- **Django REST Framework** — REST API
- **JWT** — аутентификация через токены
- **SQLite** — база данных
- **Docker** — контейнеризация
- **Render** — деплой

## ⚙️ Функционал

- 📋 Каталог ноутбуков, телефонов и автомобилей
- 🔍 Поиск по названию и бренду
- ➕ CRUD — добавление, редактирование, удаление
- 🔐 Регистрация и вход
- 🛡️ Защита страниц через `@login_required`
- 🌐 REST API с JWT аутентификацией

---

## 📅 История обучения — 12 дней

### День 1 — Основы Django
- Установил Django, создал проект `techstore`
- Разобрался с MTV архитектурой (Model, Template, View)
- Создал приложение `laptops`
- Настроил URL-routing и первый View
- Сделал HTML-шаблон с карточками ноутбуков

### День 2 — Models и База данных
- Создал модель `Laptop` с полями name, brand, price, ram
- Сделал миграции (`makemigrations` + `migrate`)
- Подключил Admin-панель и зарегистрировал модель
- Создал суперпользователя
- Подключил `Laptop.objects.all()` — данные из БД на странице

### День 3 — Detail View и динамические URL
- Сделал страницу отдельного ноутбука `/laptops/<id>/`
- Разобрался с динамическими URL и `get_object_or_404`
- Добавил навигацию между страницами

### День 4 — Поиск и фильтрация
- Сделал поиск по названию и бренду через GET-запросы
- Разобрался с `request.GET.get()` и `filter(icontains=)`
- Нашёл и исправил баг самостоятельно

### День 5 — Django Forms
- Создал `forms.py` с `ModelForm`
- Сделал форму добавления ноутбука прямо с сайта
- Разобрался с POST-запросами, `csrf_token`, валидацией
- Добавил `redirect()` после сохранения

### День 6 — Update и Delete (полный CRUD)
- Добавил редактирование ноутбука через форму
- Сделал страницу подтверждения удаления
- Завершил полный CRUD (Create, Read, Update, Delete)
- Нашёл и исправил несколько багов самостоятельно

### День 7 — Аутентификация
- Создал приложение `accounts`
- Сделал регистрацию через `UserCreationForm`
- Сделал вход через `AuthenticationForm`
- Добавил выход и отображение имени пользователя в шапке

### День 8 — Защита страниц
- Подключил декоратор `@login_required`
- Настроил `LOGIN_URL` и умный редирект через `?next=`
- Защитил create, update, delete от неавторизованных

### День 9 — Django REST Framework
- Установил DRF, создал сериализатор `LaptopSerializer`
- Сделал API эндпоинты через `ListCreateAPIView` и `RetrieveUpdateDestroyAPIView`
- Настроил `IsAuthenticatedOrReadOnly`
- Открыл Browsable API в браузере

### День 10 — JWT аутентификация
- Установил `djangorestframework-simplejwt`
- Настроил JWT в `settings.py`
- Получил access и refresh токены через Python скрипт
- Сделал авторизованный запрос к API с токеном в заголовке

### День 11 — Docker
- Установил Docker Desktop, включил виртуализацию в BIOS
- Создал `Dockerfile` и `docker-compose.yml`
- Собрал и запустил проект в контейнере
- Теперь запуск одной командой: `docker-compose up`

### День 12 — Деплой
- Загрузил проект на GitHub
- Установил gunicorn, создал `Procfile` и `.gitignore`
- Задеплоил на Render через Docker
- Сайт доступен в интернете 🌍

---

## 📦 Установка

```bash
git clone https://github.com/Amin-html/techstore.git
cd techstore
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Открой в браузере: `http://127.0.0.1:8000/laptops/`

## 🐳 Запуск через Docker

```bash
docker-compose up --build
```

## 🌍 API endpoints

| Метод | URL | Описание |
|---|---|---|
| GET | `/laptops/api/` | Список ноутбуков |
| POST | `/laptops/api/` | Добавить ноутбук |
| GET | `/laptops/api/<id>/` | Один ноутбук |
| PUT | `/laptops/api/<id>/` | Обновить |
| DELETE | `/laptops/api/<id>/` | Удалить |
| POST | `/api/token/` | Получить JWT токен |
| POST | `/api/token/refresh/` | Обновить токен |

## 👤 Автор

**Amin** — начал с нуля, закончил с рабочим проектом за 12 дней 💪
