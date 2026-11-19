# Define base class 1: ElectronicDevice
class ElectronicDevice:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_device_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


# Define base class 2: Warranty
class Warranty:
    def __init__(self, warranty_provider, warranty_expiry):
        self.warranty_provider = warranty_provider
        self.warranty_expiry = warranty_expiry

    def display_warranty_info(self):
        print(f"Warranty Provider: {self.warranty_provider}")
        print(f"Warranty Expiry: {self.warranty_expiry}")


# Define derived class: Laptop (inherits from both ElectronicDevice and Warranty)
class Laptop(ElectronicDevice, Warranty):
    def __init__(self, brand, model, serial_number, warranty_provider, warranty_expiry):
        ElectronicDevice.__init__(self, brand, model)
        Warranty.__init__(self, warranty_provider, warranty_expiry)
        self.serial_number = serial_number

    def display_laptop_info(self):
        self.display_device_info()
        print(f"Serial Number: {self.serial_number}")
        self.display_warranty_info()


# Prompt the user for input
brand = input().strip()
model = input().strip()
serial_number = input().strip()
warranty_provider = input().strip()
warranty_expiry = input().strip()

# Create an instance of the Laptop class
my_laptop = Laptop(brand, model, serial_number, warranty_provider, warranty_expiry)

# Display the laptop information
my_laptop.display_laptop_info()