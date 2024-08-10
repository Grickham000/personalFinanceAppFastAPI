# models/user_dto.py
from pydantic import BaseModel

class UserDTO(BaseModel):
    email: str
    name: str
    password: str
    role: str