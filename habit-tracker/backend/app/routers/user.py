from fastapi import APIRouter
from typing import List

from app.models.user import User
from app.schemas.user import UserCreate, UserPrivateOut, UserAdminOut, UserUpdate
from app.services.user_service import (
    create_user, 
    get_all_users,
    get_user_by_email, 
    update_user_by_email, 
    delete_user_by_id
)

router = APIRouter(
    prefix = '/users',
    tags = ['User']
)

@router.post('/', response_model = UserPrivateOut)
async def create_new_user(user_in: UserCreate) -> User:
    
    return await create_user(user_in)

@router.get('/', response_model = List[UserAdminOut])
async def get_users() -> User:

    return await get_all_users()

@router.get('/email', response_model = UserPrivateOut)
async def get_user_email(email: str) -> User:

    return await get_user_by_email(email)

@router.put('/email', response_model = UserPrivateOut)
async def update_user(user_data: UserUpdate) -> User :
    return await update_user_by_email(user_data)

@router.delete('/email')
async def delete_user(email: str):

    return await delete_user_by_id(email)