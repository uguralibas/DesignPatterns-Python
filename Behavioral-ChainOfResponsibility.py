"""
Chain of Responsibility tasarım deseni, taleplerin işlenme sırasını 
dinamik olarak belirlemek ve her bir işleyiciyi gerektiğinde 
değiştirmek için kullanılır. Bu desen, 
istemcinin hangi işleyicinin talebi işleyeceğini bilmemesini ve 
isteği işleyecek işleyicinin otomatik olarak seçilmesini sağlar.
"""

from abc import ABC, abstractmethod

# Handler: Soyut
class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass

# ConcreteHandler: Somut
class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request <= 10:
            print("ConcreteHandler1 is handling the request")
        elif self._successor:
            self._successor.handle_request(request)

# ConcreteHandler: Somut
class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if 10 < request <= 20:
            print("ConcreteHandler2 is handling the request")
        elif self._successor:
            self._successor.handle_request(request)

# ConcreteHandler: Somut
class ConcreteHandler3(Handler):
    def handle_request(self, request):
        if request > 20:
            print("ConcreteHandler3 is handling the request")
        elif self._successor:
            self._successor.handle_request(request)

# Kullanım
def main():
    # Zincirin oluşturulması
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()

    handler1._successor = handler2
    handler2._successor = handler3

    # Taleplerin işlenmesi
    requests = [5, 15, 25]
    for request in requests:
        handler1.handle_request(request)

if __name__ == "__main__":
    main()
