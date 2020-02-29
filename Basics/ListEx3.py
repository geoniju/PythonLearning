

# Get the input file name

fname = input('Enter the file name: ')

# create file handler object
try:
    fhand = open(fname)
except:
    print('File does not exist')
    exit()
# initializing counter for filtering rows
counter = 0
for line in fhand:

    line = line.strip()
    words = line.split()
    if (len(words) == 0 or len(words) == 2) or not words[0] == 'From':
        continue
    # if not words[0] == 'From':
    #     continue
    print(words[2])
    counter += 1

    if counter == 10:
        break


