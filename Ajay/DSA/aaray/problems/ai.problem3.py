import numpy as np

Student_marks = np.array([[45, 54, 78, 68], # Student 1 marks
                          [67, 76, 56, 89], # Student 2 marks
                          [54, 76, 87, 56]]) # Student 3 marks

def highx_score():
    roll_no = 1
    print("\n------- Maximum Score --------")
    for student in Student_marks:
        print(f'''Student {roll_no} Highest Marks -> {(np.max(student))}''')
        roll_no += 1
        if len(student) == roll_no:
            print("")

def min_score():
    roll_no = 1
    print("--------- Min Score ---------")
    for student in Student_marks:
        print(f'''Student {roll_no} Min Marks -> {(np.max(student))}''')
        roll_no +=1
        if len(student) == roll_no:
            print("")

def avg_score():
    roll_no = 1
    print("-------- Average Score --------")
    for student in Student_marks:
        print(f"Student {roll_no} Average Marks -> {(np.mean(student))}")
        roll_no += 1
        if len(student) == roll_no:
            print("\n")

highx_score()
min_score()
avg_score()

# Bina kisi loop ke har student ka highest, lowest aur average!
print("Sabhi students ka Highest:", np.max(Student_marks, axis=1))
print("Sabhi students ka Lowest:", np.min(Student_marks, axis=1))
print("Sabhi students ka Average:", np.mean(Student_marks, axis=1))
