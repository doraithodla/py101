'''
wfq.py - opens a text file and counts the frequency of words in the file

'''
import sys

try:
    file = sys.argv[1]
except:
    file = r'..\data\test.txt'

words = {}

# open a file and read the contents

text = open(file).read()

# split the contents and count the frequency

wfd = {}

for word in text.split():
    try:
        wfd[word] += 1
    except:
        wfd[word] = 1

for word in wfd:
    print(word, wfd[word])
