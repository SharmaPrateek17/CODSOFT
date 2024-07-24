
def task():
    tasks = []
    print("----Welcome To The Task Bar----")
    while True:
        print("\n1. Add Task\n2. Update Task\n3. Delete Task\n4. View Tasks\n5. Exit")
        operation = int(input("Choose an operation: "))

        if operation == 1:
            task_name = input("Enter task name: ")
            tasks.append(task_name)
            print(f"Task '{task_name}' has been successfully added")

        elif operation == 2:
            update_val = input("Enter the task name you want to update: ")
            if update_val in tasks:
                up = input("Enter new task name: ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"Task '{update_val}' has been updated to '{up}'")
            else:
                print("Task not found")

        elif operation == 3:
            del_val = input("Enter the task name you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted")
            else:
                print("Task not found")

        elif operation == 4:
            print("\nToday's Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

        elif operation == 5:
            print("Closing The Bar")
            break

        else:
            print("Invalid Input")

task()
