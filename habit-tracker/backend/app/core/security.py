from passlib.context import CryptContext

password_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

async def hash(password: str) -> str:
    password_bytes = password.encode("utf-8")[:72]
    password_truncated = password_bytes.decode("utf-8", errors = "ignore")

    return await password_context.hash(password_truncated)

async def verify(plain_password: str, hashed_password: str) -> bool:
    if not hashed_password:
        return False
    
    return await password_context.verify(plain_password, hashed_password)