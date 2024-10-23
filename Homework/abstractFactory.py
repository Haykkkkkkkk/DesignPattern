from abc import ABC, abstractmethod



class Button(ABC):
    @abstractmethod
    def paint(self):
        pass



class WindowsButton(Button):
    def paint(self):
        print("Button in Windows style")



class MacButton(Button):
    def paint(self):
        print("Button in Mac style")



class ButtonFactory:
    @staticmethod
    def create_button(os_type: str) -> Button:
        if os_type == "windows":
            return WindowsButton()
        elif os_type == "mac":
            return MacButton()
        else:
            raise ValueError("Unknown OS")


if __name__ == "__main__":
    os_type = input("Enter OS (windows/mac): ").lower()
    button = ButtonFactory.create_button(os_type)
    button.paint()
