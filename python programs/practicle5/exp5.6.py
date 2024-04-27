import statistics

# Given list of numbers
numbers = [10, 20, 30, 40, 50]

# Calculating mean
mean = statistics.mean(numbers)
print("Mean:", mean)

# Calculating variance
variance = statistics.variance(numbers)
print("Variance:", variance)

# Calculating standard deviation
std_deviation = statistics.stdev(numbers)
print("Standard Deviation:", std_deviation)
