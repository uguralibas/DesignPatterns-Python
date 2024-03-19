"""
Template Method tasarım deseni, 
bir sürecin yapısını belirleyen ancak bazı adımların 
alt sınıflar tarafından uygulanmasına izin veren bir yapı sağlar. 
Bu desen, bir algoritmanın genel yapısını tanımlamak ve 
alt sınıflar aracılığıyla belirli adımları özelleştirmek için kullanılır.
"""

from abc import ABC, abstractmethod

# AbstractClass: Soyut Sınıf
class AbstractClass(ABC):
    # Template method
    def template_method(self):
        self.operation1()
        self.operation2()

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

# ConcreteClass: Somut Sınıflar
class ConcreteClassA(AbstractClass):
    def operation1(self):
        print("ConcreteClassA: Operation 1")

    def operation2(self):
        print("ConcreteClassA: Operation 2")

class ConcreteClassB(AbstractClass):
    def operation1(self):
        print("ConcreteClassB: Operation 1")

    def operation2(self):
        print("ConcreteClassB: Operation 2")

# Kullanım
def main():
    # ConcreteClassA için template method çağrısı
    a = ConcreteClassA()
    a.template_method()

    print("-" * 20)

    # ConcreteClassB için template method çağrısı
    b = ConcreteClassB()
    b.template_method()

if __name__ == "__main__":
    main()