class Venicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return f"марка: {self.make}, модель: {self.model}"
class Car(Venicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, тип топлива: {self.fuel_type}"
bike = Venicle("Harley-Davidson", "Sportster")
print(bike.get_info())
my_car = Car("Ford", "Mustang", "Дизель")
print(my_car.get_info())
