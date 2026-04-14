from fastapi import HTTPException, Response, status
from pymongo.errors import DuplicateKeyError

from app.core.security import hash, verify
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User

async def create_user(user_in: UserCreate):
    exists_email = await User.find_one(User.email == user_in.email)

    if exists_email:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT, 
            detail = f"User with email: {user_in.email} already exists"
        )
    
    exists_username = await User.find_one(User.username == user_in.username)

    if exists_username:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT, 
            detail = f"User with username: {user_in.username} already exists"
        )
    
    try :
        # hash password before storing
        hashed_password = await hash(user_in.password)
        
        # create new user 
        new_user = User(
            name = user_in.name,
            username = user_in.username,
            email = user_in.email, 
            password = hashed_password
        )

        # add new user to the database
        return await new_user.insert()
    
    except DuplicateKeyError:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Data conflict: The provided credentials are already in use."
        )

async def get_user_by_email(user_in_email: str) -> User:
    user = await User.find_one(User.email == user_in_email)

    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"User with email: {user_in_email} does not exist"
        )
    
    return user

async def update_user_by_email(user_in_email: str, user_update: UserUpdate) -> User:
    user = await User.find_one(User.email == user_in_email)

    if not user_update:
        return user
    
    update_data = user_update.model_dump(exclude_unset = True, exclude_none = True)
    
    if "password" in update_data:
        update_data["password"] = await hash(update_data["password"])

    # also you can use await user.set(update_data)
    await user.update({ "$set" : update_data})
    user = await User.get(user.id)
    return user

async def delete_user_by_id(user_in_email):
    # find the user from database
    user = await User.find_one(User.email == user_in_email)

    # if user does not exist
    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"User with email: {user_in_email} does not exists"
        )
    # delete the user from database
    await user.delete()

    return Response(status_code = status.HTTP_204_NO_CONTENT)