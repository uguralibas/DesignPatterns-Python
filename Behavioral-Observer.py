"""
Observer tasarım deseni, bir nesnenin durumu değiştiğinde 
diğer nesneleri otomatik olarak güncellemek için kullanılır. 
Bu desen, nesneler arasındaki bağımlılığı azaltır ve 
sistemdeki değişiklikleri izlemeyi ve yönetmeyi kolaylaştırır.
"""

from abc import ABC, abstractmethod

# Subject: Gözlemci Altjesi (Soyut)
class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

# Observer: Gözlemci (Soyut)
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

# ConcreteSubject: Somut Gözlemci Altjesi
class ConcreteSubject(Subject):
    def __init__(self, state=None):
        super().__init__()
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self.notify()

# ConcreteObserver: Somut Gözlemciler
class ConcreteObserverA(Observer):
    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        print("Observer A: State changed to", self._subject.state)

class ConcreteObserverB(Observer):
    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        print("Observer B: State changed to", self._subject.state)

# Kullanım
def main():
    # Konu oluştur
    subject = ConcreteSubject()

    # Gözlemciler oluştur
    observer1 = ConcreteObserverA(subject)
    observer2 = ConcreteObserverB(subject)

    # Konunun durumunu güncelle
    subject.state = "New State"

if __name__ == "__main__":
    main()
