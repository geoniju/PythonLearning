# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 16:16:35 2018

@author: gshanth
"""
import pymysql

#open database connection
db = pymysql.connect(host='localhost', port=3306, user='root', 
                     passwd='February@123', db='sys') 
#prepare a cursor object using cursor() method
cursor = db.cursor()

#execute sql query using execute() method
cursor.execute("SELECT VERSION()")

#fetch a single row using fetchone()

data=cursor.fetchone()
print("database version: %s" % data)
##print("database version: {}".format(data))
#disconnect from server
db.close()

"""
create a Database table EMPLOYEE
"""

#open database connection
db=pymysql.connect('localhost','root','February@123','sys')

#prepare a cursor object using cursor method
cursor=db.cursor()

#drop table if already existing using execute() method
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#create table as per requirement

sql = """CREATE TABLE EMPLOYEE (
FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)

#disconnect from server

db.close()


"""
The following example, executes SQL INSERT statement to create a record in the EMPLOYEE table
"""
#open database connection
db=pymysql.connect('localhost','root','February@123','sys')

#prepare a cursor object using cursor method
cursor=db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    #execute the sql command
    cursor.execute(sql)
    #commit changes to the database
    db.commit()
except:
    #rollback in case any error
    db.rollback()
# disconnect from server
db.close()


"""
Create sql queries dynamically
"""

#open database connection
db=pymysql.connect('localhost','root','February@123','sys')

#prepare a cursor object using cursor method
cursor=db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
   LAST_NAME, AGE, SEX, INCOME) \
   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
   ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

"""
queries all the records from EMPLOYEE table having salary more than 1000 
"""

# Open database connection
db=pymysql.connect('localhost','root','February@123','sys')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   type(results)
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      print ("fname = %s,lname = %s,age = %d,sex = %s,income = %d" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()

"""
The following procedure updates all the records having SEX as 'M'. Here, 
we increase the AGE of all the males by one year.
"""


# Open database connection
db=pymysql.connect('localhost','root','February@123','sys')

# prepare a cursor object using cursor() method
cursor = db.cursor()


# Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

"""
Following is the procedure to delete all the records from EMPLOYEE 
where AGE is more than 20 
"""


# Open database connection
db=pymysql.connect('localhost','root','February@123','sys')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to DELETE required records
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()



import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:myserver.database.windows.net' 
database = 'mydb' 
username = 'myusername' 
password = 'mypassword' 
cnxn = pyodbc.connect('DSN=SQLS;UID='+'CORP\gshanth'+';PWD=' +'August@123')
cursor = cnxn.cursor()
employee=cursor.execute('SELECT * FROM [Chapter 2 - Sales].dbo.calendar')
employee_data=employee.fetchone()
type(employee_data)

for employee in employee_data:
    empdate=str(employee)


 

#Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0]) 
    row = cursor.fetchone()
    
#Sample insert query
cursor.execute("INSERT SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, CURRENT_TIMESTAMP )") 
row = cursor.fetchone()

while row: 
    print 'Inserted Product key is ' + str(row[0]) 
    row = cursor.fetchone()