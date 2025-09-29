# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!")


# Child class (inherits from Animal)
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")


# Using them
dinosaur1 = Animal("Dino")
dog1 = Dog("Ryan")
cat1 = Cat("Alice")

dog1.speak()   # Ryan says woof!
cat1.speak()   # Alice says meow!
dinosaur1.speak()  # Dino makes a sound.