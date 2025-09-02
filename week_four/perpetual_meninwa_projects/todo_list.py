# Simple TO-DO List App
from pathlib import Path
new_folder = Path("week_four/perpetual_meninwa_projects/todo_folder")
new_folder.mkdir(exist_ok=True)
todo_path = new_folder / "todo.txt"

# Defining Variables
tasks = []
completed_tasks = []

# Function to add task
def add_task(new_task):
  if new_task != "":
    tasks.append(new_task)
    print("New Task added successfully: \n", tasks)
  else:
    raise ValueError("Task cannot be empty")
  
# Function to remove task from the list of tasks
def remove_task(removed_task):
  if removed_task not in tasks:
    raise ValueError("Task cannot be found!")
  else:
    tasks.remove(removed_task)
    print(f"{removed_task} removed successfully!")
    print("New List of Tasks: \n", tasks)

# Function to edit task
def edit_task(task, task_to_replace):
  if task_to_replace in tasks:
    task_index = tasks.index(task_to_replace)
    tasks.remove(tasks[task_index])
    tasks.insert(task_index, task)
    print("Updated Task\n", tasks)
  else:
    raise ValueError("The task does not exist!")

# Function to mark tasks as complete
def mark_as_complete(task):
  if task in tasks:
    new_tasks = tasks.copy()
    selected_task = new_tasks.pop(new_tasks.index(task))
    print(selected_task)
    completed_tasks.append(selected_task)
    # uncompleted_tasks.insert(new_tasks)
    print(completed_tasks)
  else:
    raise ValueError("Task cannot be found")
  
def display_completed_tasks():
  print("Completed Tasks: ", completed_tasks)
  
def display_not_completed_tasks():
  uncompleted_tasks = [x for x in tasks if x not in completed_tasks]
  print("Uncompleted Tasks", uncompleted_tasks)

# Function to display task
def diplay_tasks():
  print("\nAll Tasks: \n", tasks)

def write_to_file(tasks):
  with open(todo_path, "w", encoding="utf-8") as f:
    f.write("All Tasks: \n", )
    for task in tasks:
      f.write(f" -> {task}\n")
    f.write("Completed Tasks\n")
    for c_task in completed_tasks:
      f.write(f" -> {c_task}\n")
    uncompleted_tasks = [x for x in tasks if x not in completed_tasks]
    f.write("Not Completed Tasks\n")
    for n_task in uncompleted_tasks:
      f.write(f"-> {n_task}\n")

def main():
  try:
    while True:
      print("Select Operation:")
      print("1. Add Task")
      print("2. Remove Task")
      print("3. Display Task")
      print("4. Edit Task")
      print("5. Mark Task as Complete")
      print("6. Display Completed Tasks")
      print("7. Display Uncompleted Tasks")
      print("8. Exit")

      user_input = int(input("Please select from 1, 2, 3, 4, 5, 6, 7, 8: "))
      if (user_input == 8):
        print("Exiting program...")
        break
      elif (user_input == 1):
        task_to_add = input("What task would you like to add?: ")
        add_task(task_to_add)
        if (todo_path.exists()):
          # Writing to the file
          with open(todo_path, "a", encoding="utf-8") as f:
            f.write(f"-> {task_to_add}")
        else:
          write_to_file(tasks)
      elif (user_input == 2):
        task_to_remove = input("What task would you like to remove?: ")
        remove_task(task_to_remove)
        write_to_file(tasks)
      elif (user_input == 3):
        diplay_tasks()
      elif (user_input == 4):
        task_to_replace = input("What task would you like to edit?: ")
        new_task = input("What would you like to replace it with? ")
        edit_task(new_task, task_to_replace)
        write_to_file(tasks)
      elif (user_input == 5):
        task_completed = input("Enter completed task: ")
        mark_as_complete(task_completed)
        print(f"{task_completed} marked as complete")
        write_to_file(tasks)
      elif (user_input == 6):
        display_completed_tasks()
      elif (user_input == 7):
        display_not_completed_tasks()
      else: 
        print("Invalid input")
  except ValueError as e:
    print("Error: ", e)
  finally:
    print("Thank you for using our task management app!")
    
main()
