## Todo List Application:
# Add, Remove, update, Delete
print("Todo List App".center(77, " "))

# Four Example of each task and then we store each in another list.
task1 = {'task_name': 'Complete Project Proposal', 'deadline': '2024-03-15', 'status': 0}
task2 = {'task_name': 'Review Code Changes', 'deadline': '2024-03-10', 'status': 1}
task3 = {'task_name': 'Prepare Presentation', 'deadline': '2024-03-20', 'status': 0}
task4 = {'task_name': 'Submit Weekly Report', 'deadline': '2024-03-12', 'status': 0}
task5 = {'task_name': 'Create Monthly Budget', 'deadline': '2024-03-25', 'status': 1}
task6 = {'task_name': 'Read New Book', 'deadline': '2024-04-05', 'status': 1}
task7 = {'task_name': 'Attend Team Meeting', 'deadline': '2024-03-18', 'status': 0}

all_task = [task1 , task2 , task3 , task4 , task5 , task6 , task7]  # All task double list
# Lists to store tasks, u for uncompleted, c for completed
task_list_u = [task for task in all_task if task['status'] == 0]
task_list_c = [task for task in all_task if task['status'] == 1]


def add():
    global all_task, task_list_c, tasks_list_u
    name = input("Enter the Task: ")
    deadline = input("Enter the Deadline: ")
    status = int(input("Enter 1 if it is Completed and 0 for Remaining: "))
    new_task = {'task_name': name, 'deadline': deadline, 'status': status}
    all_task.append(new_task)

    if status == 1:
        task_list_c.append(new_task)
    else:
        task_list_u.append(new_task)

'''
def update_status(all_task, task_list_u):
    """
    Update the status of a task in the task list.

    Parameters:
    - all_task (list): The list containing dictionaries of all tasks.
    - task_list_u (list): The list containing dictionaries of incompleted tasks.

    Returns:
    - None
    """
    # Display the current task list
    print("Current Task List:")
    for i, task in enumerate(task_list_u, start=1):
        print(f"{i}. {task['task_name']} (Status: {task['status']})")

    # Get user input for the task index and new status
    task_index = int(input("Enter the index of the task to update: "))
    new_status = int(input("Enter the new status (0 or 1): "))

    # Remove the old version of the task from all_task
    old_task = task_list_u.pop(task_index - 1)
    all_task.remove(old_task)

    # Update the status of the selected task in both all_task and task_list_u
    old_task['status'] = new_status
    task_list_c.append(old_task)
    all_task.append(old_task)
    
    # Display the updated task list
    print("\nUpdated Task List:")
    for i, task in enumerate(task_list_u, start=1):
        print(f"{i}. {task['task_name']} (Status: {task['status']})")

'''
def update_status(all_task, task_list_u, task_list_c):
    """
    Update the status of a task in the task list.

    Parameters:
    - all_task (list): The list containing dictionaries of all tasks.
    - task_list_u (list): The list containing dictionaries of incompleted tasks.
    - task_list_c (list): The list containing dictionaries of completed tasks.

    Returns:
    - None
    """
    # Display the current task list
    print("Current Task List:")
    for i, task in enumerate(task_list_u, start=1):
        print(f"{i}. {task['task_name']} (Status: {task['status']})")

    # Get user input for the task index
    while True:
        try:
            task_index = int(input("Enter the index of the task to update: "))
            if 1 <= task_index <= len(task_list_u):
                break
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get user input for the new status
    while True:
        try:
            new_status = int(input("Enter the new status (0 or 1): "))
            if new_status in [0, 1]:
                break
            else:
                print("Invalid status. Please enter 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Remove the old version of the task from all_task
    old_task = task_list_u.pop(task_index - 1)
    all_task.remove(old_task)

    # Update the status of the selected task in both all_task and task_list_u
    old_task['status'] = new_status
    task_list_c.append(old_task)
    all_task.append(old_task)

    # Display the updated task list
    print("\nUpdated Task List:")
    for i, task in enumerate(task_list_u, start=1):
        print(f"{i}. {task['task_name']} (Status: {task['status']})")



def showAllTasksWithDetails(all_task):
    """
    Display all tasks with details.

    Parameters:
    - all_tasks (list): The list containing dictionaries of all tasks.

    Returns:
    - None
    """
    if not all_task:
        print("No tasks to display.")
    else:
        for i, task in enumerate(all_task, start=1):
            print(f"{i}. Task Name: {task['task_name']}")
            print(f"   Deadline: {task['deadline']}")
            print(f"   Status: {task['status']}")
            print("")

def deleteTask(all_task):
    """
    Display tasks and allow the user to delete a selected task.

    Parameters:
    - all_tasks (list): The list containing dictionaries of all tasks.

    Returns:
    - None
    """
    print("Select a task to delete:")
    showAllTasksWithDetails(all_task)

    try:
        choice = int(input("Enter the index of the task to delete (0 to cancel): "))
        if 0 < choice <= len(all_task):
            deleted_task = all_task.pop(choice - 1)
            
            # Check if the deleted task is in task_list_u and remove it
            if deleted_task in task_list_u:
                task_list_u.remove(deleted_task)
            
            # Check if the deleted task is in task_list_c and remove it
            elif deleted_task in task_list_c:
                task_list_c.remove(deleted_task)
            
            print(f"Task '{deleted_task['task_name']}' has been deleted.")
        elif choice == 0:
            print("Operation canceled.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def showTask(all_task):
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
        display_tasks(all_task)
    elif option == 2:
        print("\nCompleted Tasks:")
        display_tasks(task_list_c)
    elif option == 3:
        print("\nIncompleted Tasks:")
        display_tasks(task_list_u)
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
            task_name = task.get('task_name') or task.get('Name', 'N/A')
            status = task['status']  # Get the status directly from the task dictionary
            print(f"{i}. Task Name: {task_name}")
            print(f"   Status: {status}")
            print("")


while True:
    try:
        choice = int(input("Enter The Number:\n1) Add Task \n2) Update Task \n3) Delete Task \n4) Show Task\n5) Show All Task With Detail\n6) Exit The Program\n*) Option:- "))
        if choice == 1:
            add()
        elif choice == 2:
            update_status(all_task, task_list_u, task_list_c)
        elif choice == 3:
            deleteTask(all_task, task_list_u, task_list_c)
        elif choice == 4:
            showTask(all_task)
        elif choice == 5:
            showAllTasksWithDetails(all_task)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")