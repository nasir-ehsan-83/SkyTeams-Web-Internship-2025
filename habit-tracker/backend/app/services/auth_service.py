from fastapi import HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 

from app.models.user import User
from app.core.security import verify

from app.core.oauth2 import create_access_token

async def login(user_credential: OAuth2PasswordRequestForm) :
    # get user from database
    existance_user = await User.find_one({"username": user_credential.username})

    # if specific user does not exist
    if not existance_user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Invalid user credential"
        )

    # else verify password

    if not await verify(user_credential.password, existance_user.password):
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Invalid password credential"
        )

    # create JWT token
    access_token = await create_access_token(data = {"user_id": existance_user.id})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }