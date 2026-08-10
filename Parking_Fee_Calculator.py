def calculate_parking_fee():
    try:
        hours = float(input("Enter parking hours: "))
        if hours < 0:
            print("Hours cannot be negative.")
            return

        # Determine rate per hour based on duration
        if hours <= 2:
            rate = 30
        elif hours <= 5:
            rate = 25
        else:
            rate = 20

        # Calculate initial parking charge
        parking_charge = hours * rate

        # Determine service charge
        if parking_charge > 150:
            service_charge = 20
        else:
            service_charge = 0

        final_amount = parking_charge + service_charge

        # Display results (formatted nicely for whole or decimal amounts)
        print(f"\nParking Charge: ₹{parking_charge:.2f}".rstrip('0').rstrip('.'))
        print(f"Service Charge: ₹{service_charge}")
        print(f"Final Amount: ₹{final_amount:.2f}".rstrip('0').rstrip('.'))

    except ValueError:
        print("Invalid input. Please enter a numerical value for hours.")

if __name__ == "__main__":
    calculate_parking_fee()