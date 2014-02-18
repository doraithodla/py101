# dict1.py - Create a dictionary and populate it
# 

words = {}
line = "The quick brown fox jumped over a lazy dog"

# splits a string into words
# dictionary stores a word as the key and its length as its value

for word in line.split():
	words[word]=len(word)

# print contents of the dictionary
print "Word and its length from the dictionary"

for k in words:
	print k+ ' = '+str(words[k])

