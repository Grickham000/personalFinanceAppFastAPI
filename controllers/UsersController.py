# controllers/UsersController.py
from fastapi import APIRouter, HTTPException, Depends
from schemas.user_api import UserAPI
from services.UserService import UserService
from daos.UserDAO import UserDAO
from firebase_admin import firestore
from models.user_dto import UserDTO

router = APIRouter()

def get_firestore_db():
    return firestore.client()

@router.post("/users/", response_model=UserAPI)
async def create_user(user: UserDTO, db=Depends(get_firestore_db)):
    user_dao = UserDAO(db)
    user_service = UserService(user_dao)
    user_dto = UserDTO(
        email=user.email,
        name=user.name,
        password=user.password,  # Use a secure method to handle passwords
        role=user.role
    )
    user_service.create_user(user_dto)
    return user

@router.get("/users/{email}", response_model=UserAPI)
async def get_user(email: str, db=Depends(get_firestore_db)):
    user_dao = UserDAO(db)
    user_service = UserService(user_dao)
    user_dto = user_service.get_user(email)
    if not user_dto:
        raise HTTPException(status_code=404, detail="User not found")
    return user_dto

@router.delete("/users/{email}")
async def delete_user(email: str, db=Depends(get_firestore_db)):
    user_dao = UserDAO(db)
    user_service = UserService(user_dao)
    user_service.delete_user(email)
    return {"message": "User deleted successfully"}

@router.put("/users/{email}", response_model=UserAPI)
async def update_user(email: str, user: UserDTO, db=Depends(get_firestore_db)):
    user_dao = UserDAO(db)
    user_service = UserService(user_dao)
    user_dto = UserDTO(
        email=user.email,
        name=user.name,
        password=user.password,  # Use a secure method to handle passwords
        role=user.role
    )
    user_service.update_user(email,user_dto)
    return user_dto

@router.get("/users/", response_model=list[UserAPI])
async def get_all_users(db=Depends(get_firestore_db)):
    user_dao = UserDAO(db)
    user_service = UserService(user_dao)
    user_dto_list = user_service.get_all_users()
    return user_dto_list