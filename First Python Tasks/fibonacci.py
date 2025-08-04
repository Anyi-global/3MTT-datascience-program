'''
Task: Generate the Fibonacci Sequence.

Objective: To create a Python program that generates the first n terms of the Fibonacci sequence based on user input.

Acceptance Criteria:

The program accepts a positive integer input (n) from the user.
It generates and displays the first n terms of the Fibonacci sequence.
The Fibonacci sequence is calculated iteratively.
If the input is zero or negative, an appropriate error message is displayed.
Non-integer input is handled gracefully with an error message.
'''

# Handles errors gracefully
try:
    print("Operation Begins...\n")
    n = int(input("Enter Integer number: "))

    def fibonacci_sequence(n):
        if n <= 0:
            print("Enter a positive integer!")
            return
        
        # Handling case where n is equal to 1
        if n == 1:
            print("Fibonacci Sequence: [0] \n")
            return
        
        # Initializing fibonacci sequence
        first_term = 0
        second_term = 1
        fib_sequence = [first_term, second_term]

        # Generating fibonacci numbers iteratively
        for i in range(2, n):
            next_term = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_term)

        # Printing the first n terms in the fibonaaci sequence
        print("Fibonacci Sequence: ", fib_sequence[:n], "\n")
    
    # Calling the fibonacci function
    fibonacci_sequence(n)
    
except ValueError as e:
    print("Invalid input value: ", e)

else:
    print("Successful...")

finally:
    print("Ended Here!")