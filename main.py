from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import get_db

app = FastAPI()

@app.post("/users/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)

    # 201 okay status will tell that the table is created.

def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # this (user:...) is sending pydantic validation request if request body is wrong and
    # validation didnt run properly then it will give error.  
    # also depends(get_db) we will get database session and without calling databse.py. 

    db_user = models.User(name=user.name, email=user.email)

    #here the curd operations are being handled:
    #pydantic validation (body check) and swagger k through JSON format mein jaega, toh checking if user is writing the right format or not. 

    db.add(db_user)                     # new user object session me stage hojaega isse.
    db.commit()                         # completes a transaction and permanent save data into database.
    db.refresh(db_user)                 # new id and created_at will be there for new user
    return db_user

@app.get("/users/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()  # gettting all users together

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user