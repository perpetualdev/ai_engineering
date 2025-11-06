from fastapi import FastAPI
import os
import uvicorn
from dotenv import load_dotenv
from routes import api_router

load_dotenv()

app = FastAPI(title="Contact App", version="1.0.0")

app.include_router(api_router)

@app.get("/")
def root():
  return {"message": "Welcome to the Contact App"}

if __name__ == "__main__":
  uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("contact_port"))) # type: ignore
