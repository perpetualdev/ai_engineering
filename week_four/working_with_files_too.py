from pathlib import Path

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

