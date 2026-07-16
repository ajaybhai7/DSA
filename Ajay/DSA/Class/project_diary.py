from datetime import datetime
def add(txt):
    Diary = "Diary.txt"
    with open(Diary, 'a') as f:
        aaj_ki_date = datetime.now().strftime("%Y-%m-%d- %H:%M")
        f.write(f"[{aaj_ki_date}] {txt}\n")
def view():
    diary = "Diary.txt"
    try:
        with open(diary, 'r') as f:
            read = f.readlines()
            # Agar file khali hai
            if len(read) == 0:
                print("Diary bilkul khali hai!")
            else:
                for txt in read:
                    # strip() lagane se extra space nahi aata
                    print(txt.strip()) 
    except FileNotFoundError:
        print("Abhi tak koi diary nahi bani hai.")

def delete(line_to_delete):
    Diary = "Diary.txt"

    try:
        with open(Diary, 'r') as f:
            lines = f.readlines()

        with open(Diary, 'w') as f:
            deleted = False

            for line in lines:
                if line_to_delete not in line:
                    f.write(line)

                else:
                    deleted = True

            if deleted:
                print(f"'{line_to_delete}' wali line delete ho gayi. ") 

            else:
                print("aisi koi line nahi mili")

    except FileNotFoundError:
        print("Abhi tak koi diary nahi bani hai!")

# Main menu

while True:
    print('''
--- MY DIARY 
1. Add new
2. View Diary
3. Delete Line
4. Exit
''')
    
    try:
        choose = int(input("Enter Option -> "))
        if choose == 1:
            a = input("Enter text to add in Diary: ")
            add(a)
            print("Successfull Added")

        elif choose == 2:
            print("\n---- Aapki Diary ----")
            view()
            print("----------------------")

        elif choose == 3:
            line = input("Enter txt to delete From Diary: ")
            delete(line)


        elif choose == 4:
            print("Diary Closed. By!")
            break

    except ValueError:
        print("Please Enter a Valid Number (1-4).")
            

