# To do list
tasks = []

while True:
        try:

            print('''
        1. Add task
        2. view task
        3. Delete task
        4. Exit''')
            
            user_choose = int(input("Taks -> ").lower())

            if user_choose == 1:
                tasks.append(input("Enter Task to add: "))

            elif user_choose == 2:
                

                    if tasks == "": 
                        print("To do list is empty Now!")

                    else:
                        for task in tasks:
                            print(f"Your tasks are\n{tasks}")

            elif user_choose == 3:
                remove_task = input("Enter to remove task: ")
                if remove_task in tasks:
                     
                    tasks.remove(remove_task)
                    print(f"Successfully remove {remove_task} task in to do list")
                else:
                    print("Task not exist in to do list")

            else:
                break

        except ValueError:
             print("Enter Corect argument or Value")  
print("Thanks for using") 
        
    
