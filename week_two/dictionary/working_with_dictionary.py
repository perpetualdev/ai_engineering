# ============= DICTIONARY =====================
# Creating Dictionaries
# Using curly braces
student = {
  "name": "Ada",
  "age": 20,
  "course": "Computer Science"
}
print(student)   #  {'name': 'Ada', 'age': 20, 'course': 'Computer Science'}

# Using the dict() constructor
student_info = dict(name="John", age=25, course="Maths")
print(student_info)   # {'name': 'John', 'age': 25, 'course': 'Maths'}

# Empty dictionary
student = {}
# Add key-value pairs 
student["name"] = "Goodness"
student["Interest"] = "AI"
student["Track"] = "AI_Dev"

print(student)  # {'name': 'Goodness', 'Interest': 'AI', 'Track': 'AI_Dev'}


# =================== DICTIONARY COMPREHENSION ===================
# {key_expression: value_expression  for item in iterable if condition}
# dictionary of numbers and their squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# with condition
# Dictionary of even numbers and their cubes
even_cubes = {x: x**3 for x in range(1, 10) if x % 2 == 0}
print(even_cubes)  # {2: 8, 4: 64, 6: 216, 8: 512}

# From Existing Dictionary
students = {"Ada": 85, "John": 40, "Musa": 65}
# Filter students who passed (score >= 50)
passed_students = {name: score for name, score in students.items() if score >= 50}
print(passed_students)   # {'Ada': 85, 'Musa': 65}

# Using String keys
names = ["Ada", "John", "Musa"]
lengths = {name: len(name) for name in names}
print(lengths)  # {'Ada': 3, 'John': 4, 'Musa': 4}

# =================== Accessing Dictionary Items =================
# Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}

# Using key
print(student["name"]) # Ada

# Using get() method (avoids error if key is missing)
print(student.get("age")) # 20
print(student.get("grade")) # None
print(student.get("grade", "Not Found")) # Not Found

# ================== MODIFYING DICTIONARIES ====================
# Change value
student["age"] = 21

# Add new key-value pair
student["grade"] = "A"
print(student) # {'name': 'Ada', 'age': 21, 'course': 'Computer Science', 'grade': 'A'}

# Removing Items 
# pop()
student.pop("grade")
print(student) # {'name': 'Ada', 'age': 21, 'course': 'Computer Science'}
# popitem() - removes last inserted key-value pair
student.popitem() 
print(student)  # {'name': 'Ada', 'age': 21}
# del keyword
del student["age"]
print(student)  # {'name': 'Ada'}
# clear() - removes all items
student.clear() 
print(student)  # {}

# ================= DICTIONARY METHODS ====================
person = {"name": "Emeka", "age": 30}

# Keys()
print(person.keys())   # dict_keys(['name', 'age'])

# values()
print(person.values())  # dict_values(['Emeka', 30])

# items()
print(person.items())   # dict_items([('name', 'Emeka'), ('age', 30)])

# update()
person.update({'age': 31})
print(person)   # {'name': 'Emeka', 'age': 31}

# =============== NESTED DICTIONARIES ======================
students = {
  "student1": {"name": "Ada", "age": 20},
  "student1": {"name": "John", "age": 22},
}

print(students["student1"]["name"])  # John

# =============== LOOPING THROUGH DICT =====================
# Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}

# Loop through keys
for key in student:
  print(key)
# name
# age
# course

# Loop through values:
for value in student.values():
  print(value)
# Ada
# 20
# Computer Science

# Loop through key-value pairs
for key, value in student.items():
  print(f"{key}: {value}")
# name: Ada
# age: 20
# course: Computer Science

# Storing a student's biodata
student = {
  "name": "Chinedu",
  "age": 19,
  "department": "Engineering",
  "subjects": ["Maths", "Physics", "Chemistry"],
  "is_full_time": True
}

print(f"Name: {student['name']}")
print(f"Subjects: {', '.join(student['subjects'])}")

students = [
  {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
  {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
  {"Name": "John", "Interest": "Cyber Security", "Track": "AI_Dev"}
]
print(students[0]["Name"])   # John
print(students[1]["Track"])  # AI_Eng

# ================ DICT OF DICTS ====================
students = {
  "AI010" : {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
  "AI020" : {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
  "AI030" : {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
}

print(students["AI020"]["Name"])  # Mary
print(students["AI030"]["Track"]) # AI_Dev

# =============== DICT OF LISTS ======================
scores = {
  "python": [85, 78, 92],
  "pandas": [88, 74, 90],
  "Scikit-learn": [80, 95, 87]
}

print(scores["python"])     # [85, 78, 92]
print(scores["pandas"][1])  # 74
