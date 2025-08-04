'''
What is Object-Oriented Programming (OOP)?
Object-Oriented Programming (OOP) is a way of writing programs by creating things called objects. These objects can hold data and also perform actions. Each object has two main parts:

Attributes: These are the features of the object (like the color of a car or the model of a phone).
Methods: These are the actions the object can perform (like a car driving or a phone making a call).
Why Use OOP?
OOP makes it easier to organize and manage larger programs by:

Keeping related data and actions together.
Reusing code without repeating yourself.
Making programs more structured and easier to understand.
OOP mirrors the way the world works.

Code is organized into self contained parts/objects - like the objects around you now

By structuring code as objects we can change one part of it and it won't affect the others.

A class is a definition or blueprint from which objects are created. E.g The blueprint of a car tells us what the car has or is made of - body, wheels, engine, and what a car does (functionalities) - drive(), brake(), turn(). Now we can take this blueprint to build a car - which is now known as an object.
'''

'''
Constructors
A special method
It gets called automatically at object intialization/instantiation
It is used for intializing the variables (very important)
Returns None
'''
# class HelloWorld:
#     # Creating constructor using dunder __init__
#     def __init__(self, name):
#         self.name = "Ifeanyi"
#         print("Constructor __init__ called immediately the object 'hello_obj' is created")

#     def display(self):
#         print('Hello World!')

# hello_object = HelloWorld()
# print(hello_object)

# hello_object.display()

# Constructor with mulitiple parameters
'''
'self' is an instance variable that should be used in the constructor or method
Remember the constructor is automatically called when you create an instance of an object
'''

# class Student:
#     def __init__(self, name, rno, marks):  #a constructor with the instance variables
#         self.name = name
#         self.rno = rno
#         self.marks = marks
    
#     #creating a method
#     def display(self):
#         #print(self.name, self.rno, self.marks) OR
#         print('Name: {}, Row_number: {}, Marks: {}'.format(self.name, self.rno, self.marks))
        
#         # print('Name: {}, Room_number: {}, Marks: {}'.format(self.name, self.rno, self.marks))

# #testing
# student1 = Student('Ann', 1, 98)
# print(student1.__dict__)

# if __name__ == '__main__':
#     student1.display()

'''
TYPES OF VARIABLE (PROPERTIES)
A. Instance Variable
- It is an object level variable
- The value of this variable varies from object to object, that is, they are only present for that one instance of an object

B. Static variable AKA class variable
- It is a class level variable
- These variables are the same for all objects

C. Local Variable
- This is a method level variable - avaiable within a method

How to access the Instance variable
--> Inside a class: self.variable_name
--> Outside a class: object_name.variable_name
'''

# class Student:
#     def __init__(self, name, rno, marks):
#         self.name = name
#         self.rno = rno
#         self.marks = marks
    
#     # creating a method
#     def display(self):
#         print(self.name, self.rno, self.marks) # accessing inside a class

# #testing
# student = Student("Ifeanyi", 1, 90)  # accessing outside a class
# student.display()


'''
How to access the static variable
--> Inside a class: ClassName.variable_name OR self.variable_name
--> Outside a class: ClassName.variable_name OR object_name.variable_name
'''
# class Student:
#     college = 'Stanford' #static variable
    
#     def __init__(self, name, rno, marks):
#         self.name = name
#         self.rno = rno
#         self.marks = marks
    
#     def display(self):
#         print(self.name, self.rno, self.marks)
#         print(self.college)  #accessing the static variable inside a class

# student2 = Student('Ann', 2, 98)
# student3 = Student('John', 6, 76)

# student2.display()
# student3.display()

# # accessing the static variable outside the class
# print(Student.college)  #using the ClassName
# print(student2.college)  #using the object_name

# #let us see if we can change this static variable
# Student.college = 'ABCD'

# student2.display()
# student3.display()


# # Local Variable
# class Test:
#     def m1(self):
#         x = 10
#         print(x)
    
#     def m2(self):
#         y = 20
#         print(y)

# test = Test()
# test.m1()
# test.m2()


# '''
# TYPES OF METHODS (BEHAVIOURS)
# Instance method

# - Uses the self parameter which indicates that or points to an object instance
# - Instance variables are used with instance methods
# - Can be used to modify the instance state
# '''

# class Pupil:
#     school = 'NASA'

#     def __init__(self, m1, m2, m3):
#         print("__init__ method called once s1 object was instantiated")
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     # defining an instance method - you can see it uses the self parameter
#     def avg(self):
#         return(self.m1+self.m2+self.m3)/3
    
# s1 = Pupil(34, 45, 67)
# print(s1)
# print(s1.avg())


'''
Class method

- Uses the cls parameter which indicates that or points to the class and not the object instance when the method is called
- Class(i.e static) variables are used with class methods
'''

# class Pupil:
#     school = "NASA"

#     def __init__(self, m1, m2, m3):
#         print("__init__ method called once s1 object was instantiated")
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     # defining an instance method - you can see it uses the self parameter
#     def avg(self):
#         return(self.m1+self.m2+self.m3)/3   

#     # creating a class method using @classmethod decorator
#     @classmethod
#     def getSchool(cls):
#         return cls.school

# s1 = Pupil(42, 35, 38)
# print(s1)
# s1.m1 = 50
# print(s1.avg())

# # remember that the class method points to the class name
# print(Pupil.getSchool())


'''
Static Method

- Uses neither the self or cls parameter
- It is free to accept an arbitary number of other parameters
- Cannot modify object or class state. It is only restricted to the data they can access
'''

# class Pupil:
#     school = 'NASA'
    
#     def __init__(self, m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def avg(self):
#         return(self.m1+self.m2+self.m3)/3
    
#     #creating a class method using the @classmethod decorator
    
#     @classmethod
#     def getSchool(cls):
#         return cls.school
    
#     # Always kept blank
#     @staticmethod
#     def info():
#         return "I am a Data Scientist"
    
# s1 = Pupil(34, 45, 67)

# print(s1.info())
# print(Pupil.info())


'''
ACCESS MODIFIERS
Used to restrict the access to the variables and methods. Python uses the _ symbol to determine the acess control

Public

- No symbol is used here
- Members (data and functions of a class) defined as public will be accessible from any part of the program
- This is the default state unless otherwise stated

Private

- Uses a double underscore __ symbol before the data member of that class
- Members of a class declared private are accessible within the class only
- Most secure

Protected

- Uses a single underscore _ symbol before the data member of that class
- Members of a class declared protected are only accessible to a class derived from it
'''

# class Boy:
#     def __init__(self, name, age):
#         # public data member
#         self.name = name

#         # private data member
#         self.__age = age

#     def display(self):
#         print(self.name)
#         print(self.__age)

# boy = Boy("Franklin", 26)
# boy.display()  #this prints just the name, the age is privately secured and therefore not accessible


# Create a Bottle class with color and capacity properties
# class Bottle:
#     def __init__(self, color, capacity):
#         self.color = color
#         self.capacity = capacity
    
#     def display(self):
#         return ('The color of the bottle is {} with a capacity of {}L'.format(self.color, self.capacity))
    
# mybottle = Bottle("Blue", 120)
# print(mybottle.display())


# Create a Human class with some properties and methods
# class Human:
#     state = "Imo"

#     def __init__(self, gender, height, age, occupation):
#         self.gender = gender
#         self.height = height
#         self.age = age
#         self.occupation = occupation

#     def show_details(self):
#         return(self.gender, self.height, self.age, self.occupation)
    
#     def getState(cls):
#         return(cls.state)

#     def update_details(self, age):
#         self.age = age
#         return 'Age updated Successfully'

# human = Human("Male", 5.5, 26, "Data Scientist")
# print(human.show_details())
# print(human.getState())
# human.update_details(27)
# print(human.show_details())


# Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def getArea(self):
#         return(3.14*(self.radius)**2)
    
#     def getCircumference(self):
#         return(2*3.14*self.radius)
    
# my_circle = Circle(6)
# print(my_circle.getArea())
# print(my_circle.getCircumference())


'''
Create a Student class and initialize it with name and roll number. Make methods to:

Display - It should display all informations of the student.
setAge - It should assign age to student
setMarks - It should assign marks to the student.
'''

# class Student:
#     age = 50
#     marks = 100

#     def __init__(self, name, rno):
#         self.name = name
#         self.rno = rno

#     def display(self):
#         return(self.name, self.rno)
    
#     @classmethod
#     def setAge(cls):
#         return(cls.age)
    
#     @classmethod
#     def setMarks(cls):
#         return(cls.marks)
    
# students = Student(name="Christine", rno=20)
# print(students.display())
# print(Student.__dict__)
# print(Student.setAge())
# print(Student.setMarks())


'''
Create a Temprature class. Make two methods:

convertFahrenheit - It will take celsius and will print it into Fahrenheit.
convertCelsius - It will take Fahrenheit and will convert it into Celsius.
'''

# class Temperature:
#     def __init__(self, x):
#         self.x = x

#     def convertCelsius(self):
#         return((self.x - 32)*5/9)
    
#     def convertFahrenheit(self):
#         return(self.x*(9/5))+32

# temp = Temperature(67)
# print(temp.convertCelsius())
# print(temp.convertFahrenheit())


'''
Create a class Expenditure and initialize it with salary,savings, category , total expenditure.Make the following methods.
Add expenditure according to category.

- Calculate total expenditure.
- Calculate per day expenditure and a two months expenditure.
'''

class Expenditure:
    def __init__(self, salary, savings):
        self.salary = salary
        self.savings = savings
        self.categories = {}  # Initializes an empty dictionary to store the categories
        self.total_expenditure = 0  # To be updated later in the program

    def category_expenditure(self, category, expenses):
        #first, we check if the category exists and then add the amount entered to the expenditure for that category
        if category in self.categories:
            self.categories[category] += expenses

        #if it doesn't it adds the new category and the expense for that category
        else:
            self.categories[category] = expenses

        # When the conditional statement has been fulfilled, the amount is added to the total_expenditure and it is therefore updated
        self.total_expenditure += expenses

        return self.categories, self.total_expenditure
    
    # Remember the total_expensiture is always updated therefore at anytime we have the total expenditure in that variable
    def cal_total_expenditure(self):
        return self.total_expenditure
    
    def daily_expenditure(self):
        days = 30
        return self.total_expenditure/days
    
    def monthly_expenditure(self, month):
        return self.total_expenditure*month
    
expenditure_tracker = Expenditure(salary=5000, savings=1000)  # Instatiation

# Let me add some of the expenses I've made
print(expenditure_tracker.category_expenditure('food', 500))
print(expenditure_tracker.category_expenditure('shoes', 800))
print(expenditure_tracker.category_expenditure('mouse', 1500))
print(expenditure_tracker.category_expenditure('fan', 300))

# checking for total expenditure so far
print(expenditure_tracker.cal_total_expenditure())

# what is my daily expenditure like assuming that the total_expenditure is my total expenses for a month
print(expenditure_tracker.daily_expenditure())

#what will my expenditure be for the next two months
print(expenditure_tracker.monthly_expenditure(3))
