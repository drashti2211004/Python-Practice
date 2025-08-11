from abc import ABC,abstractmethod

class Employes(ABC):
    # abstract class

    def salary(self):
        pass


class drashti(Employes):
    def salary(self):
        return 10000


class parth(Employes):
    def salary(self):
        return 11000

obj = drashti()
print(obj.salary())

obj1 = parth()
print(obj1.salary())
