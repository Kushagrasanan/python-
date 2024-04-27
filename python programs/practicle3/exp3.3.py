def is_leap_year(year):
    """
    Function to check if a given year is a leap year or not
    :param year: The year to be checked
    :return: True if the year is a leap year, False otherwise
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Taking input from the user
year = int(input("Enter a year: "))

# Checking if the year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
