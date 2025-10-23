from fastapi import APIRouter, HTTPException
from utils.csv_utils import read_contacts_from_csv, write_contacts_to_csv
from validators.contact_validator import Contact

router = APIRouter(prefix="/contacts", tags=["Contacts"])

@router.put("/{contact_id}")
async def update_contact(contact_id: int, contact: Contact):
  contacts = read_contacts_from_csv()
  for i, c in enumerate(contacts):
    if c["id"] == contact_id:
      contacts[i] = {"id": contact_id, **contact.model_dump()}
      write_contacts_to_csv(contacts)
      return {"message": "Contact updated", "contact": contacts[i]}
  raise HTTPException(status_code=404, detail="Contact not found")