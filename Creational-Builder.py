"""
Builder tasarım deseni, karmaşık nesnelerin adım adım oluşturulmasını sağlar ve 
farklı oluşturma adımlarını sarmalar. Bu tasarım deseni, 
nesne oluşturma sürecini basitleştirmek ve daha okunabilir, 
esnek kod oluşturmak için kullanılır.
"""

from abc import ABC, abstractmethod

# Product: Pizza
class Pizza:
    def __init__(self):
        self.size = None
        self.dough = None
        self.toppings = []

    def __str__(self):
        return f"Pizza (Boyut: {self.size}, Hamur: {self.dough}, Toppings: {', '.join(self.toppings)})"

# Builder: Abstract interface
class PizzaBuilder(ABC):
    @abstractmethod
    def set_size(self):
        pass

    @abstractmethod
    def set_dough(self):
        pass

    @abstractmethod
    def add_topping(self):
        pass

    @abstractmethod
    def get_pizza(self):
        pass

# Concrete Builder: Margherita Pizza
class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self):
        self.pizza.size = "Orta"

    def set_dough(self):
        self.pizza.dough = "İnce"

    def add_topping(self):
        self.pizza.toppings.append("Mozzarella")
        self.pizza.toppings.append("Domates")

    def get_pizza(self):
        return self.pizza

# Director: PizzaOrder
class PizzaOrder:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        self.builder.set_size()
        self.builder.set_dough()
        self.builder.add_topping()
        return self.builder.get_pizza()

# Kullanım
def main():
    margherita_builder = MargheritaPizzaBuilder()
    order = PizzaOrder(margherita_builder)
    margherita_pizza = order.make_pizza()
    print(margherita_pizza)

if __name__ == "__main__":
    main()
