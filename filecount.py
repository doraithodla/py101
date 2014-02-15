import os
count = 0
for (dirname, dirs, files) in os.walk('.'):
	for filename in files:
		if filename.endswith('.txt') :
			print filename
			count = count + 1
print 'Files:', count

