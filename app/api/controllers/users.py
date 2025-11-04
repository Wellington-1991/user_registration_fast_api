from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.user import UserCreateDTO, UserResponseDTO, UserUpdateDTO
from app.services.user_service import UserService

router = APIRouter(prefix='/users', tags=['Users'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[UserResponseDTO])
def list_users(db: Session = Depends(get_db)):
    return UserService(db).get_list_users()

@router.get("/{user_id}", response_model=UserResponseDTO)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).get_user(user_id)

@router.post("/", response_model=UserResponseDTO)
def create_user(user: UserCreateDTO, db: Session = Depends(get_db)):
    return UserService(db).create_user(user)