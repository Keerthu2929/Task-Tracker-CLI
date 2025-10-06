import sys
import json
import os
from datetime import datetime

Tasks_File = "tasks.json"


def load_tasks():
    if os.path.exists(Tasks_File):
        with open(Tasks_File, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(Tasks_File, 'w') as file:
        json.dump(tasks, file, indent=2)


def add_task(description):
    tasks = load_tasks()

    if tasks:
        next_id = max(task["id"] for task in tasks) + 1
    else:
        next_id = 1


    new_task = {
        "id": next_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID : {next_id})")


def update_task(task_id, new_description):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return


    print(f"Error: Task {task_id} not found")


def delete_task(task_id):
    tasks = load_tasks()

    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            save_tasks(tasks)
            print(f"Task {task_id} deleted successfully")
            return

    print(f"Error: Task {task_id} not found")


def mark_in_progress(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as in progress")
            return

    print(f"Error: Task {task_id} not found")


def mark_done(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "done"
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as done")
            return

    print(f"Error: Task {task_id} not found")


def list_tasks(status=None):
    tasks = load_tasks()

    if not tasks:
        print("No task found")
        return

    if status:
        tasks = [task for task in tasks if task["status"] == status]
        if not tasks:
            print(f"No {status} tasks found")
            return

    print("\nYour tasks:")
    print("-" * 40)
    for task in tasks:
        if task['status'] == 'todo':
            status_text = "TO DO"
        elif task['status'] == 'in-progress':
            status_text = "IN PROGRESS"
        else:
            status_text = "DONE"
        print(f"{task['id']}. {task['description']}")
        print(f" status: {status_text}")
        print(f" created: {task['createdAt'][:16]}")
        print()


def show_help():
    print("Task Tracker Commands:")
    print("  add 'task'              - Add new task")
    print("  update id 'task'        - Update task")
    print("  delete id               - Delete task")
    print("  mark-in-progress id     - Start working on task")
    print("  mark-done id            - Complete task")
    print("  list                    - Show all tasks")
    print("  list done/todo/in-progress - Filter by status")


def main():
    if len(sys.argv) < 2:
        show_help()
        return


command = sys.argv[1]

if command == "add":
    if len(sys.argv) < 3:
        print("Error: please provide a task description.")
        sys.exit(1)
    add_task(sys.argv[2])

elif command == "update":
    if len(sys.argv) < 4:
        print("Error: please provide task ID and new description.")
        sys.exit(1)
    try:
        task_id = int(sys.argv[2])
        update_task(task_id, sys.argv[3])
    except:
        print("Error: task ID must be a number.")

elif command == "delete":
    if len(sys.argv) < 3:
        print("Error: please provide task ID.")
        sys.exit(1)
    try:
        task_id = int(sys.argv[2])
        delete_task(task_id)
    except:
        print("Error: Task ID must be a number.")

elif command == "mark-in-progress":
    if len(sys.argv) < 3:
        print("Error: please provide task ID.")
        sys.exit(1)
    try:
        task_id = int(sys.argv[2])
        mark_in_progress(task_id)
    except:
      print("Error: task ID must be a number.")

elif command == "mark-done":
  if len(sys.argv) < 3:
    print("Error: please provide task ID.")
    sys.exit(1)
  try:
    task_id = int(sys.argv[2])
    mark_done(task_id)
  except:
    print("Error: Task ID must be a number.")
    
elif command =="list":
  if len(sys.argv) == 2:
    list_tasks()
  else:
    list_tasks(sys.argv[2])

else:
  print(f"Error: invalid command {command}")
  show_help()
  
if __name__ == "__main__":
  main()