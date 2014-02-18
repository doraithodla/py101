text="""
This is a line containining words. We are going to find the position of each. 
"""

pos = 0
print text

for word in text.split():

	pos = text.find(word, pos )
	print "'%s' is at index %d " % (word, pos)
