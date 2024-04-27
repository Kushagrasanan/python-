# Define a sample string
sample_string = "Hello, World!"

# Length of the string
print("Length of the string:", len(sample_string))

# Convert the string to lowercase
print("Lowercase:", sample_string.lower())

# Convert the string to uppercase
print("Uppercase:", sample_string.upper())

# Capitalize the string (first character uppercase, rest lowercase)
print("Capitalized:", sample_string.capitalize())

# Count occurrences of a substring
substring_count = sample_string.count("l")
print("Number of 'l' occurrences:", substring_count)

# Find the index of a substring
substring_index = sample_string.find("World")
print("Index of 'World':", substring_index)

# Replace a substring with another substring
replaced_string = sample_string.replace("World", "Universe")
print("After replacement:", replaced_string)

# Check if the string starts with a specified substring
starts_with_hello = sample_string.startswith("Hello")
print("Starts with 'Hello':", starts_with_hello)

# Check if the string ends with a specified substring
ends_with_world = sample_string.endswith("World!")
print("Ends with 'World!':", ends_with_world)

# Split the string into a list of substrings
split_string = sample_string.split(",")
print("Split string:", split_string)

# Join a list of substrings into a single string
joined_string = "-".join(["Hello", "World"])
print("Joined string:", joined_string)
