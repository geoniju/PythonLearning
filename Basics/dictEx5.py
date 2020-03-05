"""
This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.

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

    domain = words[1].split('@')[-1]
    mail_cnt[domain] = mail_cnt.get(domain, 0) + 1

print(mail_cnt)