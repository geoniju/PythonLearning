"""
Add code to the above program to figure out who has the most messages in the file.
After all the data has been read and the dic- tionary has been created, look through the dictionary
using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages
and print how many messages the person has.
"""


fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File does not exist')
    exit()
mail_cnt = {}
for line in fhand:
    words = line.split()
    if len(words) == 0 or not words[0] == 'From':
        continue

    mail_cnt[words[1]] = mail_cnt.get(words[1], 0) + 1

# to find who sent the most messages

largest = None

for key, val in mail_cnt.items():
    if largest is None or val > largest[1]:
        largest = key, val
larkey, larval = largest
print('Person who sent the most messages: ', larkey)
print('Number of messages sent: ', larval)


