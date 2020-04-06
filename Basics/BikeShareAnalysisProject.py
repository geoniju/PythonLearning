
"""
In this project, you will perform an exploratory analysis on data provided by Motivate, a bike-share system provider
for many major cities in the United States. You will compare the system usage between three large cities: New York City,
 Chicago, and Washington, DC. You will al so see if there are any differences within each system for those users that
 are registered, regular users and those users that are short-term, casual users.
"""


# import all necessary packages

import csv
from datetime import datetime
from pprint import pprint


def print_first_point(filename):
    """
    This function prints and returns the first data point (seond row) from
    a csv file that includes a header row.
    """

    # print city name for reference
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))
    with open(filename, 'r') as f_in:
        # TODO: Use the csv library to set up a DictReader object. #
        # see https://docs.python.org/3/library/csv.html           #
        trip_reader = csv.DictReader(f_in)
        # TODO: Use a function on the DictReader object to read the     #
        # first trip from the data file and store it in a variable.     #
        # see https://docs.python.org/3/library/csv.html#reader-objects #
        first_trip = next(trip_reader)
        pprint(first_trip)

    return city, first_trip


def duration_in_mins(datum, city):
    """
    Takes as input a dictionary containing info about a single trip (datum) and
    its origin city (city) and returns the trip duration in units of minutes.

    Remember that Washington is in terms of milliseconds while Chicago and NYC
    are in terms of seconds.

    HINT: The csv module reads in all of the data as strings, including numeric
    values. You will need a function to convert the strings into an appropriate
    numeric type when making your transformations.
    see https://docs.python.org/3/library/functions.html
    """

    if city == 'Washington':
        duration = int(datum['Duration (ms)']) / 60000
    elif city == 'Chicago':
        duration = int(datum['tripduration']) / 60
    elif city == 'NYC':
        duration = int(datum['tripduration']) / 60
    return duration


if __name__ == '__main__':
    # list of files for each city
    data_files = ['NYC-CitiBike-2016.csv',
                  'Chicago-Divvy-2016.csv',
                  'Washington-CapitalBikeshare-2016.csv', ]
    # print the first trip from each file store in dictionary
    example_trips = {}
    for file in data_files:
        city, first_trip = print_first_point(file)
        example_trips[city] = first_trip
    print(example_trips)

    # Some tests to check that your code works. There should be no output if all of
    # the assertions pass. The `example_trips` dictionary was obtained from when
    # you printed the first trip from each of the original data files.

    tests = {'NYC': 13.9833,
             'Chicago': 15.4333,
             'Washington': 7.1231}

    for city in tests:
        assert abs(duration_in_mins(example_trips[city], city) - tests[city]) < .001
.
