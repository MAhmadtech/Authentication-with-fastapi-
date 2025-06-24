from typing import TypeVar, Generic, Optional, Type
from sqlalchemy.orm import Session

from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from config import SECRET_KEY, ALGORITHM
from fastapi import Depends, Request, HTTPException
from fastapi.security import HTTPBearer, HTTPBasicCredentials
from tables.users import User

T = TypeVar('T')
UserType = TypeVar('UserType', bound=User)

# users
class BaseRepo():
    @staticmethod
    def insert(db: Session, model: User):
        db.add(model)
        db.commit()
        db.refresh(model)
        return model

class UsersRepo(BaseRepo):
    @staticmethod
    def find_by_username(db: Session, model: Type[UserType], username: str):
        return db.query(model).filter(model.username == username).first()

# token

class JWTRepo():
    @staticmethod
    def generate_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    @staticmethod
    def decode_token(token: str):
        try:
            decode_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return decode_token if decode_token['expires'] >= datetime.now(timezone.utc).timestamp() else None
        except:
            return None


