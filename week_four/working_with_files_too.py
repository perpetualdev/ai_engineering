from pathlib import Path
import json
import csv

workspace = Path("week_four/workspace_files")
workspace.mkdir(exist_ok=True)
file_path = workspace / "notes.txt"

f = open(file_path, "w", encoding="utf-8")
f.write("This is the first line in notes.txt\n")
f.close()

# Created if it does not exist
# f = open(workspace / "created_once.txt", "x", encoding="utf-8")
# f.write("This file will only be created if it doesn't exist.\n")
# f.close()

# Create Shopping List
f = open(file_path, "w", encoding="utf-8")
f.write("Shopping List:\n")
f.write(" - Rice\n")
f.write(" - Beans\n")
f.write(" - Garri\n")
f.close()

# Append to the file
f = open(file_path, "a", encoding="utf-8")
f.write(" - Groundnut oil\n")
f.write(" - Maggi\n")
f.close()

# Read from file
# Read whole file
f = open(file_path, "r", encoding="utf-8")
content = f.read()
f.close()
print(content)
"""
  Shopping List:
 - Rice
 - Beans
 - Garri
 - Groundnut oil
 - Maggi
"""

# Read line-by-line
f = open(file_path, "r", encoding="utf-8")
print("First line:", f.readline().rstrip())
print("Second line:", f.readline().rstrip())
f.close()
# First line: Shopping List:
# Second line:  - Rice

# Read as a list of lines
f = open(file_path, "r", encoding="utf-8")
lines = f.readlines()
f.close()
print("Lines list:", [line.rstrip() for line in lines])
# Lines list: ['Shopping List:', ' - Rice', ' - Beans', ' - Garri', ' - Groundnut oil', ' - Maggi']

# Iterate over lines (memory-friendly)
f = open(file_path, "r", encoding="utf-8")
for line in f:
  print("->", line.rstrip())
f.close()

"""
  -> Shopping List:
  ->  - Rice
  ->  - Beans
  ->  - Garri
  ->  - Groundnut oil
  ->  - Maggi
"""

# Write safely
with open(file_path, "w", encoding="utf-8") as f:
  f.write("My Todo List: \n")
  f.write(" - Revise Python file handline\n")
  f.write(" - Practive error handling within a function")
  f.write(" - Practice JSON & CSV\n")

# # Append safely
# with open(file_path, "a", encoding="utf-8"):
#   f.write(" - Build a small project\n")

try:
  with open(workspace / "missing_file.txt", "r") as f:
    content = f.read()
    print("File content:", content)
except FileNotFoundError:
  print("Oops! That file doesn't exist yet.")
  print("Let's create it first!")

  # Now create the file
  with open(workspace / "missing_file.txt", "w") as f:
    f.write("Now I exist!")
  print("File created successfully!")
"""
  Oops! That file doesn't exist yet.
  Let's create it first!
  File created successfully!
"""

# Checking if files exist before using then
if file_path.exists():
  print(f"Found the file: {file_path.name}")

  # Get some info about the file
  file_size = file_path.stat().st_size
  print(f"File size: {file_size} bytes")

  # Read and show the content
  with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print(f"Content preview: {content[:50]}...")  # First 50 characters
else:
  print(f"File {file_path.name} doesn't exist")
  print("You might want to create it first!")

"""
  Found the file: notes.txt
  File size: 116 bytes
  Content preview: My Todo List:
  - Revise Python file handline
  - P...
"""

# Create some student data (like a mini database)
student_data = {
  "name": "Oyindamola",
  "age": 16,
  "courses": ["Python", "Data Science", "Web Development"],
  "grades": {
    "Python": "A", 
    "Data Science": "B+", 
    "Web Development": "A-"
  },
  "is_graduated": False
}

# Save the data to a JSON file
json_file = workspace / "student_data.json"
with open(json_file, "w", encoding="utf-8") as f:
  json.dump(student_data, f, indent=2)  # indent-2 makes it pretty and readable

print("Student data saved to JSON file!")

# # Now read it back
with open(json_file, "r", encoding="utf-8") as f:
  loaded_data = json.load(f)

print("\nData read from JSON file: ")
print(f"Student name: {loaded_data['name']}")
print(f"Age: {loaded_data['age']}")
print(f"Courses: {", ".join(loaded_data['courses'])}")
print(f"Python grade: {loaded_data['grades']['Python']}")

# Working with CSV Files

csv_file = workspace / "students.csv"

# Create sample student data
students = [
  ["Name", "Age", "Course", "Grade"],
  ["Precious", 20, "Python", "A"],
  ["Favour", 22, "JavaScript", "B+"],
  ["Ore", 21, "Python", "A-"],
  ["Susan", 23, "Data Science", "A"]
]

# Write data to CSV file
with open(csv_file, "w", newline="", encoding="utf-8") as f:
  writer = csv.writer(f)
  writer.writerows(students)  # Write all rows at once

print("Student data written to CSV file!")

# Read the CSV file back
print("\nReading CSV file:")
with open(csv_file, "r", encoding="utf-8") as f:
  reader = csv.reader(f)

  for row_number, row in enumerate(reader):
    if row_number == 0:   # Header row
      print(f"Headers: {" | ".join(row)}")
      print("-" * 40)
    else:  # Data rows
      name, age, course, grade = row
      print(f"{name} ({age} years) - {course}: {grade}")

# Working with Multiple Files at Once
input_file = workspace / "original.txt"
output_file = workspace / "processed.txt"

# Create an input file with some text
sample_text = """hello world
python programming
file handling tutorial
learning is fun"""

with open(input_file, "w", encoding="utf-8") as f:
  f.write(sample_text)

print("Created input file")

# Process the file: read from input, write processed version to output
with open(input_file, "r", encoding="utf-8") as infile, \
  open(output_file, "w", encoding="utf-8") as outfile:

  line_number = 1
  for line in infile:
    # Process each line: make it uppercase and add line numbers
    processed_line = f"Line {line_number}: {line.strip().upper()}\n"
    outfile.write(processed_line)
    line_number += 1

print("File processing complete!")

# show the results
print("\nOriginal file: ")
with open(input_file, "r", encoding="utf=8") as f:
  print(f.read())

print("\nProcessed file: ")
with open(output_file, "r", encoding="utf-8") as f:
  print(f.read())

# Output to expect
"""
Created input file
File processing complete!

Original file:
hello world
python programming
file handling tutorial
learning is fun

Processed file:
Line 1: HELLO WORLD
Line 2: PYTHON PROGRAMMING
Line 3: FILE HANDLING TUTORIAL
Line 4: LEARNING IS FUN
"""

# _____________ MOVING AROUND IN A FILE ______________
file_path = workspace / "story.txt"

# Create a sample story file
story = """Once upon a time, there was a lady  who was very curious and inquisitive, 
she just want to know how things work behind the scene. 
Eventually she had an opportunity to hopp into the world of programming for the first time.
She started with python, now she codes in Python every day.
One day, she discovered file handling.
It opened up a whole new world of possibilities!
The end."""

with open(file_path, "w", encoding="utf-8") as f:
  f.write(story)

print("Created a story file!")

# Exploring moving around in the file
with open (file_path, "r", encoding="utf-8") as f:
  print("\nFile positioning demo:")

  # Read first 20 characters
  first_part = f.read(20)
  print(f"First 20 characters: '{first_part}")
  # OUTPUT: First 20 characters: 'Once upon a time, th

  # Check where we are now
  current_position = f.tell()
  print(f"Current position in file: {current_position}")
  # OUTPUT: Current position in file: 20

  # Jump to the beginning
  f.seek(0)
  print(f"After seeking to beginning: position {f.tell()}")
  # OUTPUT: After seeking to beginning: position 0

  # Jump to position 50 and read from there
  f.seek(50)
  rest_of_line = f.readline()
  print(f"Reading from position 50: '{rest_of_line.strip()}")
  # OUTPUT: Reading from position 50: 'urious and inquisitive,

  # Go back to the beginning and read the first line
  f.seek(0)
  first_line = f.readline()
  print(f"First line: '{first_line.strip()}'")
  # OUTPUT: First line: 'Once upon a time, there was a lady  who was very curious and inquisitive,'
