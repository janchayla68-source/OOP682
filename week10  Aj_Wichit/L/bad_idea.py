class Retangle:
    def __init__(self,windth,height):
        self.windth = windth
        self.height = height

    def set_windth(self,windth):
        self.windth = windth

    def set_heigth(self,heigth):
        self.height = heigth

class Squarel(Retangle):
    def __init__(self, windth, height):
        super().__init__(windth, height)
    def set_windth(self,windth):
        self.windth = windth
        self.heigth = windth
    def set_heigth(self, heigth):
        self.height = heigth
        self.windth = heigth
def resize_rectangle(rectangle,new_windth,new_heigth):
    rectangle.set_heigth(new_heigth)
    rectangle.set_windth(new_windth)
    return rectangle.windth * rectangle.height