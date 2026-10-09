from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict, Field

# (what the API accepts on register/login, and what it returns (never the password))

class UserCreate(BaseModel): # Validates registration data
  email: EmailStr
  password: str = Field(min_length=8, max_length=72)

class UserLogin(BaseModel): # Validates login credentials
  email: EmailStr
  password: str = Field(min_length=8, max_length=72)

class UserOut(BaseModel): # Defines the public user data returned by the API
  id: int
  email: EmailStr
  created_at: datetime

  model_config = ConfigDict(from_attributes=True)

class Token(BaseModel): # Defines the structure of the JWT response
  access_token: str
  token_type: str = "bearer"