"""
Write a program to read through a mail log, build a his- togram using a dictionary to count how many messages
have come from each email address, and print the dictionary.
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

print(mail_cnt)