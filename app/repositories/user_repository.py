from sqlalchemy.orm import Session
from app.db.models.User import User
from app.schemas.user import UserCreateDTO, UserUpdateDTO

class UserRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(User).all()
    
    @staticmethod
    def get_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def create(db: Session, user: UserCreateDTO):
        db_user = User(username=user.username, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def update(db: Session, user_id: int, user_data: UserUpdateDTO):
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            db_user.username = user_data.username
            db_user.email = user_data.email
            db.commit()
            db.refresh(db_user)
        return db_user
    
    @staticmethod
    def delete(db: Session, user_id: int):
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            db.delete(db_user)
            db.commit()
        return db_user