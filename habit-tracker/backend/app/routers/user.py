from fastapi import APIRouter, status

from app.models.user import User
from app.schemas.user import UserCreate, UserOut, UserUpdate
from app.services.user_service import (create_user, get_user_by_email, update_user_by_email, delete_user_by_id)

router = APIRouter(
    prefix = '/user',
    tags = ['User']
)

@router.post('/', response_model = UserOut)
async def create_new_user(user_in: UserCreate) -> User:
    
    return await create_user(user_in)

@router.get('/{email}', response_model = UserOut)
async def get_user_id(email: str) -> User:
    print(email)
    return await get_user_by_email(email)

@router.put('/email/{email}', response_model = UserOut)
async def update_user(email: str, user_update: UserUpdate) -> User :
    print(user_update)
    return await update_user_by_email(email, user_update)

@router.delete('/email/{email}')
async def delete_user(email: str):

    return await delete_user_by_id(email)