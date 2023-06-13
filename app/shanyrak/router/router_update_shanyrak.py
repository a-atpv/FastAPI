from typing import Any

from fastapi import Depends, Response
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service

from . import router


class DataToUpdataShanyrak(AppModel):
    type: str
    price: int
    city: str
    address: str
    area: int
    rooms_count: int
    description: str


@router.patch(
    "/shanyraks/{id}"
)
def update_shanyrak(
    input: DataToUpdataShanyrak,
    shanyrak_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service)
):
    svc.repository.update_shanyrak(
        shanyrak_id, input.dict()
    )

