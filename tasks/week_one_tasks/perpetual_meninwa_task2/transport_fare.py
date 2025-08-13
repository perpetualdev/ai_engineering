# Ask user for distance in km(float) and fare per km(float)
distance = int(input("Distance: "))
fare_per_km = float(input("Fare Per Km: "))

# Calculate and display the total fare with decimal places using 2f
total_fare = distance * fare_per_km

print(f"{total_fare:.2f}km")
