import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Car(Prototype):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

if __name__ == "__main__":
    original_car = Car("Kia", "Forte")
    print("Orig car:", original_car)

    cloned_car = original_car.clone()
    print("Clone car:", cloned_car)
