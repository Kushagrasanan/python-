# Define a sample string
sample_string = "Hello, World!"

# Slicing to get a substring
substring = sample_string[7:]
print("Substring starting from index 7:", substring)

# Slicing to get a substring with a specified range
substring_range = sample_string[0:5]
print("Substring from index 0 to 4:", substring_range)

# Slicing with negative indices
substring_negative = sample_string[-6:-1]
print("Substring using negative indices:", substring_negative)

# Slicing with a step
substring_step = sample_string[::2]
print("Every second character of the string:", substring_step)

# Reverse a string using slicing
reverse_string = sample_string[::-1]
print("Reversed string:", reverse_string)
