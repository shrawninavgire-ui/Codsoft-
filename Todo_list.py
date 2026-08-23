# To-Do List Application

tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n--- To-Do List ---")
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")


def add_task():
    title = input("\nEnter task: ")
    tasks.append({"title": title, "completed": False})
    print("Task added successfully!")


def update_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to update: "))

        if 1 <= number <= len(tasks):
            new_title = input("Enter new task: ")
            tasks[number - 1]["title"] = new_title
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.
