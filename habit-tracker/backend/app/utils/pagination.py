from typing import Optional, Tuple

def paginate(page: Optional[int] = 1, limit: Optional[int] = 10) -> Tuple[int, int]:
    skip: int = (page - 1) * limit
    return skip, limit