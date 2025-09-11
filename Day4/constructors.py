class student:
    def __init__(self,name,marks,roll):
        self.name=name
        self.marks=marks
        self.roll=roll
    def display(self):
        print(f"name:{self.name} marks:{self.marks} roll={self.roll}")
s1=student("sharvani",98,2)
s2=student("shanmukh",99,1)
s1.display()
s2.display()