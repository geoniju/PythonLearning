"""
This program counts the distribution of the hour of the day for each of the messages.
You can pull the hour from the “From” line by finding the time string and then splitting that
string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts,
 one per line, sorted by hour as shown below
"""

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File does not exist')
    exit()

mail_cnt = dict()

for line in fhand:
    words = line.split()
    if len(words) == 0 or not words[0] == 'From':
        continue
    msghrs = words[5].split(':')[0]
    mail_cnt[msghrs] = mail_cnt.get(msghrs, 0) + 1
#print(mail_cnt)

mail_cnt_lst = list(mail_cnt.items())
mail_cnt_lst.sort()
#print(mail_cnt_lst)

for key, value in mail_cnt_lst:
    print(key, value)
