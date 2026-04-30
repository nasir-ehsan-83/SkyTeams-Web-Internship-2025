from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.oauth2 import verify_access_token

oauth2_schema = OAuth2PasswordBearer(tokenUrl = 'login')

async def get_current_user(token: str = Depends(oauth2_schema)):
    credential_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED, 
        detail = "Could not validate credentials", 
        headers = {"WWW-Authenticate": "bearer"}
    )

    return await verify_access_token(token, credential_exception)