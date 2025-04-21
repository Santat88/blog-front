from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники. Для безопасности укажите конкретные домены.
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

@app.get("/api/v1/posts")
def get_posts():
    return [
        {
            "id": 1,
            "title": "First Post",
            "content": "This is the content of the first post.",
            "comments": [
                {"id": 1, "author": "Alice", "content": "Great post!"},
                {"id": 2, "author": "Bob", "content": "Thanks for sharing!"}
            ]
        },
        {
            "id": 2,
            "title": "Second Post",
            "content": "This is the content of the second post.",
            "comments": [
                {"id": 3, "author": "Charlie", "content": "Interesting read."},
                {"id": 4, "author": "David", "content": "I learned something new!"}
            ]
        }
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8088, log_level="info", reload=True)