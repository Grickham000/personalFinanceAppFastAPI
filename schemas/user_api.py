# schemas/user_api.py
from pydantic import BaseModel, EmailStr

class UserAPI(BaseModel):
    email: EmailStr
    name: str
    role: str
    # Exclude sensitive fields like password