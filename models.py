from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base): # base class comes from sqlalchemy and its a type of aggrement which tells user that he will create a
                  # database table and without it it will just create a simple class file

    __tablename__ = 'users' # tells sql and alembic that database name of python class should be named as 'users'.
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())

    phone_number = Column(String, nullable=True) 
    address = Column(String, nullable=True) 