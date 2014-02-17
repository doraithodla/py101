file=open('test.txt')
count=0
for line in file.readlines():
    count+=1
file.close()

print "no of lines in a file"
print count
