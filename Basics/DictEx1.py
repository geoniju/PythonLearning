
""""
Write a program that reads words in words.txt and stores them as keys in a dictionary.
It doesnt matter what the values are.
Then you can use the in operator to check whether a string is in the dictionary.
"""

fhand = open('words.txt')

word_dict = dict()

for line in fhand:
    words = line.split()
    for word in words:
        if word not in word_dict.keys():
            word_dict[word] = ''
print(word_dict)
