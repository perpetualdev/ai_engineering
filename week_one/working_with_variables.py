# # Create variables using string, integer and float
# # String
# full_name = "Perpetual Ogochukwu Meninwa"

# # Integer
# age_minus_five = 24

# # Float
# value_of_pi = 3.14

# print(full_name)
# print(age_minus_five)
# print(value_of_pi)

# # ===== TYPECASTING =======
# # int()
# # float()
# # str()
# # bool()

# # Convert input to integer
# age = int(input("Enter your age: "))
# print(f"You will be {age + 1} years old next year.")

# # Calculator using input
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# sum_result = num1 + num2
# print(f"The sum of {num1} and {num2} is {sum_result}.")


# ======= TASK: Use the USSD code kind of method to collect data from the user ======
print("Welcome to Sterling Bank.\n")

# Get the last four digit of your user
pin = input("Please input the last four digit pin: ")

# Display it in the console
print(f"Your pin is {pin}\n")

# Get the request from the user
print("What would you like to do please?")
request = input("Withdraw or Deposit: ")

# Get the amount from the user and display it
amount = int(input(f"How much would you like to {request}? "))
print("==================== Request processing ============================\n")
print(f"Congratulations, your request of N{amount} has been processed successfully...🎉🎉🎉")
