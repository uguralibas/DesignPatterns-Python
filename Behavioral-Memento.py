"""
Memento tasarım deseni, bir nesnenin durumunu kaydetmek ve 
geri yüklemek için bir mekanizma sağlar. Bu desen, 
bir nesnenin iç durumunu saklamak ve sonradan geri yüklemek için kullanılır. 
Özellikle geri alma işlevselliği sağlamak için kullanılır.
"""

import copy

# Originator: Oluşturucu
class Editor:
    def __init__(self):
        self._content = ""

    def create_memento(self):
        return Memento(self._content)

    def restore(self, memento):
        self._content = memento.get_saved_content()

    def set_content(self, content):
        self._content = content

    def get_content(self):
        return self._content

# Memento: Hatırlayıcı
class Memento:
    def __init__(self, content):
        self._content = content

    def get_saved_content(self):
        return self._content

# Caretaker: Bakıcı
class History:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

# Kullanım
def main():
    editor = Editor()
    history = History()

    # Editör durumu kaydet
    editor.set_content("State 1")
    history.add_memento(editor.create_memento())
    print("State: ", editor.get_content())

    # Editör durumunu değiştir
    editor.set_content("State 2")
    history.add_memento(editor.create_memento())
    print("State: ", editor.get_content())

    # Editör durumunu geri yükle
    editor.restore(history.get_memento(0))
    print("Restored State:", editor.get_content())

if __name__ == "__main__":
    main()
