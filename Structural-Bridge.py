"""
Bridge tasarım deseni, soyutlanmış bir arayüz ve uygulama arasındaki ilişkiyi koparır. 
Bu şekilde her ikisinin de bağımsız olarak değiştirilmesine olanak tanır. 
Bu desen, çok sayıda değişiklik yapıldığında kodun daha esnek ve 
bakımı daha kolay olmasını sağlar.
"""

from abc import ABC, abstractmethod

# Abstraction: Uzaktan Kumanda
class RemoteControl(ABC):
    def __init__(self, device):
        self.device = device

    @abstractmethod
    def toggle_power(self):
        pass

# Refined Abstraction: TV Uzaktan Kumandası
class TVRemoteControl(RemoteControl):
    def toggle_power(self):
        if self.device.is_power_on():
            self.device.turn_off()
            print("TV kapandı")
        else:
            self.device.turn_on()
            print("TV açıldı")

# Refined Abstraction: Ses Sistemi Uzaktan Kumandası
class AudioSystemRemoteControl(RemoteControl):
    def toggle_power(self):
        if self.device.is_power_on():
            self.device.turn_off()
            print("Ses sistemi kapandı")
        else:
            self.device.turn_on()
            print("Ses sistemi açıldı")

# Implementor: Device Interface
class Device(ABC):
    def __init__(self):
        self.power_on = False

    def is_power_on(self):
        return self.power_on

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Concrete Implementor: TV
class TV(Device):
    def turn_on(self):
        self.power_on = True

    def turn_off(self):
        self.power_on = False

# Concrete Implementor: Ses Sistemi
class AudioSystem(Device):
    def turn_on(self):
        self.power_on = True

    def turn_off(self):
        self.power_on = False

# Kullanım
def main():
    # TV ve Ses Sistemi oluştur
    tv = TV()
    audio_system = AudioSystem()

    # TV uzaktan kumandası ile TV'yi kontrol et
    tv_remote = TVRemoteControl(tv)
    tv_remote.toggle_power()

    # Ses sistemi uzaktan kumandası ile ses sistemini kontrol et
    audio_remote = AudioSystemRemoteControl(audio_system)
    audio_remote.toggle_power()

if __name__ == "__main__":
    main()
