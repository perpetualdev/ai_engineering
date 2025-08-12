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
# vowels = ['a', 'e', 'i', 'o', 'u'], then count each one
vowels_a = sentence.count("a")
vowels_e = sentence.count("e")
vowels_i = sentence.count("i")
vowels_o = sentence.count("o")
vowels_u = sentence.count("u")
# calculate the total number of vowels in the sentence
num_of_vowels = vowels_a + vowels_e + vowels_i + vowels_o + vowels_u
# Display the number
print(num_of_vowels)

# 10. Convert a string "1234" to an integer and multiply it by 2.
str_int = "1234"
convert_str_int = int(str_int) * 2
print(convert_str_int)
