"""
State tasarım deseni, bir nesnenin davranışını 
durumuna göre değiştirmek için kullanılır. Bu desen, 
bir nesnenin farklı durumlar arasında geçiş yapmasını 
sağlar ve durumlar arasındaki geçiş mantığını nesneden soyutlar. 
Bu, bir nesnenin durumunu dinamik olarak değiştirmek ve 
duruma bağlı davranışları yönetmek için kullanışlı bir yöntemdir.
"""

from abc import ABC, abstractmethod

# Context: Bağlam
class Context:
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state = self._state.handle()

# State: Durum (Soyut)
class State(ABC):
    @abstractmethod
    def handle(self):
        pass

# ConcreteState: Somut Durumlar
class ConcreteStateA(State):
    def handle(self):
        print("Handling request in State A")
        # Durum değişikliği
        return ConcreteStateB()

class ConcreteStateB(State):
    def handle(self):
        print("Handling request in State B")
        # Durum değişikliği
        return ConcreteStateA()

# Kullanım
def main():
    # Başlangıç durumu: StateA
    context = Context(ConcreteStateA())

    # İstekleri işle
    context.request()  # StateA'da işlem yapacak
    context.request()  # StateB'de işlem yapacak
    context.request()  # StateA'da işlem yapacak

if __name__ == "__main__":
    main()

