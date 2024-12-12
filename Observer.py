from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

# Concrete observer: Phone display
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"Phone display: Temperature updated to {temperature}°C")

# Concrete observer: Window display
class WindowDisplay(Observer):
    def update(self, temperature):
        print(f"Window display: Temperature updated to {temperature}°C")

# Subject interface
class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Concrete subject: Weather station
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = None

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()


weather_station = WeatherStation()

phone_display = PhoneDisplay()
window_display = WindowDisplay()

weather_station.add_observer(phone_display)
weather_station.add_observer(window_display)

weather_station.set_temperature(25)
weather_station.set_temperature(30)
