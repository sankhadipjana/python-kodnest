class Vehicle:
    # Class attributes
    dealership_name = "Unknown"
    total_vehicles = 0

    def __init__(self, make, model, price):
        # Instance attributes
        self.make = make
        self.model = model
        self.price = price

    @staticmethod
    def dealership_policy():
        print("Dealership Policy: All vehicles come with a 2-year warranty.")

    @classmethod
    def increment_vehicle_count(cls):
        cls.total_vehicles += 1


# Prompt the user for inputs
Vehicle.dealership_name = input().strip()
make = input().strip()
model = input().strip()
price = int(input().strip())

# Increment the vehicle count using the class method
Vehicle.increment_vehicle_count()

# Create the Vehicle object
my_vehicle = Vehicle(make, model, price)

# Display the required output
print(f"Updated Vehicle Count: {Vehicle.total_vehicles}")
print(f"Dealership: {Vehicle.dealership_name}")
print(f"Total Vehicles: {Vehicle.total_vehicles}")
print(f"Vehicle Make: {my_vehicle.make}, Model: {my_vehicle.model}, Price: {my_vehicle.price}")

# Call the static method
Vehicle.dealership_policy()