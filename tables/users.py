from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from config import Base
import datetime


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'


    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)


    first_name = Column(String)
    last_name = Column(String)

    create_date = Column(DateTime, default=datetime.datetime.now())
    update_date = Column(DateTime, default=datetime.datetime.now())