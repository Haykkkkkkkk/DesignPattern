from abc import ABC, abstractmethod

# State interface
class TVState(ABC):
    @abstractmethod
    def press_power_button(self, tv):
        pass

# Concrete states
class OnState(TVState):
    def press_power_button(self, tv):
        print("Turning TV off...")
        tv.set_state(OffState())

class OffState(TVState):
    def press_power_button(self, tv):
        print("Turning TV on...")
        tv.set_state(OnState())

class StandbyState(TVState):
    def press_power_button(self, tv):
        print("Waking TV from standby...")
        tv.set_state(OnState())

# Context
class TV:
    def __init__(self):
        self._state = OffState()  # TV starts off

    def set_state(self, state):
        self._state = state

    def press_power_button(self):
        self._state.press_power_button(self)

# Client code
tv = TV()

# Turn TV on
tv.press_power_button()

# Turn TV off
tv.press_power_button()  

# Turn TV on again
tv.press_power_button() 

# Change to standby state
tv.set_state(StandbyState())
tv.press_power_button()  
