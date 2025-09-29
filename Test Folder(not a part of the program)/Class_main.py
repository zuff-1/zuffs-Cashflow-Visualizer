
class class_dog1:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")


class class_dog2(class_dog1):  # inherits everything from class_dog1
    pass


my_dog = class_dog2("Ryan")
my_dog.bark()