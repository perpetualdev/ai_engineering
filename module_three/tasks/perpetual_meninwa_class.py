from datetime import date

class Pet:
  def __init__(self, name, species, age):
    self.name = name
    self.species = species
    self.age = age

  def display_info(self):
    print(f"Pet Name: {self.name}\nSpecies: {self.species}\nAge: {self.age}")

  def celebrate_bday(self):
    bday = input("Please input your pet's bday in this format, (Day/Month) e.g. 13/10: \n")
    today_month = date.today().month
    today_day = date.today().day
    if (bday == f"{today_day}/{today_month}"):
      print(f"Happy Birthday, {self.name}... 🎉🎉🎉")
    else:
      pass
    

new_pet = Pet('Rabbit', 'Rodent', 7)
new_pet.display_info()
new_pet.celebrate_bday()
    