"""
Proxy tasarım deseni, gerçek nesneye erişimi kontrol etmek, 
yükleme işlemlerini geciktirmek, önbelleklemek veya 
yetkilendirme eklemek gibi senaryolarda yaygın olarak kullanılır. 
Bu desen, uygulamanın performansını artırmak ve 
kaynakları etkin bir şekilde kullanmak için kullanılır.
"""

from abc import ABC, abstractmethod

# Subject: Soyut
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# RealSubject: Gerçek
class RealImage(Image):
    def __init__(self, filename):
        self._filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image: {self._filename}")

    def display(self):
        print(f"Displaying image: {self._filename}")

# Proxy: Proxy
class ImageProxy(Image):
    def __init__(self, filename):
        self._filename = filename
        self._real_image = None

    def display(self):
        if not self._real_image:
            self._real_image = RealImage(self._filename)
        self._real_image.display()

# Kullanım
def main():
    # Gerçek nesne üzerinden erişim
    real_image = RealImage("example.jpg")
    real_image.display()

    # Proxy üzerinden erişim
    image_proxy = ImageProxy("test.jpg")
    image_proxy.display()

if __name__ == "__main__":
    main()
