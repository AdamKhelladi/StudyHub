from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated=["auto"])

def hash_password(password: str) -> str:
  return pwd_context.hash(password)

def verify_password(plain_password: str, hash_password: str) -> bool: 
  return pwd_context.verify(plain_password, hash_password)

