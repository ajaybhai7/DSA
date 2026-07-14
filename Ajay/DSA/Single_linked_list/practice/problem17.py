# Writing problem 16 in another way

tasks = []

# --- APP START HOTE HI FILE SE DATA LIST MEIN DAALNA ---
try:
    with open("To_do_list.txt", "r") as f:
        saari_lines = f.readlines()
        for line in saari_lines:
            tasks.append(line.strip())
except FileNotFoundError:
    pass 

# --- SHORTCUT FUNCTION (List ko file me save karne ke liye) ---
def save_to_file():
    with open("To_do_list.txt", "w") as f:
        for t in tasks:
            f.write(t + "\n")

# --- MAIN APP LOOP ---
while True:
    try:
        print("\n1. Add task\n2. View task\n3. Delete task\n4. Exit")
        user_choose = int(input("Task -> "))

        if user_choose == 1:
            naya_task = input("Enter Task to add: ")
            tasks.append(naya_task)
            save_to_file() # Shortcut use kiya

        elif user_choose == 2:
            if len(tasks) == 0:
                print("To do list khali hai!")
            else:
                for task in tasks:
                    print(f"- {task}")

        elif user_choose == 3:
            if len(tasks) == 0:
                print("List khali hai!")
            else:
                remove_task = input("Enter to remove task: ")
                if remove_task in tasks:
                    tasks.remove(remove_task)
                    save_to_file() # Shortcut use kiya
                    print(f"Successfully removed '{remove_task}'")
                else:
                    print("Task nahi mila!")

        elif user_choose == 4:
            break

    except ValueError:
        print("Please enter a valid number!")

print("Thanks for using!")