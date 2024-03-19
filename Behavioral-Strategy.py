"""
Strategy tasarım deseni, algoritmayı sınıflara kapsülleyerek, 
algoritmanın kullanıldığı bağlamın değiştirilmesini sağlar. 
Bu, kodun daha modüler, esnek ve bakımı daha kolay hale gelmesini sağlar. 
Örneğin, bir hesap makinesi uygulamasında farklı matematiksel işlemler için 
aynı arayüzü sağlayarak, istenen işlemi dinamik olarak değiştirebiliriz.
"""

from abc import ABC, abstractmethod

# Strategy: Strateji (Soyut)
class Strategy(ABC):
    @abstractmethod
    def execute(self, num1, num2):
        pass

# ConcreteStrategy: Somut Stratejiler
class AddStrategy(Strategy):
    def execute(self, num1, num2):
        return num1 + num2

class SubtractStrategy(Strategy):
    def execute(self, num1, num2):
        return num1 - num2

class MultiplyStrategy(Strategy):
    def execute(self, num1, num2):
        return num1 * num2

class DivisionStrategy(Strategy):
    def execute(self, num1, num2):
        return num1 / num2

# Context: Bağlam
class Calculator:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, num1, num2):
        return self._strategy.execute(num1, num2)

# Kullanım
def main():
    # Stratejileri oluştur
    add_strategy = AddStrategy()
    subtract_strategy = SubtractStrategy()
    multiply_strategy = MultiplyStrategy()
    division_strategy = DivisionStrategy()

    # Bağlam oluştur
    calculator = Calculator(add_strategy)
    result = calculator.execute_strategy(5, 3)
    print("Add result:", result)

    # Stratejiyi değiştir ve hesaplamaları yap
    calculator.set_strategy(subtract_strategy)
    result = calculator.execute_strategy(5, 3)
    print("Subtraction result:", result)

    calculator.set_strategy(multiply_strategy)
    result = calculator.execute_strategy(5, 3)
    print("Multiplication result:", result)

    calculator.set_strategy(division_strategy)
    result = calculator.execute_strategy(5, 3)
    print("Division result:", result)

if __name__ == "__main__":
    main()
