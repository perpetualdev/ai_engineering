import csv
import os
from fastapi import HTTPException


CSV_FILE = "contacts.csv"

def read_contacts_from_csv():
  contacts = []
  if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
      writer = csv.writer(file)
      writer.writerow(['id', 'name', 'phone'])
    return contacts
  try:
    with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
        contacts.append({
          "id": int(row["id"]),
          "name": row["name"],
          "phone": row["phone"]
        })
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error reading CSV: {str(e)}")
  return contacts

def write_contacts_to_csv(contacts):
  try:
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
      fieldnames = ['id', 'name', 'phone']
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(contacts)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error writing CSV: {str(e)}")

def get_next_id():
  contacts = read_contacts_from_csv()
  if not contacts:
    return 1
  return max([c["id"] for c in contacts]) + 1