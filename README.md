# Table Reservations API

**Table Reservations** — RESTful API для бронирования столиков в ресторане. Реализовано с использованием **Flask**, **SQLAlchemy**, **Pydantic**, и FastAPI-стиля валидаций.

## 📁 Структура проекта

```
table_reservations/
├── app/
│    ├── core/            # Настройки, utils, config
│    ├── models/          # SQLAlchemy модели
│    ├── routers/         # Роутеры в стиле FastAPI
│    ├── schemas/         # Pydantic схемы
│    ├── servies/         # Логика валидаций и операций
│    └── main.py          # Точка входа
├── tests/                # Pytest тесты
├── migrations/           # Alembic миграции
└── requirements.txt      # Зависимости
```

## 🚀 Запуск проекта

### 1. Клонируй репозиторий

```bash
git clone https://github.com/yourusername/table_reservations.git
cd table_reservations
```

### 2. Активируй виртуальное окружение

Windows:

```bash
python -m venv venv
sourse venv/Scripts/activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установи зависимости

```bash
pip install -r requirements.txt
```

### 4. Запусти сервер

```bash
uvicorn app.main:app --reload
```

API будет доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Swagger-документация: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🐳 Запуск с Docker

```bash
docker build -t table_reservations .
docker run -d -p 8000:8000 table_reservations
```

Либо через `docker-compose`:

```bash
docker-compose up --build
```

---

## 🧪 Запуск тестов

Обычный запуск:

```bash
pytest tests/
```

Аварийный запуск (если есть проблемы с импортами):

```bash
PYTHONPATH=C:/FLASK_API/table_reservations pytest
```

---


## ⚙️ Используемые технологии

- **Flask**
- **SQLAlchemy**
- **Pydantic**
- **Uvicorn**
- **pytest**
- **flake8**
- **Alembic**
- **Docker**

---
