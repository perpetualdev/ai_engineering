# Ask user for 5 Nigerian states separated by comma and put them in a tuple
states = input("Enter five Nigerian states separated by comma e.g. Kano,Jos,etc: ")

# convert to list using the split method and then to tuple using the tuple constructor
states_tuple = tuple(states.split(","))

# Print the first state and last state
print("First State: ", states_tuple[0])
print("Last State: ", states_tuple[-1])

# Check if "Lagos" is in the tuple and print "Yes" or "No"
if "Lagos" in states_tuple:
  print("Yes")
else:
  print("No")
