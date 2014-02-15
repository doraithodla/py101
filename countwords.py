# countwords.py
# - a simple python program to read the contents of a file and count the words
import sys

if (len(sys.argv) >1):
    file = open(sys.argv[1])
    text = file.read()
count =0
for word in text.split():
    count = count +1
print "File - "+sys.argv[1]+" contains "+ str(count) + " words"
