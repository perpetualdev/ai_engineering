# ====================== TASK 1 =========================
# Take input from user and display it in uppercase
nickname = input("What is your nickname? ")
print(nickname.upper())

# 2. Given the string "python", print its first and last characters.
print("Python"[0])
print("Python"[-1])

# 3. Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.
name = input("What is your name? ")
print(f"Hello {name}")

# 4. Write a program to count the number of characters in a string without using len().
word = "Hello World"
print(word.find(word[-1]) + 1)
# print(len("Hello World"))

# 5. Given "Hello World", replace "World" with "Python".
print("Hello World".replace("World", "Python"))

# ==================== TASK 2 ========================
# Check if a given string contains the substring "python" (case-insensitive).
print("Python" in "Hello Python")

# 7. Write a program to reverse a string without using slicing ([::-1]).
reverse_word = "Hello People"
print("".join(reversed(reverse_word)))

# 8. Given a string with extra spaces, remove the leading and trailing spaces.
print("     Hello Python    ".strip())

# 9. Ask the user to enter a sentence and print the number of vowels in it.
sentence = input("Enter a sentence: ")

# let us display the vowels in a list
vowels = ['a', 'e', 'i', 'o', 'u']
new_vowels = []

# 10. Convert a string "1234" to an integer and multiply it by 2.
str_int = "1234"
convert_str_int = int(str_int) * 2
print(convert_str_int)
