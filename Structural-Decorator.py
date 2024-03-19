"""
Decorator tasarım deseni, bir nesneye dinamik olarak ek işlevsellik eklemeyi sağlar. 
Bu desen, bir nesneyi sarmalayarak (wrapper) ve 
bu nesneye ek işlevsellik ekleyerek çalışır.
"""

from abc import ABC, abstractmethod

# Component: Abstract
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

# Concrete Component: Basit kahve
class SimpleCoffee(Coffee):
    def cost(self):
        return 10

# Decorator: Abstract
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete Decorator: Süt ekleyen kahve
class Milk(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def cost(self):
        return self._coffee.cost() + 5

# Concrete Decorator: Şeker ekleyen kahve
class Sugar(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def cost(self):
        return self._coffee.cost() + 3

# Kullanım
def main():
    # Basit kahve oluştur
    coffee = SimpleCoffee()

    # Kahveye süt ekleyerek yeni bir kahve oluştur
    coffee_with_milk = Milk(coffee)

    # Kahveye süt ve şeker ekleyerek yeni bir kahve oluştur
    coffee_with_milk_and_sugar = Sugar(coffee_with_milk)

    # Diğer
    coffee_2 = SimpleCoffee()
    coffee_with_sugar = Sugar(coffee_2)

    # Kahve fiyatlarını listele
    print("Basit Kahve: ", coffee.cost())
    print("Süt Eklenmiş Kahve: ", coffee_with_milk.cost())
    print("Süt ve Şeker Eklenmiş Kahve: ", coffee_with_milk_and_sugar.cost())
    print("Şeker Eklenmiş Kahve: ", coffee_with_sugar.cost())

if __name__ == "__main__":
    main()
