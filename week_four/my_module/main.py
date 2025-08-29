import first
import second

print("")
print("=== Math Functions ===")
print("5 + 3 =", first.add(5, 3))
print("10 - 4 =", first.subtract(10, 4))
print("6 * 7 =", first.multiply(6, 7))
print("20 / 5 =", first.divide(20, 5))

print("\n=== String Functions ===")
print(second.greet("Ridwan"))
print("Reverse of 'Python' =", second.reverse_string('Python'))
print("Character count in sentence =", second.count_chars("Python modules are powerful"))
print("Word count in sentence =", second.count_words("Python modules are powerful"))
