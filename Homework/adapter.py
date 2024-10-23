class OldSystem:
    def specific_request(self):
        return "Old system data"


class NewSystem:
    def request(self):
        return "New system data"


class Adapter:
    def __init__(self, new_system: NewSystem):
        self.new_system = new_system

    def specific_request(self):
        return self.new_system.request()


if __name__ == "__main__":
    old_system = OldSystem()
    print(old_system.specific_request())

    new_system = NewSystem()
    adapter = Adapter(new_system)
    print(adapter.specific_request())
