from calc import add, sub, mul, div
import os
import os.path
import platform

print(add(6,2))

print(sub(9,3))

print(mul(3,8))

print(div(20,2))

#gets prints the name of your operating system
print(os.name)

#gets and prints your current working directory
print(os.getcwd())

#gets and prints the list of all the directories in your root folder
print(os.listdir('.'))

#get and prints the absolute path to your project folder
print(os.path.abspath('.'))

#gets and prints the list of all your operating system environment variables
print(os.environ)

#provides functions to access information about the system where my Python code is currently running
print(platform.version())
print(platform.machine())
print(platform.system())
print(platform.release())
print(platform.platform())
print(platform.win32_ver())

#os.path provides methods to extract info about paths and filenames
print(os.path.isdir(os.getcwd()))
print(os.path.isfile('functions.py'))
print(os.path.exists(os.getcwd()))
print(os.path.getsize('functions.py'))

# os.mkdir('exc_handling.py')
# os.rmdir('exc_handling.py')