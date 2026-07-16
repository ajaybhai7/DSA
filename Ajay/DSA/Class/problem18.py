class StudentProfile:
    def __init__(self, student_name):
        self.name = student_name
        self.marks = {}

    def add_marks(self, subject, score):
        self.marks[subject] = score

    def show_result(self):
        print(f'''
{self.name} ke Score hai: {self.marks}''')
        
s1 = StudentProfile("Ajay")
s1.add_marks(subject = input("Enter Subject Name: "), score = input("Enter Score: "))
s1.show_result()

