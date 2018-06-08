# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 18:09:50 2018

@author: gshanth
"""

""" GLOBAL VARIABLE EXAMPLE """

PI=3.14
print(PI)
one = 1
two = 2
three = 3

one, two, three= 1,2,3
print(one)
print(two)
print(three)

two=4

print(two)
print(one)

decimal=1.1

print(decimal)

stringvar= "Hello" + "1"

print(stringvar)

"""LOCAL VARIABLE EXAMPLE"""

def FunctionName():
    newVar="world"
    global four 
    four = 4
    print(newVar)
    print(four)
    return

FunctionName()
print(newVar)
print(four)

five= 3+2

count=0
print(count)
count=count + 1
print(count)
count+=1 
print(count)
count*=1 
print(count)
count/=1 
print(count)




