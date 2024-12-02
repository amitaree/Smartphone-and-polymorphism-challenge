class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphism in action
for animal in [Dog(), Cat()]:
    print(animal.speak())

class SecretStash:
    def __init__(self):
        self.__chocolates = 10  # Private attribute

    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("One chocolate taken!")
        else:
            print("No chocolates left 😢")

stash = SecretStash()
stash.take_chocolate()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

class Car:
    def __init__(self, make, model, year):
        self.make = make        # Public attribute
        self._model = model     # Protected attribute
        self.__year = year      # Private attribute

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if year > 1885:  # The first car was invented in 1886
            self.__year = year
        else:
            print("Invalid year")

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

print(my_car.make)       # Output: Toyota
print(my_car._model)     # Output: Corolla
print(my_car.get_year()) # Output: 2020

# Trying to access the private attribute directly will raise an AttributeError
# print(my_car.__year)  # Uncommenting this line will raise an error
