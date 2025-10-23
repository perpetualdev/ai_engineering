from pydantic import BaseModel, Field

class Contact(BaseModel):
  name: str
  phone: str = Field(..., max_length=15)

class ContactUpdate(BaseModel):
  name: str | None = None
  phone: str | None = None

class ContactResponse(BaseModel):
  id: int
  name: str
  phone: str
