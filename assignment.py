# Base class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")
    
    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")

# Derived class
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, price, os, camera_megapixels):
        super().__init__(brand, model, price)
        self.os = os
        self.camera_megapixels = camera_megapixels
    
    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels} MP camera!")
    
    def info(self):
        super().info()
        print(f"OS: {self.os}, Camera: {self.camera_megapixels} MP")

# Using the classes
basic_phone = Smartphone("Nokia", "1100", 20)
basic_phone.call("1234567890")
basic_phone.info()

print()

smartphone = AdvancedSmartphone("Apple", "iPhone 15", 999, "iOS", 48)
smartphone.call("9876543210")
smartphone.take_photo()
smartphone.info()
