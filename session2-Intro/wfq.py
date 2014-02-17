words={}

# open a file and read the contents

text = open('test.txt').read()

# split the contents and count the frequency

wfd = {}

for word in text.split():
	try:
		wfd[word] += 1
	except:
		wfd[word] = 1

for word in wfd:
	print word, wfd[word]
