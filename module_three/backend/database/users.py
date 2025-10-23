from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import bcrypt
import uvicorn

load_dotenv()

app = FastAPI(title="Simple App", version="1.0.0")

class Simple(BaseModel):
  name: str = Field(..., example="Sam Larry")
  email: str = Field(..., example="sam@gmail.com")
  password: str = Field(..., example="sam123")

@app.post("/signup")
def signUp(input: Simple):
  try:
    duplicate_query = text("""
      SELECT * FROM users
      WHERE email = :email
    """)

    existing = db.execute(duplicate_query, {"email": input.email})

    if existing:
      print("Email already exist")
      # raise HTTPException(status_code=400, detail="Email already exist!")

    query = text("""
      INSERT INTO users (name, email, password)
      VALUES (:name, :email, :password)
      # VALUES (?, ?, ?)
    """)

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(input.password.encode('utf-8'), salt)
    print(hashed_password)

    db.execute(query, {"name": input.name, "email": input.email, "password": hashed_password})
    db.commit()

    return {
      "message": "User created successfully",
      "data": {
        "name": input.name, 
        "email": input.email
      }
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail = e)
    # print("Server error")
  
if __name__ == "__main__":
  uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))
