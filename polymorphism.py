# polymorphism allows different objects to respond to the same method in their own way


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2
class Square(Shape):
    def __init__(self,side):
        self.side= side
    def area(self):
        return self.side*self.side

#Creating Objects
shape=[Circle(5),Square(4)]
for i in shape:
    print("Area is",i.area())
