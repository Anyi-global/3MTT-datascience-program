'''
3. Prime/Armstrong/Palindrome Number Identifier
Task: Write a code/logic to determine if the value entered is a Prime number, an Armstrong Number or a Palindrome number.

Objective: To create a Python program that checks whether a user-entered number is a Prime number, Armstrong number, or Palindrome, and displays the results accordingly.

Acceptance Criteria:

The program accepts a single integer input from the user.
It checks and identifies if the number is a:
Prime number: A number greater than 1 that is divisible only by 1 and itself.
Armstrong number: A number equal to the sum of its digits raised to the power of the number of digits.
Palindrome: A number that reads the same backward as forward.
The program displays appropriate messages for each property satisfied by the number.
If the number does not meet any criteria, a message is displayed stating so.
Non-integer input is handled gracefully with an error message.
'''

print("What do you want to do? Prime, Armstrong, or Palindrone, choose one...\n")

user_input = input("Enter 1 for Prime, 2 for Armstrong, and 3 for Palindrome: ")

# Handles error gracefully
try:
    print("Operation Begins...\n")
    if user_input == '1':
        number = int(input("Enter a number: "))

        def is_prime(number):
            if number < 1:
                return "Enter a positive number!!"

            elif number == 1:
                return f'{number} is not a prime number'

            for i in range(2, int(number**0.5) + 1):
                if number%i == 0:
                    return f'{number} is not a prime number \n'
            
            return f'{number} is a prime number \n'
            
        result = is_prime(number)
        print(result)

    elif user_input == '2':
        num = int(input("Enter an integer number: "))

        def is_armstrong(num):
            count_digits = int(len(str(num)))

            temp = num
            sum = 0

            while temp != 0:
                rem = temp%10
                temp = temp//10
                sum += rem ** count_digits

            if sum == num:
                return f'{num} is Armstrong!'
            else:
                return f'{num} is not Armstrong!'
        
        result = is_armstrong(num)
        print(result)

    elif user_input == '3':
        string = input("Enter string: ")

        def is_palindrome(string):
            cleaned_string = ''.join(c.lower() for c in string if c.isalnum())
                
            if cleaned_string == cleaned_string[::-1]:
                return f'{string} is a palindrome.\n'
            else:
                return f'{string} is not a palindrome.\n'
        
        result = is_palindrome(string)
        print(result)

    else:
        print("Enter a valid instruction")

except ValueError as e:
    print("Invalid input value: ", e)

except Exception as e:
    print("Something went wrong elsewhere!")

else:
    print("Operation Successful...")

finally:
    print("We're Done!!")