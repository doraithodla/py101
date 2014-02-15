
# long  strings


description="""
This is a small document and a typical example of a multi-line
string. This document describes Python as a pseudo language and also
a high level langauge.
"""
print "\n----- Print Description\n"
print description

print "\n----- Split the long string into a set of tokens\n"
s = description.split()


print s
print 'type of s is ', type(s)


