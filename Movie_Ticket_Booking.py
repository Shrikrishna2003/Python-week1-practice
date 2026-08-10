# Get user inputs
name = input("Enter customer name: ")
age = int(input("Enter age: "))
tickets = int(input("Enter number of tickets: "))

# Determine ticket price based on age rules
if age < 12:
    price_per_ticket = 120
elif age <= 59:
    price_per_ticket = 200
else:
    price_per_ticket = 150

# Calculate total before discount
total_before_discount = price_per_ticket * tickets

# Apply 10% discount if buying 5 or more tickets
if tickets >= 5:
    discount = total_before_discount * 0.10
else:
    discount = 0.0

# Calculate final amount
final_amount = total_before_discount - discount

# Display summary
print("\n--- Movie Ticket Booking Summary ---")
print(f"Customer Name: {name}")
print(f"Ticket Price: ₹{price_per_ticket}")
print(f"Number of Tickets: {tickets}")
print(f"Total Before Discount: ₹{total_before_discount:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")