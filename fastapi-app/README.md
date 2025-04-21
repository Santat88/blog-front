# Приложение FastAPI

Это бэкенг на FastAPI для тестового проекта блога. Оно предоставляет endpoints для управления постами и комментариями.

## Установка зависимостей

1. Создайте виртуальное окружение:
   ```
   python -m venv venv
   ```

2. Активируйте виртуальное окружение:
   - На Windows:
     ```
     venv\Scripts\activate
     ```
   - На macOS/Linux:
     ```
     source venv/bin/activate
     ```

3. Установите необходимые зависимости:
   ```
   pip install -r requirements.txt
   ```

## Использование

Чтобы запустить приложение FastAPI, выполните следующую команду:

```
uvicorn app.main:app --host 0.0.0.0 --port 8088 --reload
```

Вы можете получить доступ к документации API по адресу `http://localhost:8088/docs`.