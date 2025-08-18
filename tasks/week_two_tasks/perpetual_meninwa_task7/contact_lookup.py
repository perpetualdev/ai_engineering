# store three names and their phone numbers in a dictionary
names = ('Joseph', 'Benedict', 'Kemi')
phone_numbers = ('07012345678', '08098765432', '09011223344')
contact_info = dict(zip(names, phone_numbers))
print("Contact Information:", contact_info)

# Ask the user for a name and display the corresponding phone number
lookup_contact = input("Enter a name to look up their phone number: ")

# Display the corresponding phone number or an error message if the name is not found
print(contact_info.get(lookup_contact, f"No contact found for {lookup_contact}."))
