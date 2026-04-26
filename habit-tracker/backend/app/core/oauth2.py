from fastapi.concurrency import run_in_threadpool
from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta
from typing import Dict

from app.schemas.token import TokenData
from app.core.confing import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

async def create_access_token(data: Dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})

    encoded_jwt = await run_in_threadpool(
        jwt.encode,
        to_encode,
        SECRET_KEY,
        algorithm = ALGORITHM
    )

    return encoded_jwt

async def verify_access_token(token: str, credentials_exception):
    try:
        payload = await run_in_threadpool(
            jwt.decode,
            token,
            SECRET_KEY,
            algorithm = [ALGORITHM]
        )

        id: str = payload.get("user_id")
        role: str = payload.get("role")

        if id is None or role is None:
            raise credentials_exception
        
        token_data = TokenData(id = str(id), role = role)

    except JWTError:
        raise credentials_exception
    
    return token_data