


class Rectangle():
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
     
    
    def perimeter(self):
        return ((self.length + self.width) * 2)
    
class Square(Rectangle):
    def __init__(self, side: int):
            super().__init__(side, side)