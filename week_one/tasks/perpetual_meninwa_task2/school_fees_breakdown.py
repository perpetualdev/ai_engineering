# Ask user for school name, tuition fee (float), hostel fee(float) and feeding fee(float)
school_name = input("What is the  name of your school? ")
tuition_fee = float(input("Tuition Fee: "))
hostel_fee = float(input("Hostel Fee: "))
feeding_fee = float(input("Feeding Fee: "))

total_fees = float(tuition_fee + hostel_fee + feeding_fee)

# Calculate the total and print it in receipt format with each fee on a new line
print(f"School Name: {school_name}\nTuition Fee: {tuition_fee}\nHostel Fee: {hostel_fee}\nFeeding Fee: {feeding_fee}\nTOTAL FEES: {total_fees:.2f}")