from unicodedata import name

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says Woof!"

Dog1 = Dog("Buddy", 5)
print(Dog1.bark())
