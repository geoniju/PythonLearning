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
maria_string = "Maria loves {} and {}"
print(maria_string.format("math","statistics"))


""" If you need to include a brace character in the 
literal text, it can be escaped by doubling: {{ and }}."""




