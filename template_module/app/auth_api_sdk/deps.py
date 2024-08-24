from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import requests
from app.config import auth_endpoint

from app.auth_api_sdk.schemas.user import RoleInDB, UserResponseRules

auth_scheme = HTTPBearer()

async def get_current_user(token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> UserResponseRules:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    headers = {
        'authorization': f'{token.scheme} {token.credentials}'
    }

    user = UserResponseRules(**requests.get(f'{auth_endpoint}/users/me', headers=headers).json())

    if not user:
        raise credentials_exception
    
    return user