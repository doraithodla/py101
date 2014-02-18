# stringfunctions.py
# - There are several string functions. We will try a few

marker = "01234567890123456789012345678901234567"
string = "this is a test string. This is another"

# Find where the substring starts
print "Index gives the position of a substring %s in a string %d" % (string, string.index('test'))

# similar to index
print "find is similar to index -- %s %d" % (string, string.find('test'))
print


# replace a substring
print "replacing test with a null string original = %s replaced = %s" % (string, string.replace('test ', ""))

# calculate the length of a string
print "length of a string %s %d" % (string, len(string))

# Count the occurences of a substring
print "In string %s 'is' occurs %d times" % (string, string.count('is'))

