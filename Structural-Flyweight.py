"""
Flyweight tasarım deseni, çok sayıda benzer nesnenin 
bellek kullanımını azaltmak için kullanılır. 
Bu desen, bir nesnenin paylaşılabilir durumdaki (intrinsic) kısmını 
ayırarak aynı veriyi paylaşan nesneler arasında bellek kullanımını minimize eder.
"""

class CoffeeFlavour:
    def __init__(self, flavour_name):
        self._flavour_name = flavour_name

    def __str__(self):
        return f"Coffee flavour: {self._flavour_name}"

class Menu:
    def __init__(self):
        self._flavours = {}

    def get_flavour(self, flavour_name):
        flavour = self._flavours.get(flavour_name)
        if not flavour:
            flavour = CoffeeFlavour(flavour_name)
            self._flavours[flavour_name] = flavour
        return flavour

    def get_total_flavours(self):
        return len(self._flavours)

class Order:
    def __init__(self, table_number, flavour_name, menu):
        self._table_number = table_number
        self._flavour = menu.get_flavour(flavour_name)

    def serve(self):
        print(f"Serving {self._flavour} to table {self._table_number}")

# Kullanım
def main():
    menu = Menu()

    order1 = Order(1, "Cappuccino", menu)
    order2 = Order(2, "Espresso", menu)
    order3 = Order(3, "Cappuccino", menu)

    order1.serve()
    order2.serve()
    order3.serve()

    print(f"Total coffee flavours in menu: {menu.get_total_flavours()}")

if __name__ == "__main__":
    main()
