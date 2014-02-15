# split.py
# - splitting strings

test = "this is a test string"
print test
print type(test)

# split takes a string and breaks it into words
words= test.split()
print words
print type(words)

# split can take an argument as separator
test2='orange,mango,banana,pineapple,apple'
words =  test2.split(',')
for word in words:
    print word

