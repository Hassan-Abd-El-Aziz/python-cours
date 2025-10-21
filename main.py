from abc import ABCMeta,abstractmethod

class programin(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass
    def goo(self):
        return "good"
class python(programin):
    def has_oop(self):
        return "Yes"


one=python()
print(one.has_oop())
print(one.goo())