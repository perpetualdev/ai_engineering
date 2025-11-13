# ========= LIST CONTINUA ==============
# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5]
result = list1 + list2
print(result)  # [1, 2, 3, 4, 5]

# Repetition
nums = [1, 2]
repeated = nums * 3
print(repeated)  # [1, 2, 1, 2, 1, 2]

# Indexing
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-1])

# Slicing
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])   # [1, 2, 3]
print(numbers[:3])    # [0, 1, 2]
print(numbers[3:])    # [3, 4, 5]
print(numbers[::2])   # [0, 2, 4]

# Membership
colors = ["red", "green", "blue"]
print("green" in colors)  # True
print("yellow" not in colors) # True

# Length (len())
items = ["pen", "book", "laptop"]
print(len(items)) # 3

# Min and Mas (min()/max())
nums = [5, 2, 9, 1]
print(min(nums))  # 1
print(max(nums))  # 9

# Sum (sum()) - adds all the numerical elements in a list
numbers = [1, 2, 3, 4]
print(sum(numbers))  # 10

# Copying a List
a = [1, 2, 3]
b = a.copy()
# OR
c = list(a)
print(b)  # [1, 2, 3]
print(c)  # [1, 2, 3]
