for gala in range(10):
    if gala == 5:
        break  # Stop buying after the fifth gala
    print(f"Bought gala number {gala + 1}")
print('Stop buying gala')

## WARNING - INFINITE LOOP - your tab might crash
number = 0

while number < 5:
    print(number)

    if number == 3:
        continue  #anything beneath this continue function is not executed, it just keeps going back to the start of the for loop and results in an infinite loop
    number = number +1
else:
    print('No longer < 5')

