# Ask the user to input a word
word = input("Please input a word: ")

# Print the length of the word
print(len(word))

# check if it is all uppercase, all lowercase or title case
print(word.isupper())
print(word.islower())
print(word.istitle())

# Reverse the word using slicing
print(word[::-1])
