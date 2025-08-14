# Store seat numbers (1 to 50) in a set
seat_numbers = set(range(1, 51))

# Ask user to book a seat from 1 - 50
book_seat = int(input("Book a seat from 1 to 50: "))

# Remove booked seats from the set
seat_numbers.remove(book_seat)

# Show remaining seats after booking
print(seat_numbers)
