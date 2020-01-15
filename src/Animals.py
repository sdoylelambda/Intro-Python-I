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
        # print("Animal")
        pass

class Dog(Animal):
    def __init__(self, name, legs=4):
        super().__init__(name, legs)
    def speak(self):
        return "Woof!"
    def species(self):
        return "Dog"

class Bird(Animal):
    def __init__(self, name, legs=2):
        super().__init__(name, legs)
    def speak(self):
        return "Brrrrraawwpp"
    def species(self):
        return "Bird"

class Cat(Animal):
    def __init__(self, name, legs=4):
        self.name = name
        self.legs = legs
    def speak(self):
        return "Meowz"
    def species(self):
        return "Cattious minimus"


d = Dog("Fido")
b = Bird("CawCaw")
c = Cat("kitty")

animals = [d,b,c]
print("a", d.legs)
print(d.speak())
print(d.type)
print(animals)


for animal in animals:
    print(f"{animal.name} says {animal.speak()}")





# HOUSE EX
class Building:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
    def __repr__(self):
        # this return name of room
        return self.name

class Room:
    def __init__(self, room_type):
        self.room_type = room_type
    def __repr__(self):
        return self.room_type

bedroom = Room("Bedroom")
bathroom = Room("bathroom")
home = Building("House" [bedroom, bathroom])

print(home.Room)


def print_string():
    print('STR')

def return_string():
    return "STR"