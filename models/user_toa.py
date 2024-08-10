# models/user_toa.py
from models.user_dto import UserDTO
class UserTOA:
    def __init__(self, email: str, name: str, password: str, role: str):
        self.email = email
        self.name = name
        self.password = password
        self.role = role

    @classmethod
    def from_dto(cls, dto):
        return cls(
            email=dto.email,
            name=dto.name,
            password=dto.password,
            role=dto.role
        )

    def to_dto(self):
        return UserDTO(
            email=self.email,
            name=self.name,
            password=self.password,
            role=self.role
        )