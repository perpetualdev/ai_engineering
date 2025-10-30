from database import db
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import bcrypt
import uvicorn
from middleware import create_token, verify_token

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

class courseRequest(BaseModel):
  title: str = Field(..., example="Backend Course")
  level: str = Field(..., example="Engineer")

@app.post("/signup")
def signUp(input: Simple):
  try:
    duplicate_query = text("""
      SELECT * FROM users
      WHERE email = :email
    """)

    existing = db.execute(duplicate_query, {"email": input.email}).fetchone()
    print(existing)

    if existing is not None:
      raise HTTPException(status_code=400, detail="Email already exist!")

    query = text("""
      INSERT INTO users (name, email, password, userType)
      VALUES (:name, :email, :password, :userType)
      # VALUES (?, ?, ?, ?)
    """)

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(input.password.encode("utf-8"), salt)
    # print(hashed_password)

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
    
    print("RESULT: ", result)
    encoded_token = create_token({
      "id": result.id,
      "email": result.email,
      "userType": result.userType
    }, expiry_time)

    return {
      "message": "Login Successful",
      "token": encoded_token
    }

  except Exception as e:
    raise HTTPException(status_code=500, detail = str(e))

@app.post("/courses")
def addcourses(input: courseRequest, user_data = Depends(verify_token)):
  try:
    print(user_data)

    if user_data['userType'] != 'admin':
      raise HTTPException(status_code=401, detail="You are not authorized to add a course")
    
    query = text("""
      INSERT INTO courses (title, level)
      VALUES (:title, :level)
    """)

    db.execute(query, {"title": input.title, "level": input.level})
    db.commit()

    return {
      "message": "Course added successfully",
      "data": {
        "title": input.title,
        "level": input.level
      }
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
  
class Enroll(BaseModel):
  courseId: int = Field(..., example=1)

@app.post('/enroll')
def enroll_course(input: Enroll, details = Depends(verify_token)):
  try:
    query = text("""
      SELECT * FROM users
      WHERE id = :id
    """)

    existing = db.execute(query, {"id": details["id"]}).fetchone()

    if existing.userType != 'student':
      raise HTTPException(status_code=400, detail="You are not authorized to enroll!")
    
    enroll_query = text("""
      INSERT INTO enrollments(userid, courseId)
      VALUES (:userid, :courseId)
    """)
    
    db.execute(enroll_query, {"userid": details["id"], "courseId": input.courseId})
    db.commit()

    return {
      "message": "User enrolled successfully!",
      "data": {
        "userId": details["id"],
        "courseId": input.courseId
      }
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
  
if __name__ == "__main__":
  uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port"))) # type: ignore

