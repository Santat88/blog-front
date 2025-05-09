from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, MetaData, select, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager

# Используем SQLite
DATABASE_URL = "sqlite:///./test.db"

# Создаём подключение к SQLite
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Определяем таблицу
posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String, nullable=False),
    Column("content", String, nullable=False),
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Создание таблиц при старте приложения
    metadata.create_all(bind=engine)
    print("Таблицы созданы")

    # Наполнение базы данных начальными данными
    with engine.connect() as conn:
        existing_posts = conn.execute(select(posts)).fetchall()
        print(f"Существующие записи: {existing_posts}")
        if not existing_posts:  # Если таблица пуста
            conn.execute(posts.insert(), [
                {"id": 1, "title": "Первый пост", "content": "Это содержимое первого поста. Добро пожаловать в наш блог!"},
                {"id": 2, "title": "Второй пост", "content": "Это содержимое второго поста. Здесь мы делимся интересными фактами."},
                {"id": 3, "title": "Третий пост", "content": "Это содержимое третьего поста. Следите за нашими обновлениями!"},
                {"id": 4, "title": "Четвертый пост", "content": "Это содержимое четвертого поста. Мы рады вашим комментариям!"},
                {"id": 5, "title": "Пятый пост", "content": "Это содержимое пятого поста. Спасибо, что читаете наш блог!"},
            ])
            conn.commit()
            print("Данные добавлены")
    yield

app = FastAPI(lifespan=lifespan)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/posts")
def get_posts():
    with engine.connect() as conn:
        result = conn.execute(select(posts)).mappings().fetchall()
        print(f"Полученные записи: {result}")
        return [dict(row) for row in result]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8088, log_level="info", reload=True)