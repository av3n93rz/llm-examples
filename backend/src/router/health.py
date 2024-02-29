from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthCheck(BaseModel):
    status: str


@router.get("/health")
def health_check() -> HealthCheck:
    return HealthCheck(status="OK")
