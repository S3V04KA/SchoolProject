from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth_api_sdk.deps import get_current_user
from app.auth_api_sdk.schemas.user import UserResponseRules

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/', dependencies=[Depends(get_current_user)])
async def root(user: Annotated[UserResponseRules, Depends(get_current_user)]):
    return user