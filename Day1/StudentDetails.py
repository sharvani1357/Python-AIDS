std_Number=int(input("StudentNumber="))
std_Name=input("StudentName=")
Maths,physics,chemistry=map(int,input("Enter marks of Maths,Physics,Chemistry:").split())
total=Maths+physics+chemistry
average=total/3
print(f"Total={total:.2f}")
print(f"Average={average:.2f}")
print("STUDENT DETAILS:")
print(f"Student Number: {std_Number}\nStudent Name: {std_Name}\nMaths Marks: {Maths}\nPhysics Marks: {physics}\nChemistry Marks: {chemistry}\nTotal Marks: {total:.2f}\nAverage Marks: {average:.2f}")