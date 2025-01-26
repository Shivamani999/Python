# polymorphism means having many forms
# python cant overload, but can override the functions

class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("These move....")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("these float....")

class Plane(Vehicle):
    def move(self):
        print("these fly....")

car = Car("Ford", "Figo")
boat = Boat("Titanic", "A5")
plane = Plane("AirIndia", "747")

for x in (car,boat,plane):
    print(x.brand)
    print(x.model)
    x.move()