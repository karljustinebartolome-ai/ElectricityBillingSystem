# Child class

from Customer import Customer


class ElectricityCustomer(Customer):

    # Polymorphism
    def calculate_bill(self):

        # First 100 kWh
        if self.kwh <= 100:
            bill = self.kwh * 10

        # Next 100 kWh
        elif self.kwh <= 200:
            bill = (100 * 10) + ((self.kwh - 100) * 12)

        # Above 200 kWh
        else:
            bill = (100 * 10) + (100 * 12) + ((self.kwh - 200) * 15)

        return bill