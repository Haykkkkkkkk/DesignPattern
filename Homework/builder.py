class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make: str):
        self.car.make = make
        return self

    def set_model(self, model: str):
        self.car.model = model
        return self

    def set_year(self, year: int):
        self.car.year = year
        return self

    def build(self) -> Car:
        return self.car


if __name__ == "__main__":
    builder = CarBuilder()
    car = (builder
           .set_make("Kia")
           .set_model("Forte")
           .set_year(2019)
           .build())
    print(car)
