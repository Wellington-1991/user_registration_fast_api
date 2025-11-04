from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreateDTO(UserBase):
    password: str

class UserUpdateDTO(UserBase):
    password: str

class UserResponseDTO(UserBase):
    id: int

    class Config:
        from_attributes = True