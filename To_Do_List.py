# ==============================
#   To-Do List Application
# ==============================
#  Description:
# A simple console-based To-Do List application built with Python.
# It helps users manage daily tasks efficiently with basic CRUD operations.
#
#  Features:
# - Add new tasks
# - View all tasks (numbered list using enumerate)
# - Edit existing tasks
# - Delete tasks by number
# - Exit the program gracefully
#
#  Technical Details:
# - Uses a Python list to store tasks
# - Implements menu navigation with match-case
# - Includes error handling for invalid inputs
#
#  How to Use:
# 1. Run the program
# 2. Choose an option from the menu (1–5)
# 3. Manage your tasks easily
#
# ==============================

tasks = []

def menu():
    print("=====To-Do List=====")
    print(" 1. Add task ")
    print(" 2. View tasks ")
    print(" 3. Edit task ")
    print(" 4. Delete task ")
    print(" 5. Exit ")
    
while True:
    menu()
    choice = input(" Enter your choice (1 to 5) : ")
    
    match choice:
        case "1":
            task = input ("Add a new task : ")
            tasks.append(task)
            print("Task added successfully")
        case "2":
            if not tasks:
                print("No tasks found!")
            else :
                print("\n Tasks : ")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        case "3":
            if not tasks:
                print("No tasks to edit!")
            else:
                for i , task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("enter the task number you want to edit : "))
                    if 1 <= num <= len(tasks):
                        new_task =input("Enter the new task : ")
                        tasks[num-1]=new_task
                        print("Task updated successfuly.")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a valid number: ")
        case "4":
            if not tasks:
                print("No tasks to delete")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("Enter the task number you want to delete : "))
                    if 1<= num <= len(tasks):
                        deleted= tasks.pop(num-1)
                        print(f"Task deleted : {deleted}")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a valid number :")
        case "5":
            print("Good-bye")
            break
        case _:
            print("Invalid choice , try again")