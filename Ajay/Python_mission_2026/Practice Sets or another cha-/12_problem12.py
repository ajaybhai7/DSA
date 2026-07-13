'''
90-100 = Ex
80-90  = A
70-80  = B
60-70  = C
50-60  = D
<50    = F '''

# Write a Program to caluculate the grade of a student from his marks from the following scheme

marks = int(input("Enter your marks > "))

if marks >= 90 <100:
    Grade = "A"

elif marks >= 80 <90:
    Grade = "B"

elif marks >= 70 <80:
    Grade = "C"

elif marks >= 60 <70:
    Grade = "D"

elif marks >= 50 <60:
    Grade = "E"

elif marks < 50:
    Grade = "F"
    
elif marks == 0 or marks < 0:
    print("Invalid marks!")

print(f'''Have a good day! 
Your Grade is : {Grade}
Your Marks is : {marks} ''')
