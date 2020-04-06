
"""
Write a simple program to simulate the operation of the grep command on Unix.
Ask the user to enter a regular expression and count the number of lines that matched the regular expression
"""
import re

fname = input('Enter a file name to search: ')

cmd = input('Enter a grep command: ')

try:
    fhand = open(fname)
except:
    print('File does not exist')
    exit(0)

ln_cnt = 0

for line in fhand:
    line = line.rstrip()
    if re.search(cmd, line):
        ln_cnt += 1
        print(line)

print(fname, ' had ', ln_cnt, ' that matched ', cmd)
