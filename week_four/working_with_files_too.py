from pathlib import Path

workspace = Path("workspace_files")
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
content = f.readlines()
f.close()
print(content)

# Read
