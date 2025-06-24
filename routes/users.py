from fastapi import APIRouter, Depends, HTTPException
from models.users import TokenResponse, ResponseSchema, Login, Register
from sqlalchemy.orm import Session
from config import get_db
from passlib.context import CryptContext
from repository.users import UsersRepo, JWTRepo
from tables.users import User

router = APIRouter(
    tags=["Authentication"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/signup")
async def signup(request: Register, db: Session = Depends(get_db)):
    try:
        # insert data
        _user = User(
            username = request.username,
            password = pwd_context.hash(request.password),
            email = request.email,
            phone_number = request.phone_number,
            first_name = request.first_name,
            last_name = request.last_name,
        )
        UsersRepo.insert(db, _user)
        # generate token
        token = JWTRepo.generate_token(
            data={"sub": _user.username}
        )
        
        return ResponseSchema(
            code=200,
            status="OK",
            message="User registered successfully"
        )
    except Exception as e:
        print(e.args)
        return ResponseSchema(
            code=500,
            status="INTERNAL SERVER ERROR",
            message="User registered failed"
        ).dict(exclude_none=True)

# login

@router.post("/login")
async def login(request: Login, db: Session = Depends(get_db)):
    try:
        # find user by username
        _user = UsersRepo.find_by_username(db, User, request.username)
        if not _user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        # verify password
        if not pwd_context.verify(request.password, str(_user.password)):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        # generate token
        token = JWTRepo.generate_token(data={"sub": _user.username})
        return ResponseSchema(
            code=200,
            status="OK",
            message="Login successfully",
            result=TokenResponse(
                access_token=token,
                token_type="bearer"
            )
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    