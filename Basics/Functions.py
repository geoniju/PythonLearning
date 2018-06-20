# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 19:07:20 2018

@author: gshanth
"""
#
#def FunctionName(Input):
#    Action
#    return output

def AddOne(Number):
    Output=Number + 1
    return Output

Var = 0 
print(Var)
var2=AddOne(Var)
print(var2)
var3=AddOne(var2)
print(var3)
var4=AddOne(2.1+5.5)
print(var4)



def AddOneAddTwo(NumberOne,NumberTwo):
    Output=NumberOne + 1
    Output+=NumberTwo + 2
    return Output

Sum=AddOneAddTwo(var2,var3)
print(Sum)



def cylindervolume(height,radius):
    pi=3.14
    volume=height * pi * radius
    return volume

print(cylindervolume(5,4))

# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)
    
show_plus_ten(10)

# this returns something
def add_ten(num):
    return(num + 10)
print(add_ten(10))

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))

# default value, passing values by name and position


def cylinder_volume(height, radius=0):
    pi = 3.14159
    return height * pi * radius ** 2

# by position
cylinder_volume(3,2)

# by name
cylinder_volume(height=5,radius=6)


# write your function here
def population_density(population,land_area):
    density=population/land_area
    return density


# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))


def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))

#mThe print statement will output each expression
#separated by spaces, followed by a newline.

print('niju','shanth')
print('geo','george')


# Variable scope

# This will result in an error
def some_function():
    word = "hello"

print(word)



# This works fine
word='duck'

def some_function():
    word = "hello"

def another_function():
    word = "goodbye"

#global scope

# This works fine
word = "hello"

def some_function():
    print(word)

some_function()


#What is the result of running this code? 

egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()
#This causes an UnboundLocalError
#Python doesn't allow functions to modify variables that are 
#outside the function's scope. A better way would be 
#to pass the variable as an argument and reassign 
#it outside the function. 

def population_density(population, land_area):
    """Calculate the population density of an area. """## doc string example
    return population / land_area


def population_density(population, land_area):
    ## Multiple line docstring
    """Calculate the population density of an area. 

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT: 
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area


#lambda expressions
    

def multiply(x, y):
    return x * y

multiply = lambda x,y:x*y


multiply(4,5)


"""
+ Addition
- Subtraction
* Multiplication
/ Division
% Mod (the remainder after dividing)
** Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
// Divides and rounds down to the nearest integer
"""
"""
My electricity bills for the last three months have been $23, $32 and $64.
 What is the average monthly electricity bill over the three month period? 
 Write an expression to calculate the mean, and use print() to view 
 the result.
"""

# Write an expression that calculates the average of 23, 32 and 64.
# Place the expression in this print statement.
print((23 + 32 + 64)/3)


# Fill this in with an expression that calculates how many tiles are needed.
print(9*7 + 5*7)
# Fill this in with an expression that calculates how many tiles will be left over.
print(17*6 - (9*7 + 5*7))


""" Assign and Modify Variables"""
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff

# add the rainfall variable to the reservoir_volume variable

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm

# decrease reservoir_volume by 5% to account for evaporation

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.

# print the new value of the reservoir_volume variable


"""
Comparison Operators
Symbol Use Case 	Bool 	Operation
5 < 3 	False 	Less Than
5 > 3 	True 	Greater Than
3 <= 3 	True 	Less Than or Equal To
3 >= 5 	False 	Greater Than or Equal To
3 == 5 	False 	Equal To
3 != 5 	True 	Not Equal To

And there are three logical operators you need to be familiar with:
Logical Use 	Bool 	Operation
5 < 3 and 5 == 5 	False 	and - Evaluates if all provided statements are True
5 < 3 or 5 == 5 	True 	or - Evaluates if at least one of many statements is True
not 5 < 3 	True 	not - Flips the Bool Value
"""

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density>rio_de_janeiro_pop_density)

#other way but less efficient

if (san_francisco_pop_density > rio_de_janeiro_pop_density):
    print (True)
else:
    print (False)
    
""" Strings """

my_string = 'this is a string!'
my_string2 = "this is also a string!!!"

"""You can also include a \ in your string to be able to
 include one of these quotes:"""

this_string = 'Simon\'s skateboard is in the garage.'
print(this_string)
    
first_word = 'Hello'
second_word = 'There'

"""You can concatenate or repeat string using + and * """

print(first_word + second_word)
print(first_word + ' ' + second_word)

print(first_word * 5)
print((first_word + ' ') * 5)


"""You can also index on the string"""

first_word[0]
first_word[0:2]

"""len() is a built-in Python function that
 returns the length of an object, like a string in integer 
 format"""
 

print(len("ababa") / len("ab"))

type(len("ababa") / len("ab"))

"""Notice that the resultant value is a float"""


# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'

coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)

#What will be the output of this code?
type(tropical_fruit_count)


username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."


print(username + " accessed the site " + url + " at " + timestamp + ".")

"""
Use string concatenation and the len() function to find the length of a certain movie star's 
actual full name. Store that length in the name_length variable. Don't 
forget that there are spaces in between the different parts of a name!"""

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name + ' ' + middle_names + ' ' + family_name)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

len(835)


"""
Type and Type Conversion

You have seen four data types so far:

    int
    float
    bool
    string
"""

print(type(4))

print(type(3.7))

print(type('this'))

print(type(True))


"""

Calculate and print the total sales for the week from the data provided. 
Print out a string of the form "This week's total sales: xxx", where xxx will 
be the actual total of all the numbers. 

"""
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

total_sales=str(int(mon_sales)+int(tues_sales)+int(wed_sales)+int(thurs_sales)+int(fri_sales))
print("This week's total sales:" + " " + total_sales )

"""
String Methods

A method in Python behaves similarly to a function. Methods actually 
are functions that are called using dot notation. For example, lower() is a 
string method that can be used like this, on a string called "sample string": 
    sample_string.lower()
 """
 
my_string = "sebastian thrun"
my_string.islower()
my_string.isupper()
my_string.title()
"""
Each of the methods accepts the string itself as the first argument of the 
method. However, they also could receive additional arguments, that are passed
 inside the parentheses. 

"""
   
my_string.count('a')

my_string.find('a')


""" format() """

# Example 1
print("Mohammed has {} balloons".format(27))


# Example 2
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

# Example 3
maria_string =  "Maria loves {} and {}"
print(maria_string.format("math","statistics"))


""" If you need to include a brace character in the 
literal text, it can be escaped by doubling: {{ and }}."""

2.34.islower()


# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# and try them out here

print(animal.capitalize())
print(animal.casefold())
print(animal.center(10))
.
.
.
.
"""format() Practice"""

# Write two lines of code below, each assigning a value to a variable


# Now write a print statement using .format() to print out a sentence and the 
#   values of both of the variables



print("the sum of {} + {} is 5".format(2,3))

""" Lists! """

list_of_random_things = [1, 3.4, 'a string', True]

#to pull the first element of the list
list_of_random_things[0]

#to pull the last element of the list
list_of_random_things[len(list_of_random_things) - 1]


"""Alternatively, you can index from the end of a list by using negative values,
 where -1 is the last element, -2 is the second to last element and so on."""


list_of_random_things[-1] 

list_of_random_things[-2]

"""Slice and Dice with Lists"""

list_of_random_things = [1, 3.4, 'a string', True]
list_of_random_things[1:2]
list_of_random_things[:2]
list_of_random_things[1:]

"""This type of indexing works exactly the same
 on strings, where the returned value will be a string."""
 
 
'this' in 'this is a string'

'in' in 'this is a string'

'isa' in 'this is a string'

5 not in [1, 2, 3, 4, 6]

5 in [1, 2, 3, 4, 6]

"""
Mutability and Order

Mutability is about whether or not we can change an object once it has been created. 
If an object (like a list or string) can be changed (like a list can), then 
it is called mutable. However, if an object cannot be changed with creating a 
completely new object (like strings), then the object is considered immutable.
"""
#mutability works on list
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)

#However following code does not work 
greeting = "Hello there"
greeting[0] = 'M'


"""
There are two things to keep in mind for each of the data types you are using:

    Are they mutable?
    Are they ordered?
"""


"""Both strings and lists are ordered."""

"""
List indexing quiz

Use list indexing to determine how many days are in a particular month based 
on the integer variable month, and store that value in the integer variable num_days.
"""

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month

num_days=days_in_month[7:8]
print(num_days)

"""Select the three most recent dates from this list using list slicing notation"""

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[6:-1])



"""Useful Functions for Lists I

len() returns how many elements are in a list.

max() returns the greatest element of the list. 

min() returns the smallest element in a list

sorted() returns a copy of a list in order from smallest to largest, leaving the list unchanged.

"""

max(eclipse_dates)

sorted(eclipse_dates)

"""
Useful Functions for Lists II
join method

Join is a string method that takes a list of strings as an argument,
 and returns a string consisting of the list elements joined by a separator string.

"""

new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

name = "-".join(["García", "O'Kelly"])
print(name)

"""
append method

append adds an element to the end of a list.
"""

letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)

"""

Quiz: len, max, min, and Lists

What would the output of the following code be?
"""


a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))


"""
Quiz: sorted, join, and Lists

What would the output of the following code be? 

"""

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))


"""
Quiz: append and Lists

What would the output of the following code be?
"""

names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))    

# Use this playground to experiment with list methods, using Test Run

names_copy = names
names_copy[0]='Niju'

names.


"""
Tuples

It's a data type for immutable ordered sequences of elements. 
"""


location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])


"""Tuples can also be used to assign multiple variables in a compact way."""

dimensions = 52, 40, 100

#Tuple unpacking
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

"""The parentheses are optional when defining tuples"""


length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))

"""What would the output of the following code be? """


tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])

"""Tuples Playground"""

## You may test any code out here. Use Test Run to see your output

tuple_a.index(2)
tuple_a.count(1)


""" 
Sets 

A set is a data type for mutable unordered collections of unique elements. 
One application of a set is to quickly remove duplicates from a list.

"""

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

"""
Sets support the in operator the same as lists do. You can add elements to 
sets using the add method, and remove elements using the pop method, similar to lists.
"""


fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)


""" What would the output of the following code be? """

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))


"""Quiz: add and pop"""

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()

"""Set Playground"""

## You may test any code out here. Use Test Run to see your output

""" 
Dictionaries and Identity Operators 
A dictionary is a mutable data type that stores mappings of unique keys to values. 
"""

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

"""Dictionaries can have keys of any immutable type, 
like integers or tuples, not just strings."""


print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary


elements['lithium']


"""
We can check whether a value is in a dictionary the same way we check whether
 a value is in a list or set with the in keyword.'get' looks up values in a 
 dictionary, but unlike square brackets, get returns None (or a default 
 value of your choice) if the key isn't found.
"""

print("carbon" in elements)
print(elements.get("dilithium")) #better to use if u expect lookup to fail
print(elements['dilithium'])

"""
Identity Operators

is --	evaluates if both sides have the same identity
is not 	-- evaluates if both sides have different identities

"""

n = elements.get("dilithium")
print(n is None)
print(n is not None)
elements

print(elements['carbon'] is 6)  #to check for values in dictionary


print('carbon' in elements ) # in checks for keys in dictionaries


"""
Quiz: Define a Dictionary

Define a dictionary named population that contains this data:
    """
    
    
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5
    
population= {'Shanghai':17.8,'Istanbul':13.3,'Karachi':13.0,'Mumbai':12.5 }


"""get with a Default Value"""


elements.get('dilithium')

elements['dilithium']

elements.get('kryptonite', 'There\'s no such element!')


"""
Checking for Equality vs. Identity: == vs. is
"""

#What will the output of the following code be?


a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)


animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4],
           'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

"""
Compound Data Structures

We can include containers in other containers to create compound data structures.
"""


elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight




"""
Quiz: Adding Values to Nested Dictionaries
 Add another entry, 'is_noble_gas,' to each dictionary in the elements dictionary.
 """
 
elements['hydrogen']['is_noble_gas']=False
 
 
elements['helium']['is_noble_gas']=True

print(elements['hydrogen']['is_noble_gas'])

print(elements['helium']['is_noble_gas'])


"""
Collections

Data Structures

There are a number of built in python data structures that you will use all the time when programming. You can find a table of them available below:
Data Structure 	Ordered 	Mutable 	Constructor 	Example
int 	          NA 	     NA 	     int() 	          5
float 	          NA 	     NA 	     float() 	     6.5
string 	         Yes 	     No  ' ' or " " or str() 	"this is a string"
bool 	          NA 	     NA 	      NA 	         True or False
list 	         Yes 	     Yes 	    [ ] or list() 	 [5, 'yes', 5.7]
tuple 	         Yes 	     No 	    ( ) or tuple() 	 (5, 'yes', 5.7)
set 	         No 	     Yes 	    { } or set() 	 {5, 'yes', 5.7}
dictionary 	     No 	     Keys: No 	{ } or dict() 	 {'Jun':75, 'Jul':89}

"""

"""
Mathematical, Comparison, and Logical Operators


Comparison Operators
Symbol Use Case 	Bool 	Operation
5 < 3 	          False 	Less Than
5 > 3 	          True 	    Greater Than
3 <= 3 	          True 	    Less Than or Equal To
3 >= 5 	          False 	Greater Than or Equal To
3 == 5 	          False 	Equal To
3 != 5 	          True 	    Not Equal To

And there are three logical operators you need to be familiar with:
Logical Use 	     Bool 	Operation
5 < 3 and 5 == 5 	False 	and - Evaluates if all provided statements are True
5 < 3 or 5 == 5 	True 	or - Evaluates if at least one of many statements is True
not 5 < 3 	True 	not - Flips the Bool Value
"""

"""

Control Flow

Welcome to this lesson on Control Flow! Control flow is the sequence in which your code is run. Here, we'll learn about several tools in Python we can use to affect our code's control flow:

    Conditional Statements
    Boolean Expressions
    For and While Loops
    Break and Continue
    Zip and Enumerate
    List Comprehensions

"""

"""If Statement"""

phone_balance=4
bank_balance=0
if phone_balance < 5:  #The condition is specified in a boolean expression
                        #that evaluates to either True or False.
    phone_balance += 10
    bank_balance -= 10


"""If, Elif, Else"""

season='spring'

if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')



"""
Indentation

In Python we use indentation to enclose blocks of code.

Try it out!
"""

#First Example - try changing the value of phone_balance
phone_balance = 10
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)

#Second Example - try changing the value of number

number = 145
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

#Third Example - try to change the value of age
age = 35

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)


"""Practice: Which Prize
Write an if statement that lets a competitor know which of these prizes they 
won based on the number of points they scored, which is stored in the integer 
variable points.

Points 	 Prize
1 - 50  	wooden rabbit
51 - 150 	no prize
151 - 180 	wafer-thin mint
181 - 200 	penguin

"""

points = 174  # use this input to make your submission

# write your if statement here
if points <= 50:
    result='wooden rabbit'
elif points <= 150:
    result='no prize'
elif points <= 180:
    result='wafer-thin-mint'
elif points <=200:
    result='penguin'
else:
    result= 'no prize'
    
print(result)
        

"""Quiz: Guess My Number

You decide you want to play a game where you are hiding a number from someone. 
Store this number in a variable called 'answer'. Another user provides a number 
called 'guess'. By comparing guess to answer, you inform the user if their guess
 is too high or too low.
"""


# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 500
guess = 450

if answer > guess:
    result = "Oops!  Your guess was too low."
elif answer < guess:
    result = "Oops!  Your guess was too high."
elif answer == guess:
    result = "Nice!  Your guess matched the answer!"

print(result)


"""

Quiz: Tax Purchase

Depending on where an individual is from we need to tax them appropriately. 
The states of CA, MN, and NY have taxes of 7.5%, 9.5%, and 8.9% respectively. 
Use this information to take the amount of a purchase and the corresponding state 
to assure that they are taxed by the right amount.


"""

# '''
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = 'NY'
purchase_amount = 500

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state =='MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)


"""
Complex Boolean Expressions

"""

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")


"""
Good and Bad Examples

"""

# Bad example
if True:
    print("This indented code will always get run.")
    
    
# Another bad example
if is_cold or not is_cold:
    print("This indented code will always get run.")
    
    
# Bad example
if weather == "snow" or "rain":
    print("Wear boots!")
    
# Bad example
if is_cold == True:
    print("The weather is cold!")
    
# Good example
if is_cold:
    print("The weather is cold!")
    
"""
Truth Value Testing


Here are most of the built-in objects that are considered False in Python:

    constants defined to be false: None and False
    zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
    empty sequences and collections: '"", (), [], {}, set(), range(0)

"""


errors = 3
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")
    
"""errors has the truth value True because it's a non-zero number,
 so the error message is printed. """
 
 
 """
 
 Quiz: Using Truth Values of Objects

The code below is the solution to the Which Prize quiz you've seen previously. 
You're going to rewrite this based on what you've learned about truth values.
"""
 

points = 174  # use this input when submitting your answer

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."
print(result)




"""
For Loops
A for loop is used to "iterate", or do something repeatedly, over an iterable. 
An iterable is an object that can return one of its elements at a time. 
This can include sequence types, such as strings, lists, and tuples, as well 
as non-sequence types, such as dictionaries and files.
"""
#Example

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities: #city is the iteration variable, and cities is 
                    #the iterable being looped over
    print(city)
print("Done!")



"""Using the Range() Function with For Loops
range() is a built-in function used to create an iterable sequence of numbers. 
"""
for i in range(3):
    print("Hello!" + str(i))


"""range(start=0, stop, step=1)

The range() function takes three integer arguments, the first and third of 
which are optional:

    The 'start' argument is the first number of the sequence. If unspecified, 
    'start' defaults to 0.
    The 'stop' argument is 1 more than the last number of the sequence. This 
    argument must be specified.
    The 'step' argument is the difference between each number in the sequence.
    If unspecified, 'step' defaults to 1.

Notes on using range():

    If you specify one integer inside the parentheses withrange(), it's used 
    as the value for 'stop,' and the defaults are used for the other two.
    e.g. - range(4) returns 0, 1, 2, 3
    If you specify two integers inside the parentheses withrange(), they're 
    used for 'start' and 'stop,' and the default is used for 'step.'
    e.g. - range(2, 6) returns 2, 3, 4, 5
    Or you can specify all three integers for 'start', 'stop', and 'step.'
    e.g. - range(1, 10, 2) returns 1, 3, 5, 7, 9

"""

"""Creating and Modifying Lists"""

# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())


"""Modifying a list is a bit more involved, and requires the use of the range()
 function. """

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()

print(cities)


"""
Quiz: Create Usernames

Write a for loop that iterates over the names list to create a usernames list. 

HINT: Use the .replace() method to replace the spaces with underscores. 

"""

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names: 
    usernames.append(name.replace(' ','_'))

print(usernames)

"""Let's say instead of creating a new list, we want to modify the names list 
itself with the changes and write the following code. What would this do?
"""

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)

"""
Quiz: Modify Usernames with Range

Write a for loop that uses range() to iterate over the positions in usernames
to modify the list. 


"""
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here

for i in range(len(usernames)):
    usernames[i]=usernames[i].lower().replace(" ", "_")
print(usernames)


"""
Quiz: Tag Counter
Write a for loop that iterates over a list of strings, tokens, and counts how 
many of them are XML tags. 
"""

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
        
print(count)

"""
Quiz: Create an HTML List

Write some code, including a for loop, that iterates over a list of strings 
and creates a single string, html_str, which is an HTML list. 

"""

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)

print("<li>{}</li>\n".format(items[0]) + "</ul>"  )


"""
Iterating Through Dictionaries with For Loops

"""

    
#Try it out

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))





"""
While Loops

"""
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  < 17:
    hand.append(card_deck.pop())

print(hand)

"""


    break terminates a loop
    continue skips one iteration of a loop
"""

#Try it out

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))


"""

Zip and Enumerate

Zip

zip returns an iterator that combines multiple iterables into one sequence of tuples.

"""

list(zip(['a', 'b', 'c'], [1, 2, 3]))

#unpack each tuple in a for loop

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))


some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)


"""
Enumerate

enumerate is a built in function that returns an iterator of tuples containing
 indices and values of a list. 
 
"""
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

"""
List Comprehensions

"""
cities=['chennai','bangalore','mumbai']
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

##can be reduced to below code using list comprehension
    
cities=['chennai','bangalore','mumbai']
capitalized_cities = [city.title() for city in cities]



"""
Conditionals in List Comprehensions
"""

squares = [x**2 for x in range(9) if x % 2 == 0]

#you ll get syntax error if you add else
squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3]


#If you would like to add else, you have to move the conditionals to the 
#beginning of the listcomp, right after the expression


squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
    

"""Quixx






