# Create an empty dictionary
student = {}

# Ask user for name and age and store in dictionary
name = input("Enter your name: ")
age = int(input("Enter your age: "))

student["Name"] = name
student["Age"] = age

student["Scores"] = [70, 85, 90]

# Use a comparison operator to check if the student has passed 
average_score = 50

for score in student["Scores"]:
  student["Passed"] = score >= average_score

# Check if the student is a teenager
student["Teenager"] = age >= 13 and age <= 19


print("Student Record:")
for item, result in student.items():
  print(f"{item}: {result}")
