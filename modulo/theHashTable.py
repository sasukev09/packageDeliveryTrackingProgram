"""
theHashTable.py
~
Western Governors University
C950: Data Structures & Algorithms II
~
Kevin Salazar
Student ID: 010303855
~
January 7, 2024
"""
class HashMapCreation:
    # Constructor that initializes the hash map with initial capacity.
    # Time Complexity: O(N), N is the initial capacity; it depends on the size of the hash map.
    def __init__(self, initial_capacity=20):
        # Initializing the hash map as a list of empty lists
        self.list = [[] for _ in range(initial_capacity)]

    # Method that inserts a key-value pair into the hash map.
    # Time Complexity: O(1) average; O(N) in the worst case when many collisions are present.
    def insert(self, key, item):
        # Determines the bucket index using the hash of the key
        bucket = hash(key) % len(self.list)
        # Accesses the bucket list at the calculated index
        bucket_list = self.list[bucket]

        for kv in bucket_list:
            # Checks if the key already exists in the bucket
            if kv[0] == key:
                # If found, updates the value associated with the key
                kv[1] = item
                return True

        # If the key is non-existent in the bucket, a new key-value pair is added
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Method that looks up the value associated with a given key in the hash map.
    # Time Complexity: O(1) average; O(N) in the worst case (many collisions).
    def lookup(self, key):
        # Determining the bucket index using the hash of the key
        bucket = hash(key) % len(self.list)
        # Accessing the bucket list at the calculated index
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            # Checking if the key matches the key in the current key-value pair
            if key == pair[0]:
                # If key is found, returns associated value.
                return pair[1]
        # Return None if the key is not found in the hash map
        return None

    # Method to remove a key-value pair from the hash map.
    # Time Complexity: O(N),( N is the length of the bucket list), dependent on the size of the list.
    def hash_remove(self, key):
        # Determining the bucket index using the hash of the key
        slot = hash(key) % len(self.list)
        # Accessing the bucket list at the calculated index
        destination = self.list[slot]

        if key in destination:
            destination.remove(key)