num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Check if num1 is equal to num2
print(f"{num1} == {num2} : {num1 == num2}")

# Check if num2 is not equal to num2
print(f"{num1} != {num2} : {num1 != num2}")

# Check if num1 is greater than num2
print(f"{num1} > {num2} : {num1 > num2}")

# Check if num1 is less than num2
print(f"{num1} < {num2} : {num1 < num2}")

### Give 3 usecases or cenarios where you can apply the program below.
# SC. 1 - Check for eligibility to drink alcohol
# SC. 2 - Check for eligibility to join the army
# SC. 3 - Check if you pass the IELTS exam

### Write the code for 1 of the 3 use cases
# Check for eligibility to join the army

# Defining variables
eligibleHeight = 175
userHeight = float(input("Enter your height: "))

if eligibleHeight == userHeight:
  print("You are eligible to join the army.")
elif eligibleHeight < userHeight:
  print("You are eligible to join the army.")
else:
  print("You are not eligible to join the army")

# ======================= OR =====================
# A shorter version below

# if eligibleHeight <= userHeight:
#   print("You are eligible to join the army.")
# else:
#   print("You are not eligible to join the army")
