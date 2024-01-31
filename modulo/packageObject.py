"""
packageObject.py
~
Western Governors University
C950: Data Structures & Algorithms II
~
Kevin Salazar
Student ID: 010303855
~
January 7, 2024
"""
import datetime


class Package:
    # Creating a special case ID variable, for package with ID of 9.
    SPECIAL_CASE_ID = 9

    # Constructor which initializes the Package object with its attributes
    # Time Complexity: O(1) - Because the number of operations is fixed, making it constant.
    def __init__(self, ID, address, city, state, zipcode, deadlineTime, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadlineTime = deadlineTime
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    # String representation of  package object, for easy printing and debug
    # Time Complexity: O(1) - Number of operations id fixed, being constant.
    def __str__(self):
        return f"ID: {self.ID} | {self.address} {self.city} {self.state}, {self.zipcode} | Deadline: {self.deadlineTime} | Weight: {self.weight} | Delivery time: {self.delivery_time} | Status: {self.status}"

    # Method that updates the status of the package based on time.
    # Time Complexity: O(1) - Constant time, number of operations is fixed.
    def update_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            self.status = "Package has been delivered."
        elif self.departure_time > convert_timedelta:
            self.status = "Package in transit, expected delivery time is displayed."
        else:
            self.status = "Package at hub, expected delivery time is displayed."

        # Helper method to handle a special case.
        self._update_special_case(convert_timedelta)

    # Helper method to handle a special case of package with ID 9.
    # Time Complexity: O(1) - Constant time as number of operations is fixed.
    def _update_special_case(self, convert_timedelta):
        if self.ID == self.SPECIAL_CASE_ID:
            # Making the update that occurs at 10:20AM, correcting the delivery address for package with ID 9.
            if convert_timedelta > datetime.timedelta(hours=10, minutes=20, seconds=0):
                self.address, self.zipcode = "410 S State St", "84111"
            else:
                self.address, self.zipcode = "300 State St", "84103"
