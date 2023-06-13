from fastapi import Depends, HTTPException, status

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class UpdateUserResponce(AppModel):
    email: str


class DataToUpdataUser(AppModel):
    phone: str
    name: str
    city: str


@router.patch(
    "/auth/users/me"
)
def update_user(
    input: DataToUpdataUser,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service)
):
    svc.repository.update_user(
        jwt_data.user_id, input.dict()
    )
