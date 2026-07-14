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
                to_do = (input("Enter Task to add: "))
                with open("To_do_list.txt", 'a')as f:
                     f.write(f"\n{to_do}")

            elif user_choose == 2:
                    
                    with open("To_do_list.txt") as f:
                        file = f.read()
                        if file == "": 
                            print("To do list khali hai !")

                        else:
                            print(f"Your tasks are\n{file}")

            # Option 3 (Delete) bas itna chota ho jayega:
            elif user_choose == 3:
                if len(tasks) == 0:
                    print("To do list khali hai!")
                else:
                    remove_task = input("Enter to remove task: ")
                    if remove_task in tasks:
                        tasks.remove(remove_task) # Sidha list se hataya (1 line)
                        
                        # Ab nayi list ko file mein daal do (Overwrite)
                        with open("To_do_list.txt", 'w') as f:
                            for t in tasks:
                                f.write(t + "\n")
                                
                        print(f"Successfully removed {remove_task}")
                    else:
                        print("Task nahi mila")

            else:
                break

        except ValueError:
             print("Enter Corect argument or Value")  
print("Thanks for using") 