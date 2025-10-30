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

class Enroll(BaseModel):
  courseId: str = Field(..., example=1)

@app.post('/enroll')
def enroll_course(input: Enroll, details = Depends(verify_token)):
  try:
    query = text("""
      SELECT * FROM users
      WHERE id = :id
    """)

    existing = db.execute(query, {id: details.id}).fetchone()

    if existing.userType != 'student':
      raise HTTPException(status_code=400, detail="You are not authorized to enroll!")
    
    enroll_query = text("""
      INSERT INTO enrollment(userid, courseId)
      VALUES (:userid, :courseId)
    """)
    
    new_enrollment = db.execute(enroll_query, {"userid": details.id, "courseId": input.courseId})
    db.commit()

    return {
      "message": "User enrolled successfully!",
      "data": {
        "userId": new_enrollment.userid,
        "courseId": new_enrollment.courseId
      }
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
  
if __name__ == "__main__":
  uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port"))) # type: ignore
