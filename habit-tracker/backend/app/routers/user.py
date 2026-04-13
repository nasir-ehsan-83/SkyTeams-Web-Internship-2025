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
    
    return await get_user_by_email(email)

@router.put('email/{email}', response_model = UserUpdate)
async def update_user(email: str, updated_user: UserUpdate) -> User :

    return await update_user_by_email(email, updated_user)

@router.delete('/email/{email}', response_model = status.HTTP_204_NO_CONTENT)
async def delete_user(email: str):

    return await delete_user_by_id(email)