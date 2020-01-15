from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def species(self):
        pass


class Dog(Animal):
    def __init__(self, name, legs=4):
        super().__init__(name, legs)
    def speak(self):
        return "Woof!"
    def species(self):
        print("Dog")


class Bird(Animal):
    def __init__(self, name, legs=4):
        super().__init__(name, legs)
    def speak(self):
        return "Tweet tweet!"
    def species(self):
        print("Bird")



class Cat(Animal):
    def __init__(self, name, legs=4):
        super().__init__(name, legs)
    def speak(self):
        return "Meow"
    def species(self):
        print("Cat")


b = Bird("Larry")
c = Cat("Garfield")
d = Dog("Fido")

animals = [b, c, d]


for animal in animals:
    print(f"{animal.name} says {animal.speak()}")



class Building:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
    def __str__(self):
        return self.name


class Room:
    def __init__(self, room_type):
        self.type = room_type
    def __str__(self):
        return self.type
    def __repr__(self):
        return self.type



bedroom= Room("Bedroom")
bathroom= Room("Bathroom")

house = Building("My house", [bedroom, bathroom])



def print_string():
    print("STR")
    # return None


def return_string():
    return "STR"

