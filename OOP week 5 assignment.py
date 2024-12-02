class Smartphone:
    def __init__(self, brand, model, os, camera_mp):
        self.brand = brand
        self.model = model
        self.os = os
        self.camera_mp = camera_mp
    
    def make_call(self, number):
        print(f"Calling {number}...")
    
    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")
    
    def take_photo(self):
        print(f"Taking photo with {self.camera_mp}MP camera...")

class FlagshipSmartphone(Smartphone):
    def __init__(self, brand, model, os, camera_mp, fast_charging):
        super().__init__(brand, model, os, camera_mp)
        self.fast_charging = fast_charging
    
    def enable_fast_charging(self):
        print("Fast charging enabled...")

class BudgetSmartphone(Smartphone):
    def __init__(self, brand, model, os, camera_mp, expandable_storage):
        super().__init__(brand, model, os, camera_mp)
        self.expandable_storage = expandable_storage
    
    def insert_memory_card(self):
        print("Memory card inserted...")

# Create instances
iphone15 = FlagshipSmartphone("Apple", "iPhone 14", "iOS", 12, True)
galaxyS24 = FlagshipSmartphone("Samsung", "Galaxy S23", "Android", 108, False)
redmiNote12 = BudgetSmartphone("Xiaomi", "Redmi Note 11", "Android", 50, True)

# Make calls, send messages, take photos
iphone15.make_call("555-1234")
galaxyS24.send_message("555-5678", "Hello from S23!")
redmiNote12.take_photo()

# Enable fast charging or insert memory card
iphone15.enable_fast_charging()
redmiNote12.insert_memory_card()

#polymorphismchallenge.py
class Animal:
  def move(self):
    print("Walking") 

class Vehicle:
  def move(self):
    print("Driving") 

class Plane:
  def move(self):
    print("Flying") 

# Create instances of each class
dog = Animal()
car = Vehicle()
plane = Plane()

# Call the move() method on each instance
dog.move()  # Output: Walking 🚶
car.move()  # Output: Driving 🚗
plane.move()  # Output: Flying ✈️