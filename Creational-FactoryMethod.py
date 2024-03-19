"""
Factory Method tasarım deseni, bir üst sınıftaki bir methodu 
alt sınıflara devrederek nesnelerin oluşturulmasını sağlar. 
Bu desen, alt sınıfların nesnelerin türlerini belirleyebileceği ve 
bu nesneleri oluşturabileceği bir yapı sağlar.
"""

from abc import ABC, abstractmethod

# Product: Abstract interface
class Cake(ABC):
    @abstractmethod
    def bake(self):
        pass

# Concrete Product: Chocolate Cake
class ChocolateCake(Cake):
    def bake(self):
        return "Çikolatalı pasta hazırlandı"

# Concrete Product: Vanilla Cake
class VanillaCake(Cake):
    def bake(self):
        return "Vanilyalı pasta hazırlandı"

# Creator: Abstract interface
class Bakery(ABC):
    @abstractmethod
    def create_cake(self):
        pass

    def order_cake(self):
        cake = self.create_cake()
        return cake.bake()

# Concrete Creator: Chocolate Bakery
class ChocolateBakery(Bakery):
    def create_cake(self):
        return ChocolateCake()

# Concrete Creator: Vanilla Bakery
class VanillaBakery(Bakery):
    def create_cake(self):
        return VanillaCake()

# Kullanım
def main():
    chocolate_bakery = ChocolateBakery()
    chocolate_cake = chocolate_bakery.order_cake()
    print(chocolate_cake)

    vanilla_bakery = VanillaBakery()
    vanilla_cake = vanilla_bakery.order_cake()
    print(vanilla_cake)

if __name__ == "__main__":
    main()