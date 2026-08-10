seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]

# Display all seats with their status
for i in range(len(seats)):
    print("Seat", i + 1, ":", seats[i])

# Ask user to enter a seat number
seat_number = int(input("Enter seat number: "))

# Check seat availability
if seats[seat_number - 1] == "Available":
    seats[seat_number - 1] = "Booked"
    print("Seat booked successfully.")
else:
    print("Seat is already booked.")

# Count booked and available seats
booked_seats = seats.count("Booked")
available_seats = seats.count("Available")

# Display final details
print("Total Seats:", len(seats))
print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)