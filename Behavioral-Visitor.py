"""
Visitor tasarım deseni, bir nesne yapısını dolaşmak için 
bir ziyaretçi nesnesi kullanır. Bu desen, yeni işlevsellik eklemeyi kolaylaştırır çünkü 
yeni işlevselliği eklemek için yeni bir ziyaretçi sınıfı oluşturabiliriz. 
Ayrıca, eleman sınıflarını değiştirmeden farklı işlevselliği uygulamamıza olanak tanır.
"""

from abc import ABC, abstractmethod

# Element: Eleman (Soyut)
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# ConcreteElement: Somut Elemanlar
class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

# Visitor: Ziyaretçi (Soyut)
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element_a):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element_b):
        pass

# ConcreteVisitor: Somut Ziyaretçi
class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element_a):
        print("ConcreteVisitor is visiting ConcreteElementA")

    def visit_concrete_element_b(self, element_b):
        print("ConcreteVisitor is visiting ConcreteElementB")

# ObjectStructure: Nesne Yapısı
class ObjectStructure:
    def __init__(self):
        self._elements = []

    def attach(self, element):
        self._elements.append(element)

    def detach(self, element):
        self._elements.remove(element)

    def accept(self, visitor):
        for element in self._elements:
            element.accept(visitor)

# Kullanım
def main():
    # Elemanlar oluştur
    element_a = ConcreteElementA()
    element_b = ConcreteElementB()

    # Ziyaretçi oluştur
    visitor = ConcreteVisitor()

    # Nesne yapısı oluştur
    object_structure = ObjectStructure()
    object_structure.attach(element_a)
    object_structure.attach(element_b)

    # Ziyaretçi, nesne yapısını ziyaret etsin
    object_structure.accept(visitor)

if __name__ == "__main__":
    main()
