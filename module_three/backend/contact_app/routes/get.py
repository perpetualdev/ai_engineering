from typing import List
from fastapi import APIRouter, HTTPException
from utils.csv_utils import read_contacts_from_csv
from validators.contact_validator import ContactResponse

router = APIRouter(prefix="/contacts", tags=["Contacts"])

@router.get("/", response_model=List[ContactResponse])
async def get_contacts():
  return read_contacts_from_csv()

@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: int):
  contacts = read_contacts_from_csv()
  for contact in contacts:
    if contact["id"] == contact_id:
      return contact
  raise HTTPException(status_code=404, detail="Contact not found")