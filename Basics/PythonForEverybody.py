# using try,except and open
fname = input('Enter the file name')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('Number of lines starting with Subject: ', count)
print('Thank you')

