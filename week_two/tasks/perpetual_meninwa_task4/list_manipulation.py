# Create a list of five cties
cities = ["Lagos", "Abuja", "Ibadan", "New York", "Texas"]

# Replace the third city with a new one
cities.pop(2)
cities.insert(2, "Kano")
# print(cities)

# Remove the last city
cities.pop()
# print(cities)

# Add a new city to the beginning of the list
cities.insert(0, "Maryland")
print(cities)