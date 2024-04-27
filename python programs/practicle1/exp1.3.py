def compound_interest(principal, rate, time):
    """
    Function to calculate compound interest
    :param principal: Principal amount
    :param rate: Interest rate (in percentage)
    :param time: Time period (in years)
    :return: Compound interest
    """
    # Convert rate from percentage to decimal
    rate = rate / 100

    # Calculate compound interest
    amount = principal * (1 + rate) ** time
    compound_interest = amount - principal

    return compound_interest

# Taking input from the user
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))
time_period = float(input("Enter the time period (in years): "))

# Calculating compound interest
interest = compound_interest(principal_amount, interest_rate, time_period)

# Displaying the result
print("Compound interest:", interest)
