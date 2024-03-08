## Todo List Application:
# Add, Remove, update, Delete
print("Todo List App".center(77, " "))

# Four Example of each task and then we store each in another list.
task1 = {'task_name': 'Complete Project Proposal', 'deadline': '2024-03-15', 'status': 0}
task2 = {'task_name': 'Review Code Changes', 'deadline': '2024-03-10', 'status': 1}
task3 = {'task_name': 'Prepare Presentation', 'deadline': '2024-03-20', 'status': 0}
task4 = {'task_name': 'Submit Weekly Report', 'deadline': '2024-03-12', 'status': 0}

tasks_list_u = [task1, task3, task4] # _u mean uncompleted task 
task_list_c = [task2]   # _c mean completed Task
all_task = tasks_list_u + task_list_c  # All task double list

def add():
    """
    Add New Task --name, date, status
    Every task is a dictionary that is then append into a new list
    """
    name = input("Enter the Task: ")
    date = input("Enter the Deadline: ")
    status = int(input("Enter 1 if it is Completed and 0 for Remaining: "))
    user_dict = {"Name": name, "Date": date, "Status": status}
    tasks_list_u.append(user_dict)

def remove():
    """
    Remove the task
    """
    r = int(input("Enter the index number: "))
    removing_item = r - 1
    # Check if the index is within the valid range
    if 0 <= removing_item < len(task_list_c):
        removed_task = task_list_c.pop(removing_item)
        print(f"Removed task: {removed_task}")
        print("Updated List:")
        for i, task in enumerate(task_list_c, start=1):
            print(f"{i}. {task}")
    else:
        print("Invalid index. Please enter a valid index.")
    

def update_status(tasks_list_u):
    """
    Update the status of a task in the task list.

    Parameters:
    - task_list (list): The list containing dictionaries of tasks.
    - task_index (int): The index (1-based) of the task to be updated.
    - new_status (int): The new status value (0 or 1) for the task.

    Returns:
    - None
    """
    # Display the current task list
    print("Current Task List:")
    for i, task in enumerate(tasks_list_u, start=1):
        print(f"{i}. {task['task_name']} (Status: {task['status']})")

    # Get user input for the task index and new status
    task_index = int(input("Enter the index of the task to update: "))
    new_status = int(input("Enter the new status (0 or 1): "))

    # # Call the update_status function
    # update_status(tasks_list_u, task_index, new_status)

    # Display the updated task list
    print("\nUpdated Task List:")
    for i, task in enumerate(tasks_list_u, start=1):
        print(f"{i}. {task['task_name']} (Status: {task['status']})")
    pass
    # new_status = input("Enter the Current Status: ")


def showAllTasksWithDetails(all_tasks):
    """
    Display all tasks with details.

    Parameters:
    - all_tasks (list): The list containing dictionaries of all tasks.

    Returns:
    - None
    """
    if not all_tasks:
        print("No tasks to display.")
    else:
        for i, task in enumerate(all_tasks, start=1):
            print(f"{i}. Task Name: {task['task_name']}")
            print(f"   Deadline: {task['deadline']}")
            print(f"   Status: {task['status']}")
            print("")

def deleteTask(all_tasks):
    """
    Display tasks and allow the user to delete a selected task.

    Parameters:
    - all_tasks (list): The list containing dictionaries of all tasks.

    Returns:
    - None
    """
    print("Select a task to delete:")
    showAllTasksWithDetails(all_tasks)

    try:
        choice = int(input("Enter the index of the task to delete (0 to cancel): "))
        
        if 0 < choice <= len(all_tasks):
            deleted_task = all_tasks.pop(choice - 1)
            print(f"Task '{deleted_task['task_name']}' has been deleted.")
        elif choice == 0:
            print("Operation canceled.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def showTask(all_tasks):
    """
    Display tasks based on user-selected options.

    Parameters:
    - all_tasks (list): The list containing dictionaries of all tasks.

    Returns:
    - None
    """
    print("Options:")
    print("1. Display all tasks")
    print("2. Display completed tasks")
    print("3. Display incompleted tasks")

    option = int(input("Enter your choice (1, 2, or 3): "))

    if option == 1:
        print("\nAll Tasks:")
        display_tasks(all_tasks)
    elif option == 2:
        print("Completed Tasks:")
        display_tasks(task_list_c)
    elif option == 3:
        print("Incompleted Tasks:")
        display_tasks(tasks_list_u)
    else:
        print("Invalid option. Please enter a valid choice (1, 2, or 3).")


def display_tasks(task_list):
    """
    Display tasks from the given task list.

    Parameters:
    - task_list (list): The list containing dictionaries of tasks.

    Returns:
    - None
    """
    if not task_list:
        print("No tasks to display.")
    else:
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task['task_name']} (Status: {task['status']})")


def deleteTask(all_tasks):
    """
    Display tasks and allow the user to delete a selected task.

    Parameters:
    - all_tasks (list): The list containing dictionaries of all tasks.

    Returns:
    - None
    """
    print("Select a task to delete:")
    showAllTasksWithDetails(all_tasks)

    try:
        choice = int(input("Enter the index of the task to delete (0 to cancel): "))
        
        if 0 < choice <= len(all_tasks):
            deleted_task = all_tasks.pop(choice - 1)
            print(f"Task '{deleted_task['task_name']}' has been deleted.")
        elif choice == 0:
            print("Operation canceled.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")



while True:
    choice = int(input("Enter The Number:\n1) Add Task \n2) Remove Task \n3) Update Task \n4) Delete \n5) Show Task\n*) Option:- "))
    if choice == 1:
        add()
    elif choice == 2:
        remove()
    elif choice == 3:
        update_status()
    elif choice == 4:
        deleteTask(all_task)  # No update to the list
    elif choice == 5:
        showTask(all_task)
    else:
        break