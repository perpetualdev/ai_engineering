# Collect student bio-data from user input(name, age, gender, courses) and stores it in a dict

# Student Bio Data Collection
collected_data = {}

for i in range(1, 5):
  student_details = {}
  courses = []
  student_name = input(f"Enter your name: ")
  student_age = input(f"Enter your age: ")
  student_gender = input(f"Enter your gender(Male/Female): ")
  num_of_courses = int(input("How many courses are you taking?: "))
  for j in range(1, num_of_courses):
    # Ask user to enter courses
    course = input(f"Enter your course {j}: ")
    # add them to the list
    courses.append(course)
  student_details['Student Name'] = student_name
  student_details['Age'] = student_age
  student_details['Gender'] = student_gender
  student_details['Courses'] = courses
  print("Student Details: ",student_details)
  collected_data[f"{student_name}"] = student_details
# Display the bio-data neatly using escape sequences
for key, value in collected_data.items():
  print(f"{key}:\t{value}\n")