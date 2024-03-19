"""
Adapter tasarım deseni, bir arayüzün beklenen bir şekilde davranmadığı durumlarda, 
mevcut bir sınıfın arayüzünü değiştirmek veya 
uyumlu hale getirmek için kullanılır. Bu desen, 
iki uyumsuz arayüzü bir araya getirerek birlikte çalışmalarını sağlar.
"""

# Adaptee: USB 2.0 Cihazı
class USB2Device:
    def connect_via_usb2(self):
        return "USB 2.0 bağlantısı kuruldu"

# Target: USB 3.0 Arayüzü
class USB3Interface:
    def connect_via_usb3(self):
        return "USB 3.0 bağlantısı kuruldu"

# Adapter: USB 2.0 Cihazını USB 3.0 Arayüzüne Dönüştürür
class USB3Adapter(USB3Interface):
    def __init__(self, usb2_device):
        self.usb2_device = usb2_device

    def connect_via_usb3(self):
        return f"{self.usb2_device.connect_via_usb2()} USB 3.0 arayüzüne dönüştürüldü"

# Kullanım
def main():
    # USB 2.0 cihazı oluştur
    usb2_device = USB2Device()

    # USB 2.0 cihazını USB 3.0 arayüzüne dönüştüren adaptörü oluştur
    adapter = USB3Adapter(usb2_device)

    # USB 3.0 arayüzüne bağlan
    print(adapter.connect_via_usb3())

if __name__ == "__main__":
    main()