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


# A House has multiple Rooms (like Bedroom, Kitchen, Bathroom), which form the house's structu

class Room:
    def __init__(self, name, area):
        self.name = name
        self.area = area


class House:
    def __init__(self, address):
        self.address = address
        self.rooms = []

    def add_room(self, room):
        return self.rooms.append(room)


house = House("123 Maple Street")
bedroom = Room("Bedroom", 200)
kitchen = Room("Kitchen", 150)
house.add_room(bedroom)
house.add_room(kitchen)
print([(room.name, room.area) for room in house.rooms])


# A Car class can contain instances of other classes like Engine, Transmission, and Wheel.
# Each component contributes to the functionality of the car.


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower  # This defines the 'horsepower' attribute


class Transmission:
    def __init__(self, type):
        self.type = type


class Car:
    def __init__(self, name, engine, transmission):
        self.name = name
        self.engine = engine
        self.transmission = transmission


engine = Engine(2000)
transmission = Transmission('Automatic')
car = Car("Toyota corolla hybrid", engine, transmission)

print(car.name)  # Toyota corolla hybrid
print(car.transmission.type)  # Automatic
print(car.engine.horsepower)  # Output: 2000
