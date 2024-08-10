# services/UserService.py
from models.user_toa import UserTOA
from daos.UserDAO import UserDAO
from models.user_dto import UserDTO

class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def create_user(self, user_dto: UserDTO):
        user_toa = UserTOA.from_dto(user_dto)
        self.user_dao.save_user(user_toa.email, user_toa.__dict__)

    def get_user(self, email: str) -> UserDTO:
        user_data = self.user_dao.get_user(email)
        if user_data:
            user_toa = UserTOA(**user_data)
            return user_toa.to_dto()
        return None
    
    def get_all_users(self):
        user_data_list = self.user_dao.get_all_users()
        user_dto_list = []
        for user_data in user_data_list:
            user_toa = UserTOA(**user_data)
            user_dto_list.append(user_toa.to_dto())
        return user_dto_list

    def delete_user(self, email: str):
        self.user_dao.delete_user(email)
    
    def update_user(self,email: str, user_dto):
        user_toa=UserTOA.from_dto(user_dto)
        self.user_dao.update_user(email, user_toa.__dict__)