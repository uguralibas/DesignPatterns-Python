"""
Abstract(soyut) Factory tasarım deseni, birbirine bağımlı nesnelerin ailesini oluşturmak için kullanılır ve 
bu nesnelerin nasıl oluşturulacağını gizler. Bir Abstract Factory, ilgili nesnelerin 
bir ailesini oluşturan ve bu nesnelerin nasıl oluşturulacağını tanımlayan bir arayüz sağlar. 
Ardından, somut fabrika sınıfları, bu arayüzü uygular ve belirli bir nesne ailesini oluşturur.
"""

from abc import ABC, abstractmethod

#---------------------------------------------------#
# Abstract Factory arayüzü
class AbstractFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass

    @abstractmethod
    def create_color(self):
        pass

# Somut fabrika sınıfı - Kırmızı şekiller
class RedShapeFactory(AbstractFactory):
    def create_shape(self):
        return Square()

    def create_color(self):
        return Red()

# Somut fabrika sınıfı - Mavi şekiller
class BlueShapeFactory(AbstractFactory):
    def create_shape(self):
        return Circle()

    def create_color(self):
        return Blue()

#---------------------------------------------------#
# Abstract Product arayüzü
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete Product - Kare
class Square(Shape):
    def draw(self):
        return "Kare çizildi"

# Concrete Product - Daire
class Circle(Shape):
    def draw(self):
        return "Daire çizildi"

#---------------------------------------------------#
# Abstract Product arayüzü
class Color(ABC):
    @abstractmethod
    def fill(self):
        pass

# Concrete Product - Kırmızı
class Red(Color):
    def fill(self):
        return "Kırmızı ile boyandı"

# Concrete Product - Mavi
class Blue(Color):
    def fill(self):
        return "Mavi ile boyandı"

# Kullanım
def main():
    # Kırmızı şekilleri oluştur
    red_factory = RedShapeFactory()
    red_shape = red_factory.create_shape()
    red_color = red_factory.create_color()
    print(red_shape.draw())
    print(red_color.fill())

    # Mavi şekilleri oluştur
    blue_factory = BlueShapeFactory()
    blue_shape = blue_factory.create_shape()
    blue_color = blue_factory.create_color()
    print(blue_shape.draw())
    print(blue_color.fill())

if __name__ == "__main__":
    main()