

class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

class Rectangle:
    
    def __init__(self,p1,p2):
        self.p1x=p1.x
        self.p1y=p1.y
        self.p2x=p2.x
        self.p2y=p2.y
        
    def get_area(self):
        return abs(self.p1x-self.p2x)*abs(self.p1y-self.p2y)
    def get_perimeter(self):
        return abs(self.p1x-self.p2x)*2+(self.p1y-self.p2y)*2
    def is_square(self):
        return bool(abs(self.p1x-self.p2x)==abs(self.p1y-self.p2y))
    

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
