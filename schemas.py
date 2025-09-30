from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: Optional[str] = None 
    address: Optional[str] = None      

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

class User(UserBase):
    id: int
    created_at: datetime
    
    class Config:

        orm_mode = True # Required for SQLAlchemy models to Pydantic
