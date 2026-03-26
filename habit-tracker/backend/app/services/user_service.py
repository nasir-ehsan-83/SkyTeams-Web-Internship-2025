from app.core.security import hash, verify
from app.schemas.user import UserCreate
from app.models.user import User

async def create_user(user_in: UserCreate):
    
    new_user = User(
        email = user_in.email, 
        password = hash(user_in.password)   # hash the user.password before storing
    )
    return await new_user.insert()
