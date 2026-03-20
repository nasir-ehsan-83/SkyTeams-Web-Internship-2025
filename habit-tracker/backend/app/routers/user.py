from fastapi import APIRouter, status
from backend.app.schemas.user import UserCreate, UserOut
from backend.app.services.user_service import create_user

router = APIRouter(
    prefix = '/user',
    tags = ['User']
)

@router.post('/', response_model = UserOut)
async def create_new_user(user_in: UserCreate):
    
    return await create_user(user_in)