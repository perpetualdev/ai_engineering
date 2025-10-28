from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import bcrypt
import uvicorn
from middleware import create_token

load_dotenv()

app = FastAPI(title="Simple App", version="1.0.0")

expiry_time = int(os.getenv("token_time")) # type: ignore

class Simple(BaseModel):
  name: str = Field(..., example="Sam Larry") # type: ignore
  email: str = Field(..., example="sam@gmail.com") # type: ignore
  password: str = Field(..., example="sam123") # type: ignore
  userType: str = Field(..., example="student") # type: ignore

class LoginRequest(BaseModel):
  email: str = Field(..., example="sam@gmail.com") # type: ignore
  password: str = Field(..., example="sam123") # type: ignore

@app.post("/signup")
def signUp(input: Simple):
  try:
    duplicate_query = text("""
      SELECT * FROM users
      WHERE email = :email
    """)

    existing = db.execute(duplicate_query, {"email": input.email}).fetchone

    if existing:
      raise HTTPException(status_code=400, detail="Email already exist!")

    query = text("""
      INSERT INTO users (name, email, password, userType)
      VALUES (:name, :email, :password, :userType)
      # VALUES (?, ?, ?, ?)
    """)

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(input.password.encode("utf-8"), salt)
    print(hashed_password)

    db.execute(query, {
      "name": input.name, 
      "email": input.email, 
      "password": hashed_password, 
      "userType": input.userType
    })
    db.commit()

    return {
      "message": "User created successfully",
      "data": {
        "name": input.name, 
        "email": input.email,
        "userType": input.userType
      }
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail = str(e))
  

@app.post("/login")
def login(input: LoginRequest):
  try:
    query = text("""
      SELECT * FROM users WHERE email = :email
    """)
    result = db.execute(query, {"email": input.email}).fetchone()

    if not result:
      raise HTTPException(status_code=404, detail = "invalid email or password")
    
    verified_password = bcrypt.checkpw(input.password.encode('utf-8'), result.password.encode('utf-8'))

    if not verified_password:
      raise HTTPException(status_code=404, detail = "invalid email or password")
    
    encoded_token = create_token({
      "email": result.email,
      "userType": result.userType
    }, expiry_time)

    return {
      "message": "Login Successful",
      "token": encoded_token
    }

  except Exception as e:
    raise HTTPException(status_code=500, detail = str(e))
  
if __name__ == "__main__":
  uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port"))) # type: ignore
