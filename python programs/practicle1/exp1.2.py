def calculate_average(subject1, subject2, subject3):
    total_marks = subject1 + subject2 + subject3
    average_marks = total_marks / 3
    return average_marks

# Taking input from the user for marks in three subjects
subject1_marks = float(input("Enter marks obtained in subject 1: "))
subject2_marks = float(input("Enter marks obtained in subject 2: "))
subject3_marks = float(input("Enter marks obtained in subject 3: "))

# Calculating average marks
average_marks = calculate_average(subject1_marks, subject2_marks, subject3_marks)

# Displaying the result
print("Average marks of the three subjects:", average_marks)
