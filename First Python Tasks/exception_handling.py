'''
This line of codes handle errors gracefully each time they occur.
We have different types of errors such as: ZeroDivisionError, ValueError,
TypeError, ImportError, IndexError, KeyError, AttributeError, FileNotFoundError, e.t.c.
'''

a = 10
b = 2

try:
    print("Resource Open")
    user_input = int(input("Enter a number: "))
    print(user_input/b)

except ZeroDivisionError as e:
    print("Sorry! You cannot divide a number by zero!", e)

except ValueError as e:
    print("Invalid input value!", e)

except TypeError as e:
    print("Oops! check your typing...", e)

except ImportError as e:
    print("Import error occurred!", e)

except NameError as e:
    print("Name error occurred!", e)

except Exception as e:
    print("Something went wrong!", e)

else:
    print("Successful...") # this block runs whenever the try block runs successfully without any exception

finally:
    print("Resource Closed!") # this block will always run whether there's an exception or not


#single except can also handle multiple errors
# a = 10
# b = 0

# try:
#     print("Resource Open")
#     user_input = int(input("Enter a number: "))
#     print(user_input/b)

# #single except can also handle multiple errors
# except (ZeroDivisionError, ValueError, NameError, TypeError, ImportError, AttributeError, FileNotFoundError) as e:
#     print("Sorry! You cannot divide a number by zero!", e)

# finally:
#     print("Resource Closed!")