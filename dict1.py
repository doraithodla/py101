words = {}
line = "among all the faomous sayings of anitquity there is one  is  a test"
for word in line.split():
	words[word]=len(word)

# print contents of the dictionary
for k in words:
	print k+ ' = '+str(words[k])

