# Ask the user to input the names of the members ans store in a list
members = input("Enter the names of the members, separated by commas: ").split(',')

# Use set to remove duplicates
members_set = set(members)

# Use dictionary comprehension to create a dictionary with member names as keys and their lengths as values
members_dict = {member: len(member) for member in members_set}

print("Unique members and their name lengths:", members_dict)
