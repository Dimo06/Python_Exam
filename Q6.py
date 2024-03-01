# Original string
original_string = "Hello, world!"

# Attempt to modify the string
try:
    original_string[7] = 'W'
except TypeError as e:
    print(f"Error: {e}")
# Modifying the original string via original_string[7] = 'W' will fail, because of the string's immutability

# Correct way to "modify" a string
modified_string = original_string[:7] + 'W' + original_string[8:]
print(modified_string)

# To change the "w" to "W" in "world", we create a new string (modified_string) that contains the desired change
