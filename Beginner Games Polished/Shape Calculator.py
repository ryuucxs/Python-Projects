from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.sqrt((math.pi * self.radius))

    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt((s * (s - self.side1) * (s - self.side2) * (s - self.side3)))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Example usage:
shapes = [
    Rectangle(4, 5),
    Circle(3),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(shape.area())
    