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


















