# dict2.py - 
# similar to dict1.py except that words are taken from a file

# initialize an empty dictionary called words
words = {}

# open the file and read all the words into text
text = open(r'..\data\test.txt').read()

# Parse the text and split it into words and store each word and its length
for word in text.split():
	words[word]=len(word)

# print contents of the dictionary
for k in words:
	print k+ ' = '+ str(words[k])

