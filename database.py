from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL) #connection pool created which allows so many sessions to run together.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # temp workspace if we add user then it will temporary go to session 
                                                                            # and not to database first, also, if we commit then it will go to
                                                                            # database permanently.

def get_db():
    db = SessionLocal()
    try:
        yield db # session will get api function through yield and if it is over then finally block gets executed. 
    finally:
        db.close()