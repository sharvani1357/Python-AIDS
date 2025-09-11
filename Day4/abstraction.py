from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(f"area of rectangle:",self.length*self.breadth)
class Circle(Shape):
    def __init__(self,pi,r):
        self.pi=pi
        self.r=r
    def area(self):
        print(f"area of circle:",self.pi*self.r*self.r)
rec=Rectangle(2,3)
cir=Circle(3.14,4)
rec.area()
cir.area()

