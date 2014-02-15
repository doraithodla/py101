text="""
This is the first line. This is the second line.This is the third line"""


words = text.split()
print "'%s' is at index %d " % (words[0], 1)
pos = len(words[0])
for word in words[1:]:

	pos = text.find(word, pos )
	print "'%s' is at index %d " % (word, pos)
