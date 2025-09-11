class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"name of the employee:{self.name} salary:{self.salary}")
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
    def display(self):
        print(f"name of the employee:{self.name} salary:{self.salary} department:{self.department}")
e1=Manager("shivani",60000,"csedatascience")
e2=Employee("sharvani",95000)
e1.display()
e2.display()

