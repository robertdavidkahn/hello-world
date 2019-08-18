from abc import abstractmethod

class Shape:
    def __init__(self, name):
        self.name_ = name
        super().__init__()
    
    @abstractmethod
    def draw(self):
        pass

    def name(self):
        return self.name_

#--------------------------------------------
class Circle(Shape):
    def __init__(self, name):
        Shape.__init__(self, "Cirlce_" + name)

    def draw(self):
        print("Drawing " + Shape.name(self))


#--------------------------------------------
class Square(Shape):
    def __init__(self, name):
        Shape.__init__(self, "Square_" + name)

    def draw(self):
        print("Drawing " + Shape.name(self))
