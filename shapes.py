import shapes


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


rect = shapes.Rectangle(2, 4)
print(rect.area())
# 8

square = shapes.Square(8)
print(square.area())
# 64

print(square.perimeter())
# 32
