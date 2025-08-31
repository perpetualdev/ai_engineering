import csv
from pathlib import Path

"""
  Function to save participant details to a CSV file.
  Parameters
  path - path to save the details
  participant_dict - details to be saved in the path file
"""
def save_participant(path, participant_dict):
  # Define our header row that saves on first save  
  header_row = ["Name", "Age", "Phone", "Track"]
  
  try:
    # Open the file and create a header row
    if path.exists():
      with open(path, 'a', newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(participant_dict.values())
    else:
      with open(path, 'w', newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header_row)
        writer.writerow(participant_dict.values())
  except FileNotFoundError as e:
    print(e)

"""
  Function to read all the participants from the CSV and returns them as a list of dictionaries
"""
def load_participant(path):
  # Read the file from the file path
  with open(path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    participants = []
    for item, value in enumerate(reader):
      if item > 0:
        name, age, phone, track = value
        participants.append({"Name": name, "Age": age, "Phone": phone, "Track": track})
    return participants
      
