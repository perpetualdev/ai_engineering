from pathlib import Path
from file_ops import save_participant, load_participant

# Create a function that defines our folder
def participant_folder():
  folder = Path("tasks/week_four_tasks/participant_pkg")
  folder.mkdir(exist_ok=True)
  return folder / "contacts.csv"

path = participant_folder()

def contact_form():
  # Defining variables
  dic = {}
  while True:
    try:
      # Collecting contact's name
      name = input("Please enter your name: ")
      if not name.isalpha():
        raise ValueError("Name must be alphabets only")
      
      # Collecting contact's age
      age = int(input("Please enter your age: "))
      if age <= 0 and age.is_integer():
        raise ValueError("Age must be a positive number")
      
      # Collecting contact's phone number
      phone = input("Please enter your phone number: ")
      if len(phone) != 11:
        raise ValueError("Phone number must be 11 digits")

      # Collecting contact's track
      track = input("Please enter your track: ")
      if track == "":
        print("Track should not be empty")
      # break
    except ValueError as e:
      print("Invalid input: ", e)
    finally:
      print("Details entered successfully!")
      dic["Name"] = name
      dic["Age"] = age
      dic["Phone"] = phone
      dic["Track"] = track
      print(dic)
      dic_items = load_participant(path)
      print(f"Number of Participants: {len(dic_items)}")
      return dic

def participant_list(n):
  path = participant_folder()
  for i in range(n):
    participant_dic = contact_form()
    save_participant(path, participant_dic)

def main():
  num_people = int(input("Enter number of participants: "))
  participant_list(num_people)

if __name__ == '__main__':
  main()
