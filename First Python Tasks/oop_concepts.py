'''
CONCEPTS OF OOP

Encapsulation: groups related functions and variables together = reduce complexity and increase reusability

Abstraction: hides the details and complexities and shows the essential = reduces complexity and isolates the impact of changes in the code

Inheritance: eliminates redundant code

Polymorphism: refactor ugly switch/case statements

Inheritance
It is the ability of one class to derive or inherit the properties from another class. It also has it's types.

It represents real world relationships
We don't have to write the same code again and again and we can add more features to a class without modifying it
'''

'''
1. Single inheritance
A single parent to child relationship


# What the code looks like without any inheritance

class A:
    def m1():
        pass
    def m2():
        pass

class B:
    def m1():
        pass
    def m2():
        pass
    def m3():
        pass
    def m4():
        pass

#Notice how we had to copy and paste all the methods from classA to ClassB, imagine we have these for a more complex code
'''

# With Inheritance

# This is the parent class
class A:
    def m1(self):
        print("Class A, method 1")
    
    def m2(self):
        print("Class A, method 2")

# The child class inheriting from the parent class
class B(A):
    def m3(self):
        print("Class B, method 3")
    
    def m4(self):
        print("Class B, method 4")

# testing
b = B()
b.m1()
b.m3()


'''
2. Multilevel inheritance
A single parent, a child and a grandchild (as you know, from the child)

Parent -> Child1 -> grandchild

class A:
    def m1():
        pass
    def m2():
        pass

class B:
    def m1():
        pass
    def m2():
        pass
    def m3():
        pass
    def m4():
        pass

class C:
    def m1():
        pass
    def m2():
        pass
    def m3():
        pass
    def m4():
        pass
    def m5():
        pass
    def m6():
        pass
'''

# How multilevel inheritance solves this problem

# The Parent class
class A:
    def m1(self):
        print("Class A, method 1")

    def m2(self):
        print("Class A, method 2")

# The child class inheriting from the parent class
class B(A):
    def m3(self):
        print("Class B, method 3")
    
    def m4(self):
        print("Class B, method 4")

# The grandchild class inheriting from the child class that is inheriting from the parent class
class C(B):
    def m5(self):
        print("Class C, method 5")
    
    def m6(self):
        print("Class C, method 6")

#testing the concept
b = B()
c = C()

b.m2()
c.m1()


'''
3. Multiple inheritance
One child inheriting from two parents
'''

# Parent class
class A:
    def m1(self):
        print("Class A, method 1")

    def m2(self):
        print("Class A, method 2")

# Parent class
class B:
    def m3(self):
        print("Class B, method 3")
    
    def m4(self):
        print("Class B, method 4")

# the child class inheriting from both Parent classes
class C(A,B):
    def m5(self):
        print("Class C, method 5")
    
    def m6(self):
        print("Class C, method 6")

c = C()

c.m1()
c.m3()


'''
4. Hirerachical inheritance
Two children inheriting from a single parent
'''

#parent
class A:
    def m1(self):
        print('Class A, method 1')
    def m2(self):
        print('Class A, method 2')

#first child
class B(A):
    def m3(self):
        print('Class B, method 3')
    def m4(self):
        print('Class B, method 4')

#second child
class C(A):
    def m5(self):
        print('Class C, method 5')
    def m6(self):
        print('Class C, method 6')

b = B()
c = C()

b.m1()
c.m2()


'''
5. Hybrid inheritance
A combination of all the above types of inheritance.
'''

#parent
class A:
    pass

#first child of A
class B(A):
    pass

#second child of A
class C(A):
    pass

#child benefiting from other children
class D(B, C):
    pass


#Class B and C share the same parent - hirerachical
#Class D has a direct relationship with the parent and the second child


'''
Using super() to access the constructor and methods of the parent class
'''

class A:
    def m1(self):
        print('Class D, method 1')
    def m2(self):
        print('Class D, method 2')

# inheriting from the parent class
class B(A):
    def m3(self):
        super().m1()  # used to access the properties of the parent class from the child class
        print("Class B, method 3")

    def m4(self):
        super().m2()  # used to access the properties of the parent class from the child class
        print("Class B, method 4")
    
b = B()
b.m3()
b.m4()


'''
Polymorphism
Means that one thing can take multiple forms. Thinking about this literally, we human beings are polymorphic, we have different forms, as the situation changes, we change ourselves, the way we behave around friends, is not the same way we behave in the office.

In OOP therefore, objects can have multiple forms. There are 4 kinds of polymorphism:

- Duck typing
- Operator overloading
- Method overloading
- Method overriding
'''

'''
1. Duck typing
Here we have a function that takes an object and calls a method on it without caring about the object's type
Duck typing means that as long as the object has the required method, it can be used without caring about the object's type
Example: a duck and a dog can both have the quack() method and therefore can be treated the same in the code without checking for their specifc types
'''

class Duck:
    def quack(self):
        return("Quack")
    
class Dog:
    def quack(self):
        return("Woof")
    
def make_sound(animal):
    animal.quack()

# creating objects
duck = Duck()
dog = Dog()

print(duck.quack())
print(dog.quack())

'''
#python functions displaying polymorphism

print(len('Data engineering'))
print(len([123, 456, 789, 102]))

The len function exhibits polymorphism because it can be used with different types of objects (strings and lists in this case) that provide the required len method.

This code demonstrates duck typing because it doesn't explicity check the object's class(it doesn't care).
'''

'''
2. Operator overloading
Arithmetic operations like +,-, *,/ are actions I can perform on objects
Operator loading therefore lets me define what those actions mean for instances of my own classes
This is done using '__add__' method
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
#creating two objects with the same blueprint
p1 = Point(2,3)
p2 = Point(4,5)

result = p1 + p2
print(result)

print(result.x, result.y)


'''
3. Method overloading
Here we have a method with the capacity to house or take in different number of parameters - a very good example here is our round() method
Method overloading allows me to define multiple versions of a method with different parameter lists
When you call the method, the appropriate version is choosen based on the arguments you provide
'''

#see what I mean

#first form - pass only the number you wish to round up - default state says it rounds the number to a whole number
check1 = round(45.9800001)
print(check1)

#second form - pass the number and the number of decimal places
check2 = round(45.98076512, 3)
print(check2)

# Lets create something similar
class Calculator:
    def calculate(self, a, b=None):
        if b is None:
            return a*2
        else:
            return a*b
        
my_calc = Calculator()

print(my_calc.calculate(5))
print(my_calc.calculate(3,5))


'''
4. Method overriding
First I have a parent class with a method
When I create a subclas, I can now define the same method with the same name
Method overriding means that I am replacing the parent's method with a new implementation in the subclass
This allows me to customize the behaviour of the method for the subclass without changing the parent's behaviour
'''

# Parent class
class A:
    def m1(self):
        print('Class A, method 1')
    def m2(self):
        print('Class A, method 2')

# Child class
class B(A):
    def m1(self):
        super().m1()
        print("I changed the output")

b = B()

# method overriding in action
b.m1()


'''
Object Oriented Programming Continued...........
Encapsulation: groups related functions and variables together = reduce complexity and increase reusability

Abstraction: hides the details and complexities and shows the essential = reduces complexity and isolates the impact of changes in the code

Inheritance: eliminates redundant code

Polymorphism: refactor ugly switch/case statements

Inheritance
It is the ability of one class to derive or inherit the properties from another class. It also has it's types.

It represents real world relationships
We don't have to write the same code again and again and we can add more features to a class without modifying it
1. Single inheritance
A single parent to child relationship


[ ]
# What the code looks like without any inheritance

class A:
    def m1():
        pass
    def m2():
        pass

class B:
    def m1():
        pass
    def m2():
        pass
    def m3():
        pass
    def m4():
        pass

#Notice how we had to copy and paste all the methods from classA to ClassB, imagine we have these for a more complex code

[ ]
# With inheritance

#This is the parent class
class A:
    def m1(self):
        print('Class A, method 1')
        
    def m2(self):
        print('Class A, method 2')



[ ]
#testing the concept

b = B()

b.m1()
b.m3()
Class A, method 1
Class B, method 3
2. Multilevel inheritance
A single parent, a child and a grandchild (as you know, from the child)

Parent -> Child1 -> grandchild


[ ]
## What the code looks like without inheritance

class A:
    def m1():
        pass
    def m2():
        pass

class B:
    def m1():
        pass
    def m2():
        pass
    def m3():
        pass
    def m4():
        pass

class C:
    def m1():
        pass
    def m2():
        pass
    def m3():
        pass
    def m4():
        pass
    def m5():
        pass
    def m6():
        pass



[ ]
#How multilevel inheritance solves this problem

#parent
class A:
    def m1(self):
        print('Class A, method 1')
    def m2(self):
        print('Class A, method 2')

#child 
class B(A):
    def m3(self):
        print('Class B, method 3')
    def m4(self):
        print('Class B, method 4')

#grandchild        
class C(B):
    def m5(self):
        print('Class C, method 5')
    def m6(self):
        print('Class C, method 6')

[ ]
#testing the concept
b = B()
c = C()

print(b.m2())
print(c.m1())

#remember why we see 'None' in the output right? Yes. It's because we used print in the function call instead of return
Class A, method 2
None
Class A, method 1
None
3. Multiple inheritance
One child inheriting from two parents


[ ]
#parent
class A:
    def m1(self):
        print('Class A, method 1')
    def m2(self):
        print('Class A, method 2')

#parent
class B:
    def m3(self):
        print('Class B, method 3')
    def m4(self):
        print('Class B, method 4')

#child
class C(A,B):
    def m5(self):
        print('Class C, method 5')
    def m6(self):
        print('Class C, method 6')
4. Hirerachical inheritance
Two children inheriting from a single parent


[ ]
#keep in mind the last code without inheritance we wrote

#parent
class A:
    def m1(self):
        print('Class A, method 1')
    def m2(self):
        print('Class A, method 2')

#first child
class B(A):
    def m3(self):
        print('Class B, method 3')
    def m4(self):
        print('Class B, method 4')

#second child
class C(A):
    def m5(self):
        print('Class C, method 5')
    def m6(self):
        print('Class C, method 6')

[ ]
c = C()

c.m2()
Class A, method 2

[ ]
c.m2()
Class A, method 2
5. Hybrid inheritance
A combination of all the above types of inheritance.


[ ]
#parent
class A:
    pass

#first child of A
class B(A):
    pass

#second child of A
class C(A):
    pass

#child benefiting from other children
class D(B, C):
    pass


#Class B and C share the same parent - hirerachical
#Class D has a direct relationship with the parent and the second child
Using super() to access the constructor and methods of the parent class

[ ]
class A:
    def m1(self):
        print('Class A, method 1')
    def m2(self):
        print('Class A, method 2')

class B(A):
    def m3(self):
        super().m1()
        print('Class B, method 3')

Polymorphism
Means that one thing can take multiple forms. Thinking about this literally, we human beings are polymorphic, we have different forms, as the situation changes, we change ourselves, the way we behave around friends, is not the same way we behave in the office.

In OOP therefore, objects can have multiple forms. There are 4 kinds of polymorphism:

Duck typing
Operator overloading
Method overloading
Method overriding
1. Duck typing
Here we have a function that takes an object and calls a method on it without caring about the object's type
Duck typing means that as long as the object has the required method, it can be used without caring about the object's type
Example: a duck and a dog can both have the quack() method and therefore can be treated the same in the code without checking for their specifc types

[ ]
class Duck:
    def quack(self):
        return('Quack')
    
class Dog:
    def quack(self):
        return('Woof')

def make_sound(animal):
    animal.quack()

[ ]
#creating the objects

duck = Duck()
dog = Dog()

print(dog.quack())
print(duck.quack())
Woof
Quack
Double-click (or enter) to edit


[ ]
#python functions displaying polymorphism

print(len('Data engineering'))
print(len([123, 456, 789, 102]))
16
4
The len function exhibits polymorphism because it can be used with different types of objects (strings and lists in this case) that provide the required len method.

This code demonstrates duck typing because it doesn't explicity check the object's class(it doesn't care).

2. Operator overloading
Arithmetic operations like +,-, *,/ are actions I can perform on objects
Operator loading therefore lets me define what those actions mean for instances of my own classes
This is done using 'add'

[ ]
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
    def __add__(self,other):
        return Point(self.x+other.x, self.y+other.y)

[ ]
#creating two objects with the same blueprint

p1 = Point(2,3)
p2 = Point(3,4)

result = p1 + p2
print(result)
<__main__.Point object at 0x00000127606CBE80>

[ ]
print(result.x, result.y)
5 7
3. Method overloading
Here we have a method with the capacity to house or take in different number of parameters - a very good example here is our round() method
Method overloading allows me to define multiple versions of a method with different parameter lists
When you call the method, the appropriate version is choosen based on the arguments you provide

[ ]
#see what I mean

#first form - pass only the number you wish to round up - default state says it rounds the number to a whole number
check1 = round(45.9800001)
print(check1)

#second form - pass the number and the number of decimal places
check2 = round(45.98076512, 3)
print(check2)
46
45.981

[ ]
#let me create something similar

class Calculator:
    def calculate(self, a, b=None):
        if b is None:
            return a*2
        else:
            return a*b
my_calc = Calculator()

[ ]
print(my_calc.calculate(5))
print(my_calc.calculate(5,10))
10
50
4. Method overriding
First I have a parent class with a method
When I create a subclas, I can now define the same method with the same name
Method overriding means that I am replacing the parent's method with a new implementation in the subclass
This allows me to customize the behaviour of the method for the subclass without changing the parent's behaviour

[ ]
class A:
    def m1(self):
        print('Class A, method 1')
    def m2(self):
        print('Class A, method 2')

class B(A):
    def m1(self):
        super().m1()
        print('I changed the output!')


[ ]
b = B()

#method overriding in action
b.m1()
Class A, method 1
I changed the output!
Abstraction
This means hiding. It simplifies complex functionalities by focussing on what an object does rather than how it does it. It hides the inner workings of an object and exposes only the essential features you need to interact with it.

For example, the light switch is an abstracted object of all the internal workings behind it. We only know that when we flip the switch it either comes on or not.
'''


'''
Encapsulation
This hides data from external world. It protects the data within the class and exposes methods to the world.
'''

# Private Methods

class Car:
    def __init__(self):
        self.__updateSoftware()
    
    def drive(self):
        print("Driving")

    def __updateSoftware(self):
        print("Updating Software...")

myCar = Car()

myCar.drive()

# Private variables

class Car:
    __maxSpeed = 0
    __name = ''
    def __init__(self):
        self.__maxSpeed = 200
        self.name = 'Super car'
    
    def drive(self):
        print('Max speed is', self.__maxSpeed)        

myCar = Car()
myCar.drive()

# Use setter and getter
class Student:
    
    __college = 'LMN'

    def __init__(self, name, rno, marks):
        self.__name = name
        self.__rno = rno
        self.__marks = marks
        
    def display(self):
        print('Name: {}, Roll_number: {}, Marks: {}'.format(self.name, self.rno, self.marks))
        print('College:', self.__college)
        
    def setCollege(self, cname):
        self.__college = cname
        
    def getName(self):
        return self.__name

class Student2:
    
    __college = 'LMN'
    
    #I added a static variable here
    college2 = 'LMER'
    
    def __init__(self, name, rno, marks):
        self.__name = name
        self.__rno = rno
        self.__marks = marks
        
    def display(self):
        print('Name: {}, Roll_number: {}, Marks: {}'.format(self.name, self.rno, self.marks))
        print('College:', self.__college)
        
    def setCollege(self, cname):
        self.__college = cname
        
    def getName(self):
        return self.__name
    

'''
Create a class Animal as a base class and define method animal_attribute.
Create another class Tiger which is inheriting Animal and access the base class method.
'''

class Animal:
    def animal_attribute(self, sound, color):
        self.sound = sound
        self.color = color
        return('My pet {} and is {} in color'.format(self.sound, self.color))

class Tiger(Animal):
    def new_func(self):
        print('New function')

pet = Tiger()

print(pet.animal_attribute('roars', 'black'))


'''
Create a class Cop. Initialize its name, age , work experience. Define methods to display and update the details. Create another class Mission which extends the class Cop. Define method add_mission _details.
Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.
'''

class Cop:
    
    def __init__(self, name, age, work, experience):
        self.name = name
        self.age = age
        self.work = work
        self.experience = experience
    
    def display(self):
        return(self.name, self.age, self.work, self.experience)
    
    def update_details(self, name, age, work, experience):
        self.name = name
        self.age = age
        self.work = work
        self.experience = experience
        return 'Update completed!'
     
class Mission(Cop):
    def add_mission_details(self, country, LGA):
        self.country = country
        self.LGA = LGA
        print('Name: {}, Age: {}, Work: {}, Experience: {}'.format(self.name, self.age, self.work, self.experience))
        return('Posted to {} in {} LGA'.format(self.country, self.LGA))

police = Mission('Ken', 50, 'Director General', 'High')

print(police.add_mission_details('Nigeria', 'Chikun'))
