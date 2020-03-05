"""
Write a program that categorizes each mail message by which day of the week the commit was done.
To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the
days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
"""

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File does not exist')


day_cnt = dict()

for line in fhand:
    words = line.split()
    if len(words) == 0 or not words[0] == 'From':
        continue
    print(words[2])
    # if words[2] not in day_cnt:
    #     day_cnt[words[2]] = 1
    # else:
    #     day_cnt[words[2]] += 1
    day_cnt[words[2]] = day_cnt.get(words[2], 0) + 1
print(day_cnt)
