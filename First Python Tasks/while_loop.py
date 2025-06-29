tup = (1,2,3,4,5)

prod = 1
index = 0

while index < len(tup):
    prod *= tup[index]   #multiply the current value of prod by tup[index] #'index' is used as a variable to index the values
    index +=1
print('Product = {}'.format(prod))

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