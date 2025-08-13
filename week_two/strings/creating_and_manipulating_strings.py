# upper()
name = "Ada Balogun"
print(name.upper())
# ADA BALOGUN

# lower()
print(name.lower())
# ada balogun

# title()
sentence = "python is amazing"
print(sentence.title())
# Python Is Amazing

# strip()
# Removes whitespace (or specified characters) from both ends of the string
text = "   Abujarrrrrrr  "
print(text.strip())
print(text.strip(" r"))
# Output: Abuja

# replace()
message = "I love Java"
print(message.replace("Java", "Python"))
# Output: I love Python

# swapcase()
text = "Hello ABEOKUTA"
print(text.swapcase())
# hELLO abeokuta

# lstrip()
text = "   Nigeria"
print(text.lstrip())
# Output: Nigeria

# rstrip()
text = "Nigeria   "
print(text.rstrip())

# split()
fruits = "mango orange banana"
print(fruits.split())
# ['mango', 'orange', 'banana']

# rsplit()
text = "one,two,three,four,five"
print(text.rsplit(",", 3))

# splitlines()
lines = "Line 1\nLine 2\nLine3"
print(lines.splitlines())
# Output: ['Line 1', 'Line 2', Line 3']

# join()
words = ["I", "Love", "Python"]
print(" ".join(words))
# I Love Python

# center()
text = "Python"
print(text.center(20, "-"))
# -------Python-------

# ljust()
text = "Python"
print(text.ljust(10, "*"))
# Python****

# rjust()
text = "Python"
print(text.rjust(10, "*"))
# ****Python

# zfill()
num = "42"
print(num.zfill(5))
# 00042

# isalpha()
print("Lagos".isalpha())  # True
print("Lagos123".isalpha()) # False

# isdigit()
print("12345".isdigit())   # True
print("123a".isdigit())    # False

# isalnum()
print("Python3".isalnum())  #True
print("Python 3".isalnum()) #False

# Reverse a string
print("Python"[::-1])
