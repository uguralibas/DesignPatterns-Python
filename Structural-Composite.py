"""
Composite tasarım deseni, hiyerarşik bir nesne yapısını temsil eder ve 
bu nesnelerin tek bir nesne gibi davranmasını sağlar. 
Bu desen, parça-bütün ilişkisini temsil etmek için kullanılır ve 
ağaç yapısındaki nesnelerin işlenmesini kolaylaştırır.
"""

from abc import ABC, abstractmethod

# Component: Abstract
class FileSystemComponent(ABC):
    @abstractmethod
    def list_contents(self):
        pass

# Leaf: Concrete Component
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def list_contents(self):
        print(f"File: {self.name}")

# Composite: Concrete Component
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def list_contents(self):
        print(f"Folder: {self.name}")
        for child in self.children:
            child.list_contents()

# Kullanım
def main():
    # Ana klasör oluştur
    root = Folder("Root")

    # Alt klasörler ve dosyalar ekle
    folder1 = Folder("Folder 1")
    folder2 = Folder("Folder 2")
    folder1_1 = Folder("Folder 1-1")
    folder1_2 = Folder("Folder 1-2")
    file1 = File("File 1")
    file2 = File("File 2")
    file3 = File("File 3")

    # Alt klasörleri ana klasöre ekle
    folder1.add(folder1_1)
    folder1.add(folder1_2)
    root.add(folder1)
    root.add(folder2)

    # Dosyaları alt klasöre ekle
    folder1.add(file1)
    folder2.add(file2)
    folder1_1.add(file3)

    # Klasör ve dosyaları listele
    root.list_contents()

if __name__ == "__main__":
    main()
