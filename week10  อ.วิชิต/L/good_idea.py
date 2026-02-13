
from abc import abstractclassmethod

from numpy import resize, shape

class Shape:
    @abstractclassmethod
    def resize(self, new_windth, new_heigth):
        pass
    def area(self):
        pass

class Retangle(Shape):
    def __init__(self,windth,height):
        self.windth = windth
        self.height = height

    def resize(self, new_windth, new_height):
        self.windth = new_windth
        self.height = new_height

    def area(self):
        return self.windth * self.height

class Squarel(Shape):
    def __init__(self, windth):
        self.side = windth
    def resize(self, new_windth, new_heigth):
        self.side = new_windth
    def area(self):
        return self.side * self.side
def resize_rectangle(rectangle,new_windth,new_heigth):
    shape.resize(new_windth,new_heigth)
    return shape.area()
rec = Retangle(2,3)
resize(rec,4,5)
print("Retangle area:", rec.area())
square = Squarel(3)
resize(square,4,5)

