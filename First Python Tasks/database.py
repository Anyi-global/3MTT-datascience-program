'''
SQLite Database

# How to connect with database in python
import db module
import sqlite3

# Establish connection between the python program and the db
con = sqlite3.connect(name_of_database)

# To execute mysql query and hold result, a cursor is required
cursor = con.cursor()

# Execute mysql query with the help of cursor object
cursor.execute(query)

cursor.executemany()

# Fetch the result from the cursor object in case of select query
cursor.fetchall()

cursor.fetchone()

cursor.fetchmany(n)

# Commit or rollback changes as required
con.commit()

con.rollback()

# Close resources and disconnect database
cursor.close()

con.close()
'''

import sqlite3

# Creating a database connection
# con = sqlite3.connect('Data/Ifeanyi.db')
# print('Connection Established!')
# con.close()

# Creating a database table
# try:
#     con = sqlite3.connect('Ifeanyi.db')
#     cursor = con.cursor()
#     query = 'CREATE TABLE Employee (emp_id int(5) primary key, emp_name varchar(50), emp_age int(3))'
#     cursor.execute(query)

#     print('Table Created Successfully!')
#     con.commit()

# except sqlite3.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('Problem occured: ', e)

# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print('Completed!')

# Adding new columns
# try:
#     con = sqlite3.connect('ifeanyi.db')
#     cursor = con.cursor()
#     query = 'ALTER TABLE Employee add column emp_income double(10,2)'
#     cursor.execute(query)

#     print('Column added successfully!')
#     con.commit()

# except sqlite3.DatabaseError as e:
#     con.rollback()
#     print('Problem occured: ', e)

# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print('Done!')

# Insertion operation
# try:
#     con = sqlite3.connect('ifeanyi.db')
#     cursor = con.cursor()
#     query = 'INSERT INTO Employee (emp_id, emp_name, emp_age, emp_income) VALUES (1, "LMS", 24, 300.52)'
#     cursor.execute(query)

#     con.commit()
#     print('Row inserted!')

# except sqlite3.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('Problem occured: ', e)

# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print('All Done!')

## To add more than one row of data
# try:
#     con = sqlite3.connect('ifeanyi.db')
#     cursor = con.cursor()
#     query = 'INSERT INTO Employee (emp_id, emp_name, emp_age, emp_income) VALUES (?, ?, ?, ?)'
#     records = [(3, 'Joe', 20, 450.12),(4, 'Ifeanyi', 25, 438.23)]

#     cursor.executemany(query, records)
#     con.commit()
#     print('Columns added successfully!')

# except sqlite3.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('Problem occured: ', e)

# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print("Done!")

# Retrieving data from the database
# try:
#     con = sqlite3.connect('ifeanyi.db')
#     cursor = con.cursor()
#     query = 'SELECT * FROM Employee'
#     cursor.execute(query)

#     print(cursor)
#     data = cursor.fetchall()
#     print(data)
    
#     for row in data:
#         print('emp_id: {}, emp_name: {}, emp_age: {}, emp_income: {}'.format(row[0], row[1], row[2], row[3]))

# except sqlite3.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('Problem occured: ', e)
# finally:
#     if cursor:
#         cursor.close()  #close the cursor first then the connection
#     if con:
#         con.close()
#     print('All done!')

# Updating data in the database
# try:
#     con = sqlite3.connect('Ifeanyi.db')
#     cursor = con.cursor()
#     query = 'UPDATE Employee SET emp_age = emp_age + 1 WHERE emp_name = "LMS"'

#     cursor.execute(query)
#     con.commit()

# except sqlite3.DatabaseError as e:
#     if con:
#         con.rollback()
#         print("Problem Occured: ", e)

# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print("Done!")

# Deleting data from the database
# try:
#     con = sqlite3.connect('Ifeanyi.db')
#     cursor = con.cursor()
#     age = input('Enter age: ')
#     query = 'DELETE FROM Employee WHERE emp_age = {}'.format(age)

#     cursor.execute(query)
#     con.commit()
#     print('Deleted Successfully!')

# except sqlite3.DatabaseError as e:
#     if con:
#         con.rollback()
#         print("Problem Occured: ", e)

# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print("Done!")

'''
Reading Data from database table into
Pandas on Jupyter Notebook Environment
'''

import pandas as pd
from sqlalchemy.engine import create_engine

# Using sqlalchemy connectable
engine = create_engine('sqlite:///Data/database.sqlite')

df = pd.read_sql_table('Salaries', engine)
df.head()

'''
Connecting with a MySQL database in python from Jupyter Notebook Environment

#installing libraies

!pip install mysql.connector

!pip install pymysql

#import database module
import pymysql as pm

OR

import mysql.connector as pm

#Establish connection between python program and MySQL db
con = pm.connect(host, database, user, password)

#To execute mysql query and hold result, cursor is required
cursor = con.cursor()

#Execute mysql query with the help of the cursor object
cursor.execute(query)

cursor.executemany()

#Fetch results from cursor object in case of a select query
cursor.fetchone()

cursor.fetchall()

cursor.fetchmany(n)

#Commit or rollback changes based on your requirement
con.commit()

con.rollback()

#Close resources and disconnect database
cursor.close()

con.close()
'''

# Establishing a connection
import mysql.connector as pm

try:
    con = pm.connect(
        host='localhost',
        database='retail_stores',
        user='root',
        password='root'
    )
    print(con)

finally:
    con.close()
    print('Connected Successfully!')

# Creating Database Table Structure
try:
    con = pm.connect(host='localhost', database = 'retail_sales',\
                    user = 'root', password = 'root')

    cursor = con.cursor()

    query = 'CREATE TABLE employees1(eno int(5) PRIMARY KEY,\
             ename varchar(10), eage int(3), eincome double(10,2),\
             FOREIGN KEY(eno) REFERENCES employees(eno))' #make sure you have a table called 'employees in your database'

    cursor.execute(query)

    print('Table created successfully')
    con.commit()

except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!')

# Insert Operation
try:
    con = pm.connect(host='localhost', database = 'retail_sales',\
                    user = 'root', password = 'root')

    cursor = con.cursor()

    query = 'INSERT INTO employees1(eno, ename, eage, eincome)\
            values(%s,%s,%s,%s)' ##We used %s here

    records = [(3, 'ben', 23, 45.67),(4, 'ann', 56, 7890.8)]

    cursor.executemany(query, records)

    print('Table created successfully')
    con.commit()

except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!')

# Reading data from the Database
try:
    con = pm.connect(host='localhost', database = 'retail_sales',\
                    user = 'root', password = 'root')

    cursor = con.cursor()

    query = 'SELECT * FROM employees1'


    cursor.execute(query)
    data = cursor.fetchall()

    for row in data:
        print('Eno: {}, Ename: {}, Eage: {}, Esalary: {}'\
              .format(row[0], row[1], row[2], row[3]))


except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!')

# Updating data in the Database
try:
    con = pm.connect(host='localhost', database = 'retail_sales',\
                    user = 'root', password = 'root')

    cursor = con.cursor()

    query = 'UPDATE employees1 SET eage=eage+1 WHERE ename = "ben"'


    cursor.execute(query)
    con.commit()


except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!')

# Deleting data from the Database
try:
    con = pm.connect(host='localhost', database = 'retail_sales',\
                    user = 'root', password = 'root')

    cursor = con.cursor()

    age = input('Enter a number: ')
    query = 'DELETE FROM employees1 WHERE eage="%s"'%(age)


    cursor.execute(query)
    con.commit()


except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!')

'''
SQLAlchemy ORM
ORM - Object Relational Mapper. It is a python library that simplifies interacting with relational databases. It acts as a bridge between the object-oriented world of python and the structured world of relational databases.

SETUP

Step 1: installing the modules
pip install Flask-SQLAlchemy

pip install Flask-Migrate

Set 2: create a flask app
from flask import Flask

app = Flask(name)

Step 3: import SQLAlchemy and Migrate module
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

Step 4: SQLAlchemy Configuration and pass the application into SQLAlchemy class
basedir = os.path.abspath(os.path.dirname(file))

path = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_DATABASE_URL'] = path app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) Migrate(app, db)

Step 5: Create a model or table

- Create a model class
- Inherit from db.Model
- Provide the table name
- Add columns in the model
- Create _init__and __repr__

class Box(db.Model):
    __tablename__ = 'boxes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    mrp = db.Column(db.Integer)

    def __init__(self, name, mrp):
        self.name = name
        self.mrp = mrp

    def __repr__(self):
        return 'Box Name - {} and MRP- {}'.format(self.name, self.mrp)
Step 6: Run the following commands to migrate the database

set FLASK_APP=app.py

flask db init

flask db migrate -m 'My first DB migrate'

flask db upgrade

# Basic CRUD Operations
i. Create or Insert Operation
box = Box(name = 'biscuit', price = 10) #creating an object

db.session.add(box)

db.session.commit()

ii. Read operation
Box.query.all()

iii. Update operation
box = Box.query.get(2)

box.name = 'aloo'

db.session.commit()

iv. Delete Operation
box = Box.query.get(2)

db.session.delete(box)

db.session.commit()

# Exploring Read Operation usiing filter_by
Syntax - MODEL_NAME.query.filter_by(MODEL_COLUMN_NAME='')

# Getting all the rows if box name is "biscuit" from the database table
Box.query.filter_by(name='biscuit').all()

# Getting only the first row if sabji name is 'biscuit'
Box.query.filter_by(name='biscuit').first()

# Count of rows if box name is "biscuit"
Box.query.filter_by(name='biscuit').count()

# Getting rows by id
Box.query.filter_by(id=2).first()

OR

Box.query.get(2)

# Other powerful queries using filter
Note: filter_by is used for simple queries on the column names using regular kwargs like: User.filter_by(name="Joe")

The same can be accomplished with filter not using kwargs, but instead using operators (==, !=, >, <, etc.) which has been overloaded on the db.users,name object like thus: User.filter(User.name=='Ann')

# Getting all the boxes with the name not equal to "biscuit" from the database table
Box.query.filter(Box.name != "biscuit").all()

LIKE
Box.query.filter(Box.name.like('%b%')).all()

IN
Box.query.filter(Box.name.in_(['biscuit', 'wine'])).all()

AND
Box.query.filter(and_Box.name=='biscuit', Box.price>10)).all()

OR
Box.query.filter(or_(Box.name=='biscuit', Box.price>10)).all()

Order By and JOIN
ORDER BY
Box.query.order_by(Box.name.desc()).all() #you can remove the "desc()" if not needed

Join
db.session.query(Box, Vendor).filter(Box.id==Vendor.sabji_id).all()
'''

