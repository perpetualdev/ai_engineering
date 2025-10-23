from fastapi import APIRouter, HTTPException
from utils.csv_utils import read_contacts_from_csv, write_contacts_to_csv

router = APIRouter(prefix="/contacts", tags=["Contacts"])

@router.delete("/{contact_id}")
async def delete_contact(contact_id: int):
  contacts = read_contacts_from_csv()
  for i, c in enumerate(contacts):
    if c["id"] == contact_id:
      removed = contacts.pop(i)
      write_contacts_to_csv(contacts)
      return {"message": "Contact deleted", "contact": removed}
  raise HTTPException(status_code=404, detail="Contact not found")

@router.delete("/{contact_id}/remove_field/{field_to_remove}")
async def delete_contact_field(contact_id: int, field_to_remove: str):
  contacts = read_contacts_from_csv()
  for i, c in enumerate(contacts):
    if c["id"] == contact_id:
      if field_to_remove not in c:
        raise HTTPException(status_code=400, detail=f"Field '{field_to_remove}' does not exist!")
      c[field_to_remove] = None
      contacts[i] = c
      write_contacts_to_csv(contacts)
      return {"message": f"Field '{field_to_remove}' removed", "contact": c}
  raise HTTPException(status_code=404, detail="Contact not found")
