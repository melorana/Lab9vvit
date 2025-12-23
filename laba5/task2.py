class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
my_circle = Circle(5)
my_circle.set_radius(10)
print(my_circle.get_radius())