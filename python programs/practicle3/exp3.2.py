def check_number(num):
    """
    Function to check if a number is positive, negative, or zero
    :param num: The number to be checked
    :return: A string indicating whether the number is positive, negative, or zero
    """
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Taking input from the user
number = float(input("Enter a number: "))

# Checking the number
result = check_number(number)
print("The number is", result)
