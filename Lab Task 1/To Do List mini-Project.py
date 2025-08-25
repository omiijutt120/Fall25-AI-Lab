tasks = []
while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
             print(f"{i+1}. {tasks[i]}")
    elif choice == "3":
        if not tasks:
            print("No tasks to remove!")
        else:
            for i in range(len(tasks)):
             print(f"{i+1}. {tasks[i]}")
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num-1)
                print("Task removed!")
            else:
                print("Invalid task number!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
