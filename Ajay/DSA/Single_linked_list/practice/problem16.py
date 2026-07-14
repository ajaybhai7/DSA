# To do list

tasks = []

while True:

    print('''
1. Add task
2. view task
3. Delete task
4. Exit''')
    
    user_choose = input("Taks -> ").lower()

    if user_choose == "Add task" and 1:
        tasks.append(input("Enter Task to add: "))

    elif user_choose == "view task" and 2:
        for task in tasks():
            print(tasks)

    elif user_choose == "Delete task" and 3:
        tasks.remove()

    else:
        break
print("Thanks for using")