# To do list

tasks = []

while True:

    print('''
1. Add task
2. view task
3. Delete task
4. Exit''')
    
    user_choose = int(input("Taks -> ").lower())

    if user_choose == 1:
        tasks.append(input("Enter Task to add: "))

    elif user_choose == 2:
        for task in tasks:
            print(f"Your tasks are\n{tasks}")

    elif user_choose == 3:
        tasks.remove(input("Enter to remove task: "))
        print(f"Successfully remove task in to do list")

    else:
        break
print("Thanks for using")