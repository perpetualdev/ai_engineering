from pathlib import Path

# Creating our participant_pkg folder
participant = Path("tasks/week_four_tasks/participant_pkg")
participant.mkdir(exist_ok=True)
file_path = participant / "__init__.py"

# Creating our init file
f = open(file_path, "w", encoding="utf-8")
f.write("# This is our module init file")
f.close()

f = open(participant / "file_ops.py", "w", encoding="utf-8")
f.write("# Starting out our project")
f.close()