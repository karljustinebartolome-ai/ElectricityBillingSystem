# Main program

from ElectricityCustomer import ElectricityCustomer


# Function for checking valid input
def is_valid(kwh):

    # Consumption cannot be negative
    if kwh < 0:
        return False

    return True


print("ELECTRICITY BILLING SYSTEM")
print("--------------------------")

# Get customer name
name = input("Enter customer name: ")

# Check if name is empty
if name == "":
    print("Invalid input: Customer name cannot be empty.")

else:

    try:
        # Get electricity consumption
        kwh = float(input("Enter electricity consumption (kWh): "))

        # Check if input is valid
        if is_valid(kwh):

            # Create customer object
            customer = ElectricityCustomer(name, kwh)

            # Calculate bill
            bill = customer.calculate_bill()

            # Calculate 12% VAT
            vat = bill * 0.12

            # Calculate total
            total = bill + vat

            # Display result
            print("\n----- ELECTRICITY BILL -----")
            print("Customer Name:", customer.name)
            print("Consumption:", customer.kwh, "kWh")
            print("Bill before VAT: ₱{:.2f}".format(bill))
            print("VAT (12%): ₱{:.2f}".format(vat))
            print("Total Bill: ₱{:.2f}".format(total))

        else:
            print("Invalid input: kWh cannot be negative.")

    except ValueError:
        print("Invalid input: Please enter a number.")