from abc import abstractmethod

class Vehicle:
    def __init__(self, name):
        self.name_ = name
        super().__init__()

    @abstractmethod
    def startEngine(self):
        pass

    @abstractmethod
    def stopEngine(self):
        pass

    @abstractmethod
    def goForward(self):
        pass

    @abstractmethod
    def goReverse(self):
        pass




