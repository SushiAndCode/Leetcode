
class Rectangle():
    def __init__(self, base: int, height: int):
        
        self.base = base
        self.height = height

    def Area(self):
        return self.base * self.height

    def Perimeter(self):
        return self.base*2 + self.height*2

rectangle = Rectangle(3,5)

print(rectangle.Area())
print(rectangle.Perimeter())