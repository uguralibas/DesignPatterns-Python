"""
Iterator tasarım deseni, bir koleksiyon üzerinde gezinmek için 
bir arayüz sağlar ve koleksiyonun nasıl gezileceğini koleksiyonun kendisinden soyutlar. 
Bu desen, bir koleksiyonun iç yapısını değiştirmeden koleksiyon üzerinde 
farklı iterasyon stratejileri uygulamak için kullanılır.
"""

from abc import ABC, abstractmethod

# Aggregate: Soyut
class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

# ConcreteAggregate: Somut
class ConcreteAggregate(Aggregate):
    def __init__(self):
        self._data = []

    def add_item(self, item):
        self._data.append(item)

    def create_iterator(self):
        return ConcreteIterator(self._data)

# Iterator: Soyut
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# ConcreteIterator: Somut
class ConcreteIterator(Iterator):
    def __init__(self, data):
        self._data = data
        self._index = 0

    def has_next(self):
        return self._index < len(self._data)

    def next(self):
        if self.has_next():
            item = self._data[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

# Kullanım
def main():
    # Aggregate oluştur
    aggregate = ConcreteAggregate()

    # Verileri ekle
    aggregate.add_item("Item 1")
    aggregate.add_item("Item 2")
    aggregate.add_item("Item 3")

    # Iterator oluştur
    iterator = aggregate.create_iterator()

    # İterasyon yap
    while iterator.has_next():
        print(iterator.next())

if __name__ == "__main__":
    main()
