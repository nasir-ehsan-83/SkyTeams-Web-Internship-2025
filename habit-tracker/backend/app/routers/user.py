from fastapi import APIRouter, status
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import (create_user, get_user_by_id)

router = APIRouter(
    prefix = '/user',
    tags = ['User']
)

@router.post('/', response_model = UserOut)
async def create_new_user(user_in: UserCreate):
    
    return await create_user(user_in)

@router.get('/{id}', response_model = UserOut)
async def get_user_id(user_id: int):
    
    return await get_user_by_id(user_id)