""" is the concept of hiding the complex implementation details of a system and
 exposing only the necessary parts that are relevant to the user.
 This allows us to interact with objects at a high level without worrying about how they are implemented.


Driving a Car

When you drive a car, you use a steering wheel, accelerator, and brakes.
You don’t need to know how the engine works, how the fuel is injected, 
or how the transmission shifts gears. All the complex details are abstracted away,
and you only interact with the car's interface (steering wheel, pedals, etc.).



File System (Working with File I/O)
When you open, read, or write to a file in a programming language, you don’t
need to know how the underlying file system works, how bits are written 
to the disk, or how file systems are structured. The file handling functions 
provide an abstraction over the complex file system operations.

with open("filename.txt", "r") as f:
    f.write("Hello World")
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radios):
        self.radios = radios

    def area(self):
        return 3.14 * self.radios * self.radios


class Rectangle(Shape):
    def __init__(self, hight, width):
        self.hight = hight
        self.width = width

    def area(self):
        return self.width * self.hight


shapes = [Circle(14), Rectangle(3, 4)]

print([shape.area() for shape in shapes])


# Payment Gateway

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class PayPal(Payment):
    def process_payment(self, amount):
        return f"Paypal processing amount of ${amount}"


class Strip(Payment):
    def process_payment(self, amount):
        return f"Strip processing amount of ${amount}"


payment_method = [Strip(), PayPal()]

print([payment.process_payment(200) for payment in payment_method])


# User Authentication

class AuthSystem:
    def login(self, username, password):
        if self._validate:
            return "User Authenticated successfully"
        else:
            return "Invalid credentials"

    def _validate(self, username, password):
        return username == "admin", password == "123"


auth = AuthSystem()
print(auth.login("admin", "123"))


# Vehicle Abstraction

class Vehicle:
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "The car has been started"


class Motorcycle(Vehicle):
    def start_engine(self):
        return "The motorcycle engin started"


vehicles = [Car(), Motorcycle()]
print([vehicle.start_engine() for vehicle in vehicles])


# File System Operations

class FileSystem:
    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.readlines()


# fileSystem = FileSystem()
# fileSystem.read_file("abc.txt")


#  Notification System
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class Email(Notification):
    def send(self, message):
        return "Email has been sent: {message}".format(message=message)


class SMS(Notification):
    def send(self, message):
        return f"SMS has been sent: {message}"


notifications = [Email(), SMS()]

print("\n".join(notification.send("Hi there")
      for notification in notifications))

for notification in notifications:
    print(notification.send("Hi there"))
