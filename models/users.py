from typing import Generic, TypeVar, Optional
from pydantic import BaseModel as GenericModel


T = TypeVar('T')

# Login
class Login(GenericModel, Generic[T]):
    username: str
    password: str
    
# Register
class Register(GenericModel, Generic[T]):
    id: str
    username: str
    email: str
    phone_number: str
    first_name: str
    last_name: str
    password: str

# Response model
class ResponseSchema(GenericModel, Generic[T]):
    code: int
    status: str
    message: str
    result: Optional[T] = None

# Token
class TokenResponse(GenericModel, Generic[T]):
    access_token: str
    token_type: str  
        
        
        
        







