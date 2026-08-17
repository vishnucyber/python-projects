def task():
    tasks = []
    print("Welocme to the Task Manager.")

    total_task = int(input("How many tasks you wnat to add: "))
    for i in range(1,total_task + 1):
        task_name = input(f"Enter task {i}: = ")
        tasks.append(task_name)


    print(f"Today's task are\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add \n2-update\n3-Delete\n4-View\n5-Exit:  "))
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f" Task {add} has been added")

        elif operation == 2:
            updated_val = input("Enter the task name to update: ")
            if updated_val in tasks:
                up  = input("Enter new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
            

                print(f"Update task {up}")

        elif operation == 3:
            del_val = input("Ehich task you want to delete: ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} is deleted")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("The End...")
            break

        else:
            print(f" {operation} is an invalid input,try again")

task()