"""
Facade tasarım deseni, bir alt sistemin karmaşıklığını gizlemek ve 
daha basit bir arabirim sağlamak için kullanılır. 
Bu desen, istemcilerin karmaşık alt sistemlerle doğrudan etkileşim kurmak yerine, 
bu alt sistemlerle iletişim kurmalarını sağlayan bir arayüz sağlar.
"""

# Alt sistemler
class TheaterLights:
    def on(self):
        print("Theater lights are on")

    def off(self):
        print("Theater lights are off")

class AudioSystem:
    def turn_on(self):
        print("Audio system is on")

    def turn_off(self):
        print("Audio system is off")

class Projector:
    def turn_on(self):
        print("Projector is on")

    def turn_off(self):
        print("Projector is off")

# Facade
class HomeTheaterFacade:
    def __init__(self):
        self.lights = TheaterLights()
        self.audio = AudioSystem()
        self.projector = Projector()

    def watch_movie(self):
        self.lights.on()
        self.audio.turn_on()
        self.projector.turn_on()
        print("Get ready to watch a movie!")

    def end_movie(self):
        print("Movie is finished")
        self.lights.off()
        self.audio.turn_off()
        self.projector.turn_off()

# Kullanım
def main():
    # Facade oluştur
    home_theater = HomeTheaterFacade()

    # Film izle
    home_theater.watch_movie()

    # Film izlemeyi bitir
    home_theater.end_movie()

if __name__ == "__main__":
    main()
