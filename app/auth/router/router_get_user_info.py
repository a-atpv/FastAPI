from typing import Any

from fastapi import Depends
from pydantic import Field

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class GetMyAccountInfoResponse(AppModel):
    id: Any = Field(alias="_id")
    email: str
    phone: str
    name: str
    city: str


@router.get("/auth/users/me", response_model=GetMyAccountInfoResponse)
def get_my_account_info(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    user = svc.repository.get_user_by_id(jwt_data.user_id)
    return user
