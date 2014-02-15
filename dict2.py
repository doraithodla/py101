words = {}
text = open('test.txt').read()
for word in text.split():
	words[word]=len(word)

# print contents of the dictionary
for k in words:
	print k+ ' = '+ str(words[k])

