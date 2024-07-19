# To-do List program

tasks = []
total_task = int(input("Enter how many task you want to add = "))
for i in range(1, total_task+1):
 task_name = input(f"Enter task {i} = ")
tasks.append(task_name)
print(f"Today's tasks are{tasks}")

while True:
    
    print("---- To-Do List----- ")

    print("1. Add task")
    print("2. Update task")
    print("3. View tasks")
    print("4. Delete task")
    print("5. Quit")

    choice = input("Choose  an option = ")

    # Add task
    if choice == "1":
        task = input("Enter Tasks you want to add = ")
        tasks.append(task)
        print("Task added!")

    # Update tasks
    elif choice == "2":
        task = input("Enter the task name you want to update =")
        tasks.append(task)
        print("Task update")

    # View tasks
    elif choice == "3":
        print("Your tasks:")
        for task in tasks:
            print(task)

 # Delete task
    elif choice == "4":
        task = input("Which task you want to delete = ")
        if task in tasks:
            tasks.remove(task)
            print("Task deleted!")
        else:
            print("Task not found!")

    # Quit
    elif choice == "5":
        break

    # Invalid input
    else:
        print("Invalid choice!")
