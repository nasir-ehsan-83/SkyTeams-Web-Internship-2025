from fastapi import HTTPException, Response, status
from pymongo.errors import DuplicateKeyError
from datetime import datetime, timezone

from app.core.security import hash
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User

# create new user and add to database
async def create_user(user: UserCreate):
    # get user by email from database
    exists_email = await User.find_one({"email": user.email})

    # if user already exist by specific email
    if exists_email:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT, 
            detail = f"User with email: {user.email} already exists"
        )
    
    # get user by username from database
    exists_username = await User.find_one({"username": user.username})

    # if user already exists by specific username 
    if exists_username:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT, 
            detail = f"User with username: {user.username} already exists"
        )
    
    # else 
    try :
        # hash password before storing
        hashed_password = await hash(user.password)
        
        # create new user 
        new_user = User(
            name = user.name,
            username = user.username,
            email = user.email, 
            password = hashed_password
        )

        # add new user to the database
        return await new_user.insert()
    
    # exception by duplicate email or username
    except DuplicateKeyError:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Data conflict: The provided credentials are already in use."
        )

# get all users from database by admin access
async def get_all_users():
    # get all users from database
    users = await User.find_all().to_list()

    return users

# get user's information by email and owner access
async def get_user_by_email(email: str, current_user: int) -> User:
    # get user from database 
    user = await User.find_one({"email": email, "owner_id": int(current_user.id), "status": "active"})

    # if user does not exist by specific email and owner_id
    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"User with email: {email} does not exist"
        )
    
    # return user information
    return user

# update user's information by email and owner access
async def update_user_by_email(user_update: UserUpdate, current_user: int) -> User:
    # get user from database
    user = await User.find_one({"email": user_update.email, "owner_id": current_user.id, "status": "active"})

    # if user does not exist 
    if not user_update:
        return user
    
    # delete undefined or null values
    update_data = user_update.update_data.model_dump(exclude_unset = True, exclude_none = True)
    
    # if password is updated thus hash updated password
    if "password" in update_data:
        update_data["password"] = await hash(update_data["password"])

    # add owner_id and updated_at to the data
    update_data.update({"updated_at": datetime.now(timezone.utc), "owner_id": int(current_user.id)})

    # add updated information to the database
    await user.update({ "$set" : update_data})

    # get user by updated infromation
    user = await User.get(user.id)
    return user

# delete user from database
async def delete_user_by_email(email: str, current_user: int):
    # find the user from database
    user = await User.find_one({"email": email, "owner_id": int(current_user.id), "status": "active"})

    # if user does not exist
    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"User with email: {email} does not exists"
        )
    # change the user'status to deleted 
    await user.update({"$set": {"status": "deleted"}})

    return Response(status_code = status.HTTP_204_NO_CONTENT)