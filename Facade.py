
class DVDPlayer:
    def on(self):
        print("DVD Player is on")

    def play(self):
        print("DVD Player is playing")

class Projector:
    def on(self):
        print("Projector is on")

    def wide_screen_mode(self):
        print("Projector in wide-screen mode")

class SurroundSoundSystem:
    def on(self):
        print("Surround Sound System is on")

    def set_volume(self, level):
        print(f"Surround Sound System volume set to {level}")

# Facade
class HomeTheaterFacade:
    def __init__(self, dvd, projector, sound_system):
        self.dvd = dvd
        self.projector = projector
        self.sound_system = sound_system

    def watch_movie(self):
        print("Get ready to watch a movie...")
        self.dvd.on()
        self.dvd.play()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.sound_system.on()
        self.sound_system.set_volume(5)

# Client code
dvd = DVDPlayer()
projector = Projector()
sound_system = SurroundSoundSystem()

home_theater = HomeTheaterFacade(dvd, projector, sound_system)
home_theater.watch_movie()
