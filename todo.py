tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n1. Add Task")
    print("2. Delete Task")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        show_tasks()
        if len(tasks) == 0:
            print("Pehla task add karo!")
        else:
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    print("Task deleted!")
                else:
                    print("Invalid number")
            except ValueError:
                print("Number j type karo!")

    elif choice == "3":
        show_tasks()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")