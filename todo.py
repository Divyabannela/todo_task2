TASK_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return [task.strip() for task in f.readlines()]
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print()
def add_task(tasks):
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added")
    else:
        print("Empty task not added.")
def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number.")
def main():
    print("📋 To-Do List App")
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
         
    
