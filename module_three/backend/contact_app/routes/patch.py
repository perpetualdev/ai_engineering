from fastapi import APIRouter, HTTPException
from utils.csv_utils import read_contacts_from_csv, write_contacts_to_csv
from validators.contact_validator import ContactUpdate

router = APIRouter(prefix="/contacts", tags=["Contacts"])

@router.patch("/{contact_id}/update_field")
async def update_contact_field(contact_id: int, contact_item: ContactUpdate):
  contacts = read_contacts_from_csv()
  for i, c in enumerate(contacts):
    if c["id"] == contact_id:
      updated_contact = c.copy()
      update_data = contact_item.model_dump(exclude_unset=True) 
      updated_contact.update(update_data)

      contacts[i] = updated_contact
      write_contacts_to_csv(contacts)
      return {"message": "Contact updated", "contact": updated_contact}
  raise HTTPException(status_code=404, detail="Contact not found")