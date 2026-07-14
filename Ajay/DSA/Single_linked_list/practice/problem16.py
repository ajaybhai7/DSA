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
                to_do = tasks.append(input("Enter Task to add: "))
                with open("To_do_list.txt", 'w')as f:
                     f.write(to_do)

            elif user_choose == 2:
                    
                    with open("To_do_list.txt", 'r') as r:
                         read = r.read()

                    if read == "0": 
                        print("To do list khali hai !")

                    else:
                        with open("To_do_list.txt", 'r') as p:
                             to_do_print = p.read()
                             to_do_print = p.readlines()
                        for task in to_do_print:
                            print(f"Your tasks are\n{to_do_print}")

            elif user_choose == 3:

                with open ("To_do_list.txt", 'r') as l:
                     to_do_read_blank = l.read()

                if  to_do_read_blank == "":
                     print("To do list Khali hai !")
                
                
                else:
                    remove_task = input("Enter to remove task: ")
                    with open ("To_do_list.txt", 'a') as a:
                         append = a.write(remove_task)
                    
                    with open("To_do_list.txt", 'r') as x:
                         to_do_remove = x.read()
                    if (remove_task) in to_do_remove:
                        tasks.remove(remove_task)
                        print(f"Successfully remove {remove_task} task in to do list")
                
                    else:
                        print("Remove task list me nahi mila")

            else:
                break

        except ValueError:
             print("Enter Corect argument or Value")  
print("Thanks for using") 
    
