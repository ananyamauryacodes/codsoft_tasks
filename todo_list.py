# -----------------------------------------
# To-Do List Manager
# Helps users manage their daily tasks.
#
# Features:
# - Add Task
# - View Tasks
# - Update Task
# - Delete Task
# - Basic Input Validation
# -----------------------------------------

tasks = []

while True:

    print("\n======================================")
    print("          TO-DO LIST MANAGER")
    print("======================================")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    # ---------------- Add Task ----------------

    if choice == "1":

        new_task = input("Enter a new task: ").strip()

        if new_task == "":
            print("Task cannot be empty!")

        else:
            tasks.append(new_task)
            print("Task added successfully!")

    # ---------------- View Tasks ----------------

    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    # ---------------- Update Task ----------------

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks available to update.")

        else:

            print("\nYour Tasks:")

            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            task_number = int(input("Enter the task number to update: "))

            if task_number < 1 or task_number > len(tasks):
                print("Invalid task number!")

            else:

                updated_task = input("Enter the updated task: ").strip()

                if updated_task == "":
                    print("Task cannot be empty!")

                else:
                    tasks[task_number - 1] = updated_task
                    print("Task updated successfully!")

    # ---------------- Delete Task ----------------

    elif choice == "4":

        if len(tasks) == 0:
            print("No tasks available to delete.")

        else:

            print("\nYour Tasks:")

            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            task_number = int(input("Enter the task number to delete: "))

            if task_number < 1 or task_number > len(tasks):
                print("Invalid task number!")

            else:
                tasks.pop(task_number - 1)
                print("Task deleted successfully!")

    # ---------------- Exit ----------------

    elif choice == "5":

        print("Thank you for using the To-Do List Manager!")
        break

    # ---------------- Invalid Choice ----------------

    else:

        print("Invalid choice! Please enter a number between 1 and 5.")
