# ====================== TASK 1 =========================
# Take input from user and display it in uppercase
nickname = input("What is your nickname? ")
print(nickname.upper())

# 2. Given the string "python", print its first and last characters.
print("Python"[0]) # P
print("Python"[-1]) # n

# 3. Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.
name = input("What is your name? ")
print(f"Hello {name}")

# 4. Write a program to count the number of characters in a string without using len().
word = "Hello World"
# using the find(), get the last index and since it is zero indexed add 1
print(word.find(word[-1]) + 1)

# 5. Given "Hello World", replace "World" with "Python".
print("Hello World".replace("World", "Python"))

