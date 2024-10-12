# Task 1:/// Task 1: Identify the Greatest
#  Write a Python program that asks the user to enter three numbers. 
# Your code should then identify and print out the largest number among the three. ///

first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))
third_number = int(input("Enter third number:"))
if first_number > second_number or third_number:
    print(first_number)
elif second_number > first_number or third_number:
    print(second_number)
elif third_number > first_number or second_number:
    print(third_number)
else:
    print("Oh no,no,no")

# Task2: /// Identify the Smallest 
# Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))
third_number = int(input("Enter third number:"))
if first_number > second_number < third_number:
    print(first_number, second_number)
elif first_number > second_number > third_number:
    print(first_number, third_number)
elif first_number > second_number == third_number:
    print("smallest number is", second_number or third_number, "The largest number is", first_number)
elif second_number > first_number < third_number:
    print(second_number, first_number)
elif second_number > first_number > third_number:
    print(second_number, third_number)
elif second_number > first_number == third_number:
    print("The smallest number is", first_number or third_number, "The largest number is", second_number)
elif third_number > first_number < second_number:
    print(third_number, first_number)
elif third_number > first_number > second_number:
    print(third_number, second_number)
elif third_number > first_number == second_number:
    print("The smallest number is", first_number or second_number, "The largest number is", third_number)
else:
    print("Oh no,no,no")



