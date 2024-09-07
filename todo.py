def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")
    
def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("Your tasks")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(index):
    try:
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' deleted!")
    except IndexError:
        print("Invalid task number!")

tasks = []

while True:
    print("\nOptions: \n1. Add Task  \n2. View Tasks  \n3. Delete Task  \n4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_num = int(input("Enter task number to delete: "))
        delete_task(task_num)
    elif choice == '4':
        print(".........")
        break
    else:
        print("Invalid option, try again!")
