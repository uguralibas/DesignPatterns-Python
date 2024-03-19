"""
Prototype tasarım deseni, bir nesnenin kopyasını oluşturarak 
yeni nesnelerin oluşturulmasını kolaylaştırır. Bu desen, 
bir nesnenin oluşturulması için maliyetli işlemleri azaltır ve 
karmaşık nesnelerin daha verimli bir şekilde oluşturulmasını sağlar.
"""

from copy import deepcopy

# Prototype: Abstract interface
class BookPrototype:
    def clone(self):
        pass

# Concrete Prototype: Book
class Book(BookPrototype):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def clone(self):
        return deepcopy(self)

# Client
def main():
    # Orijinal kitap nesnesi
    original_book = Book("Python Cookbook", "David Beazley", 50)

    # Kopya kitap nesneleri oluşturma
    book1 = original_book.clone()
    book1.title = "Learning Python"
    book1.price = 40

    book2 = original_book.clone()
    book2.title = "Fluent Python"
    book2.price = 55

    # Kopya kitapları listeleme
    print("Book 1:", book1.title, "-", book1.author, "-", book1.price)
    print("Book 2:", book2.title, "-", book2.author, "-", book2.price)

if __name__ == "__main__":
    main()