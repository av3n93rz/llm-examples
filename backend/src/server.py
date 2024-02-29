import uvicorn
from fastapi import FastAPI
from src.router import health, conversation
from src.config import API_PORT

app = FastAPI()
app.include_router(health.router)
app.include_router(conversation.router)


def main() -> None:
    uvicorn.run("server:app", host="0.0.0.0", port=API_PORT, reload=True)


if __name__ == "__main__":
    main()
