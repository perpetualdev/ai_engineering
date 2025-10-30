import jwt
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from fastapi import Request, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv()

bearer = HTTPBearer()

secret_key = os.getenv("secret_key")

def create_token(details, expiry: int):
  expire = datetime.now() + timedelta(minutes=expiry)

  details.update({"exp": expire})

  encoded_jwt = jwt.encode(details, secret_key)

  return encoded_jwt

def verify_token(request: HTTPAuthorizationCredentials = Security(bearer)):
  # payload = request.headers.get("Authorization")
  token = request.credentials

  # token = payload.split(" ")[1]
  verified_token = jwt.decode(token, secret_key, algorithms=["HS256"])

  return {
    "id": verified_token.get("id"),
    "email": verified_token.get("email"),
    "userType": verified_token.get("userType")
  }
