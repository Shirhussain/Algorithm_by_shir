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


# A Library can contain multiple Book instances. Each Book object holds its own details, but together they
# form a collection within the Library.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)


book1 = Book("48 Law of power", "robert green")
book2 = Book("Zero to One", "Peter tell")

lib = Library()

lib.add_book(book1)
lib.add_book(book2)

print([f"{book.title}, {book.author}" for book in lib.books])


# A Computer class can be made up of various components such as CPU, RAM, and Storage.
# Each component is a separate object that is part of the computer.

class CPU:
    def __init__(self, brand):
        self.brand = brand


class RAM:
    def __init__(self, size):
        self.size = size


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity


class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage


cpu = CPU("Intel")
ram = RAM("16GB")
storage = Storage("2TB")

computer = Computer(cpu, ram, storage)
print(computer.cpu.brand, computer.ram.size, computer.storage.capacity)


# A House consists of multiple Room objects. Each room can have its own attributes such
# as type (e.g., kitchen, bedroom) and area.

class Room:
    def __init__(self, type, area):
        self.type = type
        self.area = area


class House:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)


kitchen = Room("Kitchen", "200 square meters")
bedroom = Room("Bedroom", "900 square meters")

house = House()
house.add_room(kitchen)
house.add_room(bedroom)


print([room.type for room in house.rooms])


# A Restaurant has various MenuItem objects.
# Each MenuItem represents a dish or drink offered by the restaurant.

class MenuItem(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant(object):
    def __init__(self):
        self.menus = []

    def add_menu(self, menu):
        self.menus.append(menu)


restaurant = Restaurant()
qabuli = MenuItem("Qabuli palaw", "$20")
chopan_kabab = MenuItem("Chopan kabab", "$24")

restaurant.add_menu(qabuli)
restaurant.add_menu(chopan_kabab)

print([(menu.name, menu.price) for menu in restaurant.menus])


# In a sports team, a Team class can contain multiple Player objects,
# each with their own attributes like name and position.

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)


team = Team("Barsolona")
messi = Player("Messi", "Forwards")
nemar = Player("Nemar", "Defense")
swaresz = Player("Swaresz", "middle")

team.add_player(messi)
team.add_player(nemar)
team.add_player(swaresz)

print(f"Team name is: {team.team_name}", [
      f"{player.name}, {player.position}" for player in team.players])


# A Person object can contain multiple Address objects,
# as a person might have a home address, a work address, etc.

class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city


class Person:
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def add_address(self, address):
        self.addresses.append(address)


person = Person("Ahmad")
address1 = Address("234 bul", "Kabul")
address2 = Address("234234th street", "San Francisco")

person.add_address(address1)
person.add_address(address2)

print(person.name, [(person.street, person.city)
      for person in person.addresses])
