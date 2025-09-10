def student_details(n):
    students=[]
    for i in range(n):
        name=input("enter name:")
        roll=int(input("enter roll number:"))
        marks=float(input("enter marks:"))
        tup=(name,roll,marks)
        students.append(tup)
    return students
def max_std(students):
    max=students[0][2]
    for i in range(len(students)):
        if students[i][2]>max:
            max=students[i][2]
    return max
def greater_std(students):
    max_marks=max_std(students)
    for i in range(len(students)):
        if students[i][2]>75:
            return students[i]
n=int(input("enter number of students:"))
students=student_details(n)
print("max marks is:",max_std(students))
print("students with marks greater than 75:",greater_std(students))
