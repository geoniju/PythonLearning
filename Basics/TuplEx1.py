"""
Revise a previous program as follows: Read and parse the “From” lines and pull
 out the addresses from the line. Count the num- ber of messages from each person
 using a dictionary. After all the data has been read, print the person with the most commits
 by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order
 and print out the person who has the most commits.
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


cnt_lst = []

for key, val in list(mail_cnt.items()):
    cnt_lst.append((val, key))

cnt_lst.sort(reverse=True)

for key, val in cnt_lst:
    print(val, key)
    break



