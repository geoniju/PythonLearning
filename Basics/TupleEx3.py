"""
Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert
all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation,
or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency
varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

"""

import string

fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File does not exist')
    exit()

word_cnt = {}

for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        word_cnt[word] = word_cnt.get(word, 0) + 1

word_cnt = list(word_cnt.items())
word_srt_lst = []

for key, value in word_cnt:
    word_srt_lst.append((value, key))

word_srt_lst.sort(reverse=True)

for key, value in word_srt_lst:
    print(value, key)
