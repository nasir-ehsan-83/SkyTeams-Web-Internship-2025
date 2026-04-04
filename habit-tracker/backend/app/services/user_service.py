from fastapi import HTTPException, status
from app.core.security import hash, verify
from app.schemas.user import UserCreate
from app.models.user import User

async def create_user(user_in: UserCreate):
    
    new_user = User(
        email = user_in.email, 
        password = hash(user_in.password)   # hash the user.password before storing
    )
    return await new_user.insert()

async def get_user_by_id(user_id: int):
    user = await User.objects().filter(id = user_id).first()

    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with id: {user_id} does not exist")
    
    return user