"""
Key Characteristics of Composition:
Has-a Relationship: Composition represents a “has-a” relationship between objects. For example, a Car has-a Engine.
Ownership: The composed objects usually do not exist independently of the class that owns them.
If the owner object is destroyed, the composed objects are also destroyed.
Flexible and Reusable: It allows for greater flexibility in designing complex systems compared to inheritance,
as you can mix and match components.
"""


# A Car has an Engine, but it can also have other components like Transmission, Wheels, and Seats.
class Engine:
    def __init__(self, hasPower):
        self.hasPower = hasPower

    def start(self):
        return "Engine started"


class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def start_car(self):
        return self.engine.start()


# Composition in action:
engine = Engine("2000Hors")
car = Car("Toyota high brid ", engine)
print(car.start_car())
