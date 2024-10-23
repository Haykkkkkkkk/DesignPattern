from abc import ABC, abstractmethod

# Abstract class for shapes


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass



class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")



class Square(Shape):
    def draw(self):
        print("Drawing a Square")



class ShapeFactory:
    shape_registry = {}

    @classmethod
    def register_shape(cls, shape_name, shape_class):
        cls.shape_registry[shape_name] = shape_class

    @classmethod
    def create_shape(cls, shape_name):
        shape_class = cls.shape_registry.get(shape_name)
        if shape_class:
            return shape_class()
        else:
            raise ValueError(f"Unknown shape type: {shape_name}")


ShapeFactory.register_shape("circle", Circle)
ShapeFactory.register_shape("square", Square)


def main():
    shape_type = input("Enter shape type (circle/square): ").lower()
    try:
        shape = ShapeFactory.create_shape(shape_type)
        shape.draw()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
