# =================== COMPARISON OPERATORS ======================
a = 10
b = 20

print(a == b)   # False

print(a != b)   # True

print(a > b)   # False

print(a < b)   # True

print (a >= 10) # True

print (b <= 25) # True

# ===== Student Exam Result Example =====
score = 75

print(score >= 50)  # True (Passed)
print(score < 50)   # False (Failed)
print(score == 100) # False (Not full marks)

x = 10
x += 5  # Adds 5 to x
# print(x)

x -= 3  # Subtracts 3 from x
# print(x)

x *= 2  # Multiplies x by 2
# print(x)

x /= 4  # Divides x by 4
# print(x)

x %= 3  # Stores remainder after division
# print(x)

x = 10
x **= 2 # Raises x to the power of 2
print (x)

x //= 2 # Floor divides x by 2
print (x)

# ===== Bank transaction example =====
balance = 1000
deposit = 200
withdraw = 150

balance += deposit    # Add deposit
balance -= withdraw   # Subtract withdrawal

print("Updated Balance:", balance)
# Output: Updated Balance: 1050


# =============== LOGICAL OPERATORS ====================
x = 10
y = 20

# and operator
print(x > 5 and y > 15)   # True

# or operator
print(x < 5 or y > 15)    # True

# not operator
print(not(x == 10))   # False

# Scholarship Eligibility Example

# Define variables
age = 17
score = 85

# Must be younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)

print("Scholarship Eligible:", eligible)
# Output: Scholarship Eligible: True


# Event Access Example
age = 22
has_ticket = False

can_enter = (age >= 18) and (has_ticket or age < 25)

print("Access Granted:", can_enter)
# Output: Access Granted: True (because age < 25 even without ticket)

