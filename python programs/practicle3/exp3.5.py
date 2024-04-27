def calculate_commission(sales_amount):
    """
    Function to calculate commission based on sales amount
    :param sales_amount: Sales amount of the salesman
    :return: Commission amount
    """
    if sales_amount >= 15000:
        commission = 0.2 * sales_amount
    elif sales_amount >= 1000:
        commission = 0.15 * sales_amount
    else:
        commission = 0.1 * sales_amount
    
    return commission

# Taking input from the user for the sales amount
sales_amount = float(input("Enter the sales amount: "))

# Calculating commission
commission = calculate_commission(sales_amount)

# Displaying the result
print("Commission:", commission)
