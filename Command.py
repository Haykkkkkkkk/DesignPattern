from abc import ABC, abstractmethod

# Receiver
class Light:
    def on(self):
        print("The light is on")

    def off(self):
        print("The light is off")

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Command to turn on the light
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

# Concrete Command to turn off the light
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

# Client code
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()
remote.set_command(light_on)
remote.press_button()  # Output: The light is on

remote.set_command(light_off)
remote.press_button()  # Output: The light is off
