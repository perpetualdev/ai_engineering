# Basic usage of input()
name = input("Enter your name: ")
print("Hello,", name)

# Convert input to integer
age = int(input("Enter your age: "))
print(f"You will be {age + 1} years old next year.")

# Calculator using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num1} is {sum_result}.")

# TASK: Use a print statement to greet your customer and use input statement to take their order

# Step1 - Print Welcome to the console
print("Welcome to Perpy's Kitchen! 😍😊😊")

# Step 2 - Take the customer order
customer_order = input("What will you like to eat today?: ") 
customer_order2 = input("Anything else?: ") 

# Step 3 - Print the inputted data to the console
print(f"Your current order is {customer_order} and {customer_order2}")
print("Your order is comin right up... 👍")
print("Thank you for patronizing Perpy's Kitchen... Come back again")
