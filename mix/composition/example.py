class Animal:
    def __init__(self):
        pass

    def eat(self):
        print("yum")


class Dog(Animal):
    def bark(self):
        print("off")


class Cat(Animal):
    def Mew(self):
        print("Meew")


class Robot:
    def move(self):
        print("robot move")


class Cook_robot(Robot):
    def cook(self):
        print("this robot is for cooking")


class Clean_robot(Robot):
    def clean(self):
        print("This robot is for clening")


class Super_bot:
    def __init__(self):
        self.obj1 = Robot()
        self.obj2 = Dog()
        self.obj3 = Clean_robot()

    def play_game(self):
        print("I love to play chase")

    def move(self):
        return self.obj1.move()

    def bark(self):
        return self.obj2.bark()

    def clean(self):
        return self.obj3.clean()
