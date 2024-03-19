"""
Command tasarım deseni, bir isteği nesne olarak temsil eder ve 
bu isteği bir aksiyona dönüştüren bir arayüz sağlar. Bu desen, 
komutların soyutlanmasını sağlar, böylece çağırıcı ve 
alıcı arasındaki bağımlılığı azaltır ve işlemleri parametrelerle ve 
önceden belirlenmiş komutlarla temsil eder.
"""

from abc import ABC, abstractmethod

# Command: Komut (Soyut)
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Receiver: Alıcı
class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

# ConcreteCommand: Somut Komutlar
class TurnOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()

class TurnOffCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()

# Invoker: Çağırıcı
class RemoteControl:
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def press_button(self, command_name):
        if command_name in self._commands:
            self._commands[command_name].execute()
        else:
            print("Command not found")

# Kullanım
def main():
    # Alıcı oluştur
    light = Light()

    # Komutları oluştur
    turn_on_command = TurnOnCommand(light)
    turn_off_command = TurnOffCommand(light)

    # Çağırıcı oluştur
    remote_control = RemoteControl()

    # Komutları kaydet
    remote_control.register("turn_on", turn_on_command)
    remote_control.register("turn_off", turn_off_command)

    # Butonları bas
    remote_control.press_button("turn_on")
    remote_control.press_button("turn_off")

if __name__ == "__main__":
    main()
