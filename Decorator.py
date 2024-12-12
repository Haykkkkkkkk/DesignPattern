class Coffee:
    def cost(self):
        return 5  

class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 1 

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 0.5 

# Usage
basic_coffee = Coffee()
print("Basic Coffee Cost: ", basic_coffee.cost())  

milk_coffee = MilkDecorator(basic_coffee)
print("Cost with Milk: ", milk_coffee.cost())  

milk_sugar_coffee = SugarDecorator(milk_coffee)
print("Cost with Milk and Sugar: ", milk_sugar_coffee.cost()) 
