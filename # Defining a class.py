# Defining a class
class Car:
    color = "red"  # Attribute

    # Method
    def drive(self):
        print("The car is driving 🚗")

# Creating an object
my_car = Car()
print(my_car.color)
my_car.drive()

class Car:
    def __init__(self, color, model):
        self.color = color    # Instance variable
        self.model = model    # Instance variable

# Creating objects with unique attributes
car1 = Car("blue", "Sedan")
car2 = Car("red", "SUV")

print(car1.color)  # Output: blue
print(car2.model)  # Output: SUV

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    pass

car = Car(4)
print(car.wheels)  # Output: 4

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
