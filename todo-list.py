tasks=[]

while True:
    print("\n=========To Do List=========")
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice==1:
        task_name=input("Enter your task:")
        task={
            "task":task_name,
            "completed":False
        }
        tasks.append(task)
        print("Task Added Successfully")
    
    elif choice==2:
        if len(tasks)==0:
            print("No tasks available")
        
        else:
            print("\n========TASKS========")
            for index,task in enumerate(tasks,start=1):
                if task["completed"]:
                    status="[✓]"
                else:
                    status="[ ]"
                    
                print(f"{index}.{status} {task['task']}")
                
    
    elif choice==3:
        
        if len(tasks)==0:
            print("No tasks available")
        
        else:
            
            print("\n======= TASKS =======")
            for index,task in enumerate(tasks,start=1):
                status="[✓]" if task["completed"] else "[ ]"
                print(f"{index}. {status} {task['task']}")
            
            task_number=int(input("Enter task number to complete"))
            if 1<= task_number <=len(tasks):
                tasks[task_number-1]["completed"]=True
                print("Task marked as completed!")
            
            else:
                print("Invalid task number")
    
    elif choice==4:
        if len(tasks)==0:
            print("No task available")
        
        else:
            print("\n======= TASKS =======")

            for index,task in enumerate(tasks,start=1):
                status="[✓]" if task["completed"] else "[ ]"
                print(f"{index}. {status} {task['task']}")
            
            task_number=int(input("Enter the task number to delete: "))
            if 1<=task_number<=len(tasks):
                deleted_task=tasks.pop(task_number-1)
                print(f"'{deleted_task['task']}' deleeted successfully")
            
            else:
                print("Invalid task number")
    
    elif choice==5:
        print("GoodBye!")
        break

    else:
        print("Invalid Choice! Please try again...")
    
    
    
        