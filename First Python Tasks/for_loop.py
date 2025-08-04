# Accept list of numbers from the user and split by spaces
num_lists = input("Enter numbers separated by spaces: ").split(' ')

# iterate over the splitted list of string numbers, append it into a new list and 
# cast the numbers into integers in the process
num_list = []
for num in num_lists:
    num_list.append(int(num))

# Initialize variables to store the largest and smallest numbers
largest = num_list[-1]
smallest = num_list[-1]

# Iterate over the list of numbers, comparing for the largest and the smallest
for num in num_list:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print(num_list)
print(f"The largest is {largest}")
print(f"The smallest is {smallest}")

# num_list = [1, 2, 3, 4, 5]
# total = 0

# for num in num_list:
#     total += num
# print(total)

# lst = (2,3,4,5,6,7,9)

# print(list(lst))