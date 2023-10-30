class Rectangle:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def get_area(self):
        return self.a*self.b
class Square:
    def __init__(self, a):
        self.a=a
    def get_area(self):
        return self.a**2
class Circle:
    def __init__(self, r):
        self.r=r
    def get_area(self):
        return 3.14*self.r**2
rect1=Rectangle(3, 4)
rect2=Rectangle(12, 3)
sql=Square(2)
circle=Circle(3)
figure=[rect1, rect2, sql, circle]
for figure in figure:
    print(figure.get_area())