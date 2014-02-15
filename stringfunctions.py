# stringfunctions.py
# - There are several string functions. We will try a few

marker = "01234567890123456789012345678901234567"
string = "this is a test string. This is another"

# Find where the substring starts
print string.index('test')

# similar to index
print string.find('test')
print
print string

# replace a substring
print string.replace('test ', "")

# calculate the length of a string
print len(string)

# Count the occurences of a substring
print "In string t occurs",string.count('t'), "times"
print "is occurs ", string.count('is'), "times"