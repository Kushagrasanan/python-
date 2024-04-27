def calculate_salary(bs):
    """
    Function to calculate DA and HRA based on basic salary
    :param bs: Basic salary of the employee
    :return: Total salary (basic salary + DA + HRA)
    """
    if bs >= 20000:
        da = 0.3 * bs
        hra = 0.2 * bs
    else:
        da = 0.2 * bs
        hra = 0.1 * bs
    
    total_salary = bs + da + hra
    return total_salary

# Taking input from the user for the basic salary
basic_salary = float(input("Enter the basic salary of the employee: "))

# Calculating total salary
total_salary = calculate_salary(basic_salary)

# Displaying the result
print("Total salary:", total_salary)
