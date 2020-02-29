# get the file name as input
fname = input('Enter the filename: ')
if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
try:
    fhand = open(fname) # open the file name
except:
    print('File {} cannot be opened'.format(fname))
    exit()

count = 0
total = 0

for line in fhand:
    line = line.strip()
    if not line.startswith('X-DSPAM-Confidence'):
        continue
    line = line[-6:]
    line = float(line)
    count = count + 1
    total = total + line
average = total / count
print(average)