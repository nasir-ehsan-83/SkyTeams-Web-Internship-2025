from backend.app.crud.user_crud import add_user
from backend.app.core.security import hash, verify
from backend.app.schemas.user import UserCreate

async def create_user(user: UserCreate):
    # hash the user.password before storing
    user.password = hash(user.password)

    return await add_user(user)
