# Single quote
name = 'Ada'

# Double quote
greeting = "Hello"

# Triple quotes
story = '''Once upon a time,
there was a coder named Ada.'''

password = "p@ssw0rd123"

# Print to the console
print(f"{name} {greeting} {story} {password}")

# ============ INDEXING ==============
word = "Python"
print(word[0])  # P
print(word[-1])  # n

# ============ SLICING ===============
word = "Python"
print(word[0:4])  # Pyth - starts from the index before the colon and ends just before the index after the colon
print(word[2:])   # thon - if there is no index after the colon, it starts from the index before the colon to the end
print(word[:3])   # Pyt - if there is no index before the colon, it starts from the beginning to the character before the index after the colon.
print(word[::2])  # Pto - if there are two colon before the index, it starts from the beginning and picks every 2 index (0, 1, 2 in this case) till the end
print(word[::-1]) # nohtyP - if there are two colons and then -1, it spells the word backwards

# ============ STR CONCATENATION & REPITITION ================
# Concatenation
a = "Hello"
b = "World"
print(a + " " + b)  # Hello World

# Repitition
word = "Hi! "
print(word * 3)

# ========== STR SEARCHING & CHECKING =================
# Membership
text = "Python programming"
print("Python" in text)   # True
print("Java" not in text) # True

# Find (find() / rfind())
text = "Hello World"
print(text.find("o"))  # 4 - find the first index of the character
print(text.rfind("o")) # 7 - reverse find the first index starting from index 0

# Index (index() / rindex()) - raises an error if not found
text = "Hello World"
print(text.index("World")) #6
# ValueError: substring not found

# startswith() / endswith()
filename = "data.csv"
print(filename.startswith("data")) # True
print(filename.endswith(".csv"))   # True

