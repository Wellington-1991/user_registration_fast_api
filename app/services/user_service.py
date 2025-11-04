from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreateDTO, UserUpdateDTO

class UserService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_list_users(self):
        return UserRepository.get_all(self.db)
    
    def get_user(self, user_id: int):
        return UserRepository.get_by_id(self.db, user_id)
    
    def create_user(self, user_data: UserCreateDTO):
        return UserRepository.create(self.db, user_data)
    
    def update_user(self, user_id: int, user_data: UserUpdateDTO):
        return UserRepository.update(self.db, user_id, user_data)
    
    def delete_user(self, user_id: int):
        return UserRepository.delete(self.db, user_id)