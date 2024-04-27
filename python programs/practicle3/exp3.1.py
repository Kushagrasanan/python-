def check_divisibility(num, divisor):
    """
    Function to check if a number is divisible by another
    :param num: The number to be checked
    :param divisor: The number to divide by
    :return: True if divisible, False otherwise
    """
    if num % divisor == 0:
        return True
    else:
        return False

# Taking input from the user
num = int(input("Enter the number to be checked: "))
divisor = int(input("Enter the divisor: "))

# Checking divisibility
if check_divisibility(num, divisor):
    print(f"{num} is divisible by {divisor}")
else:
    print(f"{num} is not divisible by {divisor}")
