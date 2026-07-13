# write a program to take inpute marks or subject from the user and print their totl marks 
#  and etire dictonari

def student():
    dict = {}
    total_marks = 0
    sub = ["Hindi", "English", "Math"]
    for Subject in sub:
        marks = int(input(f"Enter Number in {Subject}: \n"))
        dict[Subject] = marks
        total_marks += marks

    print(f"Your dictonary is : {dict}")
    print(f"Total marks is : {total_marks}")
student()