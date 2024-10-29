from fastapi import APIRouter
from dishka.integrations.fastapi import DishkaRoute, FromDishka

from app.application.dto.user import UserResponse
from app.application.use_cases.user import GetAllUsersUseCase


router = APIRouter(tags=["Users"], route_class=DishkaRoute)


@router.get("/")
async def get_all_users(
    get_all_users_interactor: FromDishka[GetAllUsersUseCase],
) -> list[UserResponse]:
    return await get_all_users_interactor()