"""
Mediator tasarım deseni, bir grup nesnenin birbiriyle doğrudan 
iletişim kurmak yerine bir arabulucu aracılığıyla iletişim kurmasını sağlar. 
Bu, nesneler arasındaki bağımlılığı azaltır ve 
iletişimi merkezi hale getirerek sistemdeki karmaşıklığı azaltır.
"""

from abc import ABC, abstractmethod

# Mediator: Arabulucu (Soyut)
class Mediator(ABC):
    @abstractmethod
    def notify(self, colleague, event):
        pass

# ConcreteMediator: Somut Arabulucu
class ChatRoom(Mediator):
    def __init__(self):
        self._colleagues = []

    def add_colleague(self, colleague):
        self._colleagues.append(colleague)

    def notify(self, colleague, event):
        for c in self._colleagues:
            if c != colleague:
                c.receive(event)

# Colleague: Meslektaş (Soyut)
class Colleague(ABC):
    def __init__(self, mediator):
        self._mediator = mediator

    def send(self, event):
        self._mediator.notify(self, event)

    @abstractmethod
    def receive(self, event):
        pass

# ConcreteColleague: Somut Meslektaşlar
class User(Colleague):
    def __init__(self, name, mediator):
        super().__init__(mediator)
        self._name = name

    def receive(self, event):
        print(f"{self._name} received: {event}")

# Kullanım
def main():
    # Arabulucu oluştur
    chat_room = ChatRoom()

    # Meslektaşları oluştur
    user1 = User("User1", chat_room)
    user2 = User("User2", chat_room)

    # Meslektaşları arabulucuya ekle
    chat_room.add_colleague(user1)
    chat_room.add_colleague(user2)

    # Meslektaşlardan biri diğerine mesaj gönder
    user1.send("Hello from User1")

if __name__ == "__main__":
    main()
