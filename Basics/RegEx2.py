
"""
Write a program to look for lines of the form: New Revision: 39772 Extract the number from each of the lines
using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.
"""

import re

fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File does not exist')
    exit(0)
count = 0
sum = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9.]+)', line)
    if len(x) > 0:
        if sum == 0:
            sum = float(x[0])
        else:
            sum = sum + float(x[0])
        count += 1

print(int(sum/count))