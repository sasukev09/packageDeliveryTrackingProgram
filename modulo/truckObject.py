"""
truckObject.py
~
Western Governors University
C950: Data Structures & Algorithms II
~
Kevin Salazar
Student ID: 010303855
~
January 7, 2024
"""
class Truck:
    # This is the constructor to initialize the Truck object with provided attributes.
    # Time Complexity: O(1) - the operations are fixed and do not depend on input size.
    def __init__(self, capacity, speed, load, packages, mileage, address, depart_time):
        self.capacity = capacity  # The Maximum package capacity of the truck
        self.speed = speed  # The Speed of the truck in units per hour
        self.load = load  # The Current load of the truck
        self.packages = packages  # The List of packages loaded onto the truck
        self.mileage = mileage  # The Total mileage covered by the truck
        self.address = address  # The Current address of the truck
        self.depart_time = depart_time  # The Departure time of the truck
        self.time = depart_time  # The Current departing/time of the truck

    # String representation for the truck object
    # Formatted using string literals ' f" ', for easy debugging and printing.
    # Time Complexity: O(1) - as the operations are fixed and do not depend on input size.
    def __str__(self):
        return (
            f"Truck Details:\n"
            f" - Capacity: {self.capacity}\n"
            f" - Speed: {self.speed}\n"
            f" - Load: {self.load}\n"
            f" - Packages: {self.packages}\n"
            f" - Mileage: {self.mileage}\n"
            f" - Address: {self.address}\n"
            f" - Departure Time: {self.depart_time}"
        )