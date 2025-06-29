'''
LIST COMPREHENSION
They offer a more concise way to create new lists in python.
They offer a one-line alternative to using traditional for loops and append statements.
'''

# nums = [12, 23, 34, 56, 67, 78, 89, 90]

# evens = [num for num in nums if num%2 == 0]

# print(evens)

# lst = [a for a in 'PYTHON']
# print(lst)

# l = [12, 23, 34, 56, 67, 78, 89, 90]
# length = [b for b in range(1, len(l)+1)]
# print(length)

# lst = [i**2 for i in range(1, 20) if i%2 != 0]
# print(lst)

# heroes = ['Black Widow', 'Hawkeye', 'Doctor Strange']
# lst = [word[0] for word in heroes]
# print(lst)

# string = 'The quick fox and the slow tortoise were friends a long time ago'

# #convert each word into upper case 
# #and count the number of characters in each word

# # for word in string.split():
# #     splitted = [word.upper(), len(word)]
# #     print(splitted)

# #List comprehension version
# lst = [[word.upper(), len(word)] for word in string.split(' ')]
# print(lst)


'''
ANONYMOUS FUNCTIONS
AKA lambda functions. These are functions defined without a name using the lambda keyword.
They are defined in a sinbgle line of code and can only contain one expression which repesents the function's body and return value.

Syntax: lambda arguments: expression
'''

# Normal function definition
# def square(n):
#     return n**2
# print(square(5))

#Using Lambda
# lambda_sq = lambda n: n**2
# print(lambda_sq(5))

# Using lambda with two arguments
# prod = lambda a,b: a*b
# print(prod(3,4))

# #using lambda again and a concept from list comprehension
# greater = lambda a,b: a if a>b else b
# print(greater(6, 87))


'''
The filter() function
A built-in python functions that allows you to efficiently process an iterable like a tuple,
list or string and return a new iterator containing only the elements that meet a certain condition

Syntax: filter(function, sequence)

Problem: We have 10 numbers and we want to filter only the even numbers from that list.
'''

# def isEven(x):
#     if x%2 == 0:
#         return True
#     else:
#         return False

# lst = [2, 3, 6, 5, 7, 8, 9, 21, 22, 12, 24, 68]
# filtered_list = filter(isEven, lst)
# print(filtered_list)
# print(type(filtered_list))

# filtered_list = list(filter(isEven, lst))
# print(filtered_list)

# Using concise problem solving
# lst = [2, 3, 6, 5, 7, 8, 9, 21, 22, 12, 24, 62]

# filtered_list = list(filter(lambda x: x%2 == 0, lst))
# print(filtered_list)


'''
The map() function
Built-in python function used to apply a function to all elements of an iterable and return a new iterator containing the results

Synatx: map(function, sequence)
'''

# def double(x):
#     return 2*x

# lst = [2, 4, 6, 8, 10]
# new_list = list(map(double, lst))
# print(new_list)

# Concise problem solving using lambda function
# lst = [2, 4, 6, 8, 10]

# new_list = list(map(lambda x: 2*x, lst))
# print(new_list)

# EXAMPLE 2
# Multiply two lists element-wise
# list1 = [2, 4, 6, 8]
# list2 = [10, 12, 14, 16]

# new_list = list(map(lambda x,y: x*y, list1, list2))
# print(new_list)


'''
The reduce() function
This function is used to reduce a sequence of elements nto a single element by applying the specified function

It is present in the functools module.

Syntax

from functools import *

reduce(function, sequence)
'''

from functools import *

lst = [1,2,3,4,5,6,7,8,9,10]

reduced_list = reduce(lambda x,y: x+y, lst)
print(reduced_list)