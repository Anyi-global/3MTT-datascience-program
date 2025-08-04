'''
Task: Swapping two numbers in Python.

Objective: Create a Python program that swaps two numbers entered by the user and displays the values before and after swapping.

Acceptance Criteria:

The program accepts two numbers as input from the user.
The numbers are displayed before and after swapping.
The program uses Python’s tuple unpacking for swapping.
Invalid input (non-numeric) is handled gracefully with an error message.
The program successfully swaps the values without requiring a temporary variable.
'''

# Handling error gracefully
try:
    # Accept two number inputs from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("\nNumbers before swapping: \n", "first number: ", num1, "\n", "second number: ", num2, "\n")
    
    print("Swapping is about to happen...")
    numbers = (num2, num1) # store the numbers in a tuple
    second_num, first_num = numbers # swapping the numbers using tuple unpacking
    
    print("\nNumbers after swapping: \n", "first number: ", second_num, "\n", "second number: ", first_num)

except ValueError as e:
    print("Input Error: ", e)

except Exception as e:
    print("Somethig went wrong!", e)

else:
    print("\nSwapping Successful...")

finally:
    print("Swapping Ended")
