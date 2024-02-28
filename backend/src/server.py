import uvicorn
from fastapi import FastAPI
from .router import health
from .config import API_PORT

app = FastAPI()
app.include_router(health.router)


def main() -> None:
    """Entrypoint to invoke when this module is invoked on the remote server."""
    # See the official documentations on how "0.0.0.0" makes the service available on
    # the local network - https://www.uvicorn.org/settings/#socket-binding
    uvicorn.run("server:app", host="0.0.0.0", port=API_PORT, reload=True)


if __name__ == "__main__":
    main()
