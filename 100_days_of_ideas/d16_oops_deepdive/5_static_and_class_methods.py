"""
Static and class methods server distinct purposes.
"""

class Vehicle:
    vehicle_count = 0  # Clas attribute

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        Vehicle.vehicle_count += 1

    @staticmethod
    def convert_speed(mph):
        """Static method to convert speed from mph to km/h"""
        return mph * 1.60934
    
    @classmethod
    def from_type(cls, type):
        """Class method to create a vehicle with default speed"""
        return cls(type, 50)
    

# Usage
vehicle1 = Vehicle("Car", 80)
print(Vehicle.convert_speed(60))

vehicle2 = Vehicle.from_type("Bike")
print(vehicle2.type, vehicle2.speed)