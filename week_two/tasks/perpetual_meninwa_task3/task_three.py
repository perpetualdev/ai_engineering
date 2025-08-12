# ============= TASK THREE ================
# Given "apple,banana,orange", split the string into a list of fruits.
print("apple,banana,orange".split(","))  # ['apple', 'banana', 'orange']

# 12. Ask the user for a sentence and print each word on a new line.
sentence = input("Write a sentence on how your day has been: ")
# First split the sentence using the separator
new_line = sentence.split(" ")
# Then join using the new line escape sequence
print("\n".join(new_line))

# 13. Replace all spaces in a string with underscores (_).
space_string = "   Cameleon   "
print(space_string.replace(" ", "_"))  # ___Cameleon___

# 14. Count how many times the letter "a" appears in "Banana".
print("Banana".count("a"))  # 3

# 15. Check if a given string starts with "https://".
site = "https://www.w3schools.com/"
print(site.startswith("https://")) # True
