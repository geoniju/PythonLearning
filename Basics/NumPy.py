#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 23:30:32 2018

@author: geo
"""

"""NumPy Arrays"""

# numpy arrays are similar to python lists-contains sequence of elements and
# those can be anything and ordered 
# pandas series are built on numpy arrays

import numpy as np

"""
Numpy array and python lists

similarities
--access elements by position
--access a range of elements
--use loops like
    for X in a:

differences
--each element should have same datatype (string,int,boolean, etc)
--convenient functions mean(),std() (faster in numpy)
--can be multidimensional
"""

# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076, 51.40000153, 50.5, 75.69999695,
    58.40000153, 40.09999847, 61.5, 57.09999847,
    60.90000153, 66.59999847, 60.40000153, 68.09999847,
    66.90000153, 53.40000153, 48.59999847, 56.79999924,
    71.59999847, 58.40000153, 70.40000153, 41.20000076
])

# Change False to True for each block of code to see what it does

# Accessing elements
if True:
    print(countries[0])
    print(countries[3])

# Slicing
if True:
    print(countries[0:3])
    print(countries[:3])
    print(countries[17:])
    print(countries[:])

# Element types
if True:
    print(countries.dtype)
    print(employment.dtype)
    print(np.array([0, 1, 2, 3]).dtype)
    print(np.array([1.0, 1.5, 2.0, 2.5]).dtype)
    print(np.array([True, False, True]).dtype)
    print(np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype)

# Looping
if True:
    for country in countries:
        print('Examining country {}'.format(country))

    for i in range(len(countries)):
        country = countries[i]
        country_employment = employment[i]
        print('Country {} has employment {}'.format(country,
                                                    country_employment))

# Numpy functions
if True:
    print(employment.mean())
    print(employment.std())
    print(employment.max())
    print(employment.sum())


def max_employment(countries, employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    '''
    max_country = None  # Replace this with your code
    max_employment = 0  # Replace this with your code
    for i in range(len(countries)):
        country = countries[i]
        country_employment = employment[i]
        if country_employment > max_employment:
            max_country = country
            max_employment = country_employment
    return max_country,max_employment

print(max_employment(countries,employment))


employment.mean()
employment.std()
employment.max()
employment.sum()

"""
Vecorized operations

A vector is a list of numbers.

1 2 3 + 4 5 6 = 5 7 9 #For numpy like in linear algebra
1 2 3 + 4 5 6 = 1 2 3 4 5 6 #For list it concatenates

1 2 3 * 3 = 3 6 9 #numpy 
1 2 3 * 3 = 1 2 3 1 2 3 1 2 3 #list

More Vectorized operations

Math operations

Add: +
Subtract: -
Multiply: *
Divide: /
Exponentiate: **

Logical operations

And: &
Or: |
Not: ~

Comparison Operations
Greater: >
Greater or equal: >=
Less: <
Less or equal: <=
Equal: ==
Not Equal: !=

"""

# Change False to True for each block of code to see what it does

# Arithmetic operations between 2 NumPy arrays
if True:
    a = np.array([1, 2, 3, 4])
    b = np.array([1, 2, 1, 2])

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a ** b)

# Arithmetic operations between a NumPy array and a single number
if True:
    a = np.array([1, 2, 3, 4])
    b = 2

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a ** b)

# Logical operations with NumPy arrays
if True:
    a = np.array([True, True, False, False])
    b = np.array([True, False, True, False])

    print(a & b)
    print(a | b)
    print(~a)

    print(a & True)
    print(a & False)

    print(a | True)
    print(a | False)

# Comparison operations between 2 NumPy Arrays
if True:
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 4, 3, 2, 1])

    print(a > b)
    print(a >= b)
    print(a < b)
    print(a <= b)
    print(a == b)
    print(a != b)

# Comparison operations between a NumPy array and a single number
if True:
    a = np.array([1, 2, 3, 4])
    b = 2

    print(a > b)
    print(a >= b)
    print(a < b)
    print(a <= b)
    print(a == b)
    print(a != b)

# First 20 countries with school completion data
countries = np.array([
    'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Austria', 'Azerbaijan',
    'Bahamas', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bolivia',
    'Botswana', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cambodia', 'Cameroon', 'Cape Verde'
])

# Female school completion rate in 2007 for those 20 countries
female_completion = np.array([
    97.35583, 104.62379, 103.02998, 95.14321, 103.69019,
    98.49185, 100.88828, 95.43974, 92.11484, 91.54804,
    95.98029, 98.22902, 96.12179, 119.28105, 97.84627,
    29.07386, 38.41644, 90.70509, 51.7478, 95.45072
])

# Male school completion rate in 2007 for those 20 countries
male_completion = np.array([
    95.47622, 100.66476, 99.7926, 91.48936, 103.22096,
    97.80458, 103.81398, 88.11736, 93.55611, 87.76347,
    102.45714, 98.73953, 92.22388, 115.3892, 98.70502,
    37.00692, 45.39401, 91.22084, 62.42028, 90.66958
])


def overall_completion_rate(female_completion, male_completion):
    '''
    Fill in this function to return a NumPy array containing the overall
    school completion rate for each country. The arguments are NumPy
    arrays giving the female and male completion of each country in
    the same order.
    '''
    return (female_completion + male_completion) / 2


print(overall_completion_rate(female_completion, male_completion))

import numpy as np

# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076, 51.40000153, 50.5, 75.69999695,
    58.40000153, 40.09999847, 61.5, 57.09999847,
    60.90000153, 66.59999847, 60.40000153, 68.09999847,
    66.90000153, 53.40000153, 48.59999847, 56.79999924,
    71.59999847, 58.40000153, 70.40000153, 41.20000076
])

# Change this country name to change what country will be printed when you
# click "Test Run". Your function will be called to determine the standardized
# score for this country for each of the given 5 Gapminder variables in 2007.
# The possible country names are available in the Downloadables section.

country_name = 'United States'


def standardize_data(values):
    '''
    Fill in this function to return a standardized version of the given values,
    which will be in a NumPy array. Each value should be translated into the
    number of standard deviations that value is away from the mean of the data.
    (A positive number indicates a value higher than the mean, and a negative
    number indicates a value lower than the mean.)
    '''
    return (values - values.mean()) / values.std()


standardize_data(employment)

import numpy as np

# Change False to True for each block of code to see what it does

# Using index arrays
if True:
    a = np.array([1, 2, 3, 4])
    b = np.array([True, True, False, False])

    print(a[b])
    print(a[np.array([True, False, True, False])])

# Creating the index array using vectorized operations
if True:
    a = np.array([1, 2, 3, 2, 1])
    b = (a >= 2)

    print(a[b])
    print(a[a >= 2])

# Creating the index array using vectorized operations on another array
if True:
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 2, 3, 2, 1])

    print(b == 2)
    print(a[b == 2])


def mean_time_for_paid_students(time_spent, days_to_cancel):
    '''
    Fill in this function to calculate the mean time spent in the classroom
    for students who stayed enrolled at least (greater than or equal to) 7 days.
    Unlike in Lesson 1, you can assume that days_to_cancel will contain only
    integers (there are no students who have not canceled yet).
    
    The arguments are NumPy arrays. time_spent contains the amount of time spent
    in the classroom for each student, and days_to_cancel contains the number
    of days until each student cancel. The data is given in the same order
    in both arrays.
    '''
    is_paid = days_to_cancel >= 7
    paid_time = time_spent[is_paid]
    return paid_time.mean()


# Time spent in the classroom in the first week for 20 students
time_spent = np.array([
    12.89697233, 0., 64.55043217, 0.,
    24.2315615, 39.991625, 0., 0.,
    147.20683783, 0., 0., 0.,
    45.18261617, 157.60454283, 133.2434615, 52.85000767,
    0., 54.9204785, 26.78142417, 0.
])

# Days to cancel for 20 students
days_to_cancel = np.array([
    4, 5, 37, 3, 12, 4, 35, 38, 5, 37, 3, 3, 68,
    38, 98, 2, 249, 2, 127, 35
])

mean_time_for_paid_students(time_spent, days_to_cancel)

"""
Inplace Vs Not INplace
+- operates in place while + does not
"""

import pandas as pd

countries = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

life_expectancy_values = [74.7, 75., 83.4, 57.6, 74.6, 75.4, 72.3, 81.5, 80.2,
                          70.3, 72.1, 76.4, 68.1, 75.2, 69.8, 79.4, 70.8, 62.7,
                          67.3, 70.6]

gdp_values = [1681.61390973, 2155.48523109, 21495.80508273, 562.98768478,
              13495.1274663, 9388.68852258, 1424.19056199, 24765.54890176,
              27036.48733192, 1945.63754911, 21721.61840978, 13373.21993972,
              483.97086804, 9783.98417323, 2253.46411147, 25034.66692293,
              3680.91642923, 366.04496652, 1175.92638695, 1132.21387981]

# Life expectancy and gdp data in 2007 for 20 countries
life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)

# Change False to True for each block of code to see what it does

# Accessing elements and slicing
if True:
    print(life_expectancy[0])
    print(gdp[3:6])

# Looping
if True:
    for country_life_expectancy in life_expectancy:
        print('Examining life expectancy {}'.format(country_life_expectancy))

# Pandas functions
if True:
    print(life_expectancy.mean())
    print(life_expectancy.std())
    print(gdp.max())
    print(gdp.sum())

# Vectorized operations and index arrays
if True:
    a = pd.Series([1, 2, 3, 4])
    b = pd.Series([1, 2, 1, 2])

    print(a + b)
    print(a * 2)
    print(a >= 3)
    print(a[a >= 3])


def variable_correlation(variable1, variable2):
    '''
    Fill in this function to calculate the number of data points for which
    the directions of variable1 and variable2 relative to the mean are the
    same, and the number of data points for which they are different.
    Direction here means whether each value is above or below its mean.
    
    You can classify cases where the value is equal to the mean for one or
    both variables however you like.
    
    Each argument will be a Pandas series.
    
    For example, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([4, 5, 6, 7]), then the output would be (4, 0).
    This is because 1 and 4 are both below their means, 2 and 5 are both
    below, 3 and 6 are both above, and 4 and 7 are both above.
    
    On the other hand, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([7, 6, 5, 4]), then the output would be (0, 4).
    This is because 1 is below its mean but 7 is above its mean, and
    so on.
    '''
    num_same_direction = None  # Replace this with your code
    num_different_direction = None  # Replace this with your code

    return num_same_direction, num_different_direction
