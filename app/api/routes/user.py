from typing import Annotated

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from app.application.dto.user import UserResponse
from app.application.use_cases.user import GetAllUsersUseCase
from app.infrastructure.container import Container


router = APIRouter(tags=["Users"])


@router.get("/", response_model=UserResponse)
@inject
async def get_all_users(
    get_all_users_use_case: Annotated[
        GetAllUsersUseCase, 
        Depends(lambda: Container.get_all_users_use_case),
    ],
):
    return await get_all_users_use_case()