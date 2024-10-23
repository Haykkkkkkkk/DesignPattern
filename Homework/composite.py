class Component:
    def operation(self):
        pass


class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        return f"Leaf: {self.name}"


class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component: Component):
        self.children.append(component)

    def operation(self):
        results = [child.operation() for child in self.children]
        return "Composite: [" + ", ".join(results) + "]"


if __name__ == "__main__":
    leaf1 = Leaf("Leaf 1")
    leaf2 = Leaf("Leaf 2")
    composite = Composite()
    composite.add(leaf1)
    composite.add(leaf2)

    print(composite.operation())
