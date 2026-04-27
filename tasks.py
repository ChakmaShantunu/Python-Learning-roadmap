def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

            if len(tasks) == 0:
                print("No tasks found")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(i, task.strip())

    except:
        print("No file found")


def add_task():
    task = input("Enter task: ")

    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

    print("Task added")


def delete_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        for i, task in enumerate(tasks, start=1):
            print(i, task.strip())

        num = int(input("Enter task number to delete: "))

        tasks.pop(num - 1)

        with open("tasks.txt", "w") as file:
            file.writelines(tasks)

        print("Task deleted")

    except:
        print("Error occurred")


while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        break

    else:
        print("Invalid choice")