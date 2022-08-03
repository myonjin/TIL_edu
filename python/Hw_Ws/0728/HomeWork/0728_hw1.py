


class Circle:
    pi = 3.14
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
    
    def area(self):
        return Circle.pi * self.r * self.r
    
    def circumference(self):
        return 2 * Circle.pi * self.r
    
    def center(self):
        return (self.x, self.y)
    
won=Circle(3,2,4)

print(won.area())
print(won.circumference())
print(won.center())

# r=3 x=2 y=4