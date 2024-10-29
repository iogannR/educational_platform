from uuid import UUID
from fastapi import APIRouter
from dishka.integrations.fastapi import DishkaRoute, FromDishka

from app.application.dto.user import UserCreate, UserResponse
from app.application.use_cases.user import (
    CreateUserUseCase,
    GetAllUsersUseCase,
    GetUserByIdUseCase,
    GetUserByEmailUseCase,
    DeleteUserUseCase,
)


router = APIRouter(tags=["Users"], route_class=DishkaRoute)


@router.post("/create")
async def create_user(
    request: UserCreate,
    create_user_interactor: FromDishka[CreateUserUseCase],
) -> UserResponse:
    return await create_user_interactor(request)


@router.get("/")
async def get_all_users(
    get_all_users_interactor: FromDishka[GetAllUsersUseCase],
) -> list[UserResponse]:
    return await get_all_users_interactor()


@router.get("/get_by_id")
async def get_user_by_id(
    id_: UUID,
    get_user_by_id_interactor: FromDishka[GetUserByIdUseCase],
) -> UserResponse | None:
    return await get_user_by_id_interactor(id_)


@router.get("/{email}")
async def get_user_by_email(
    email: str,
    get_user_by_email_interactor: FromDishka[GetUserByEmailUseCase],
) -> UserResponse | None:
    return await get_user_by_email_interactor(email)


@router.delete("/delete")
async def delete_user(
    id_: UUID, 
    delete_user_interactor: FromDishka[DeleteUserUseCase],
) -> None:
    return await delete_user_interactor(id_)