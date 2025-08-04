'''
Another example:

The idea here is that for a particular grade, we want to check if it falls within a standard range and tehn print out the grades accordingly
if the grade received is between 65 and 100 then we proceed to finding what grade suits the student best
if however, the grade entered is above 100,the corresponding output is displayed

#Note that ''' ''' are used to denote multiline comments
'''

# grade = 20

# if grade >=65 and grade <=100:
#     print('Bella got a passing grrade of:', end = ' ')

#     if grade >= 90:
#         print('A')
#     elif grade >= 80:
#         print('B')
#     elif grade >= 70:
#         print('C')
#     elif grade >=65:
#         print('D')
#     elif grade > 100:
#         print('Invalid input')
# else:
#     print('Failing grade')

# data_balance = 0

# while data_balance == 0:
#     print("Still waiting for data to be credited...")
#     # After a while, data is credited
#     data_balance = 100

# print("You now have data!")

# number = 0
# while number < 5:
#     print(number)
#     number = number + 1 #a counter

import os
import os.path
import platform

# print(platform.__doc__)
# help(platform)
help(os.path)
print(platform.machine())
print(platform.uname)