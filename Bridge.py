from abc import ABC, abstractmethod

# Abstraction
class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

# Concrete implementation 1
class SVGRenderer:
    def render_circle(self, radius):
        return f"<circle r='{radius}' />"

# Concrete implementation 2
class CanvasRenderer:
    def render_circle(self, radius):
        return f"Canvas circle with radius {radius}"

# Refined abstraction
class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        return self.renderer.render_circle(self.radius)

# Client code
svg_renderer = SVGRenderer()
canvas_renderer = CanvasRenderer()

circle1 = Circle(svg_renderer, 5)
circle2 = Circle(canvas_renderer, 10)

print(circle1.draw()) 
print(circle2.draw()) 
