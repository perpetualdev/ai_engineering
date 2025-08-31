import math
# Basic Calculator Project

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract second number from first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide first number by second
def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("Cannot divide by zero")

# Function to get the square root of a given number
def square_root(a):
    if a != 0 or a > 0:
        return math.sqrt(a)
    else:
        raise ValueError("Cannot find the square root of 0 or negative number")

# Function to get the exponential of first and second number
def exp(a, b):
    return a ** b

# Function to get the modulus of first and second number
def mod(a, b):
    return a % b

# Display operation options to the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root")
print("6. Exponential")
print("7. Modulus")
print("8. Exit")

def main():
    try:
      while True:
        choice = int(input("Enter choice (1/2/3/4/5/6/7/8): "))
        # Exit program, if choice 8 is selected
        if choice == 8:
          print("Exiting calculator program...")
          break
        # Taking input of a given number if choice 5
        elif choice == 5:
          num = int(input("Please enter the number: "))
          print(f"The square root of {num} is:" , square_root(num))
        else:
          # Taking input from user for operation choice
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))
          # Perform calculation based on user's choice
          if choice == 1:
            print(f"The sum of {num1} and {num2} is: ", add(num1, num2))
          elif choice == 2:
            print(f"{num1} subtracted from {num2} is: ", subtract(num1, num2))
          elif choice == 3:
            print(f"The multiplication of {num1} and {num2} is: ", multiply(num1, num2))
          elif choice == 4:
            print(f"{num1} divided by {num2} is: ", divide(num1, num2))
          elif choice == 6:
            print(f"{num1} exponential {num2} is: ", exp(num1, num2))
          elif choice == 7:
            print(f"The remainder of {num1} divided by {num2} is: ", mod(num1, num2))
          else:
            print("Invalid choice")
    except Exception as e:
      print("Error: ", e)
    except ValueError as e:
      print("Error: ", e)
    finally:
      print("Thank you for using our calculator program!")

main()
