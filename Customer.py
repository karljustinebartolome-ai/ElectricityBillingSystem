# Parent class

class Customer:

    def __init__(self, name, kwh):
        # Encapsulation
        self.name = name
        self.kwh = kwh

    # Abstraction
    def calculate_bill(self):
        return 0