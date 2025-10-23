from fastapi import APIRouter
from utils.csv_utils import read_contacts_from_csv, write_contacts_to_csv, get_next_id
from validators.contact_validator import Contact

router = APIRouter(prefix="/contacts", tags=["Contacts"])

@router.post("/", status_code=201)
async def create_contact(contact: Contact):
  contacts = read_contacts_from_csv()
  new_id = get_next_id()
  new_contact = {"id": new_id, **contact.dict()}
  contacts.append(new_contact)
  write_contacts_to_csv(contacts)
  return {"message": "Contact added", "contact": new_contact}