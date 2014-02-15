
# Simple string
# create a variable title and assign a string value to it.
title = "This is a Python tutorial"

# "\n prints a new line
print "\n----- print title\n"
print title

print "\n----- print title.upper()\n"
print title.upper()


print "\n----- prnt title.lower()\n"
print title.lower()

print "\n-----Find a substring 'tutor' in title \n"
pos = title.find("tutor")
print title[pos:]

print "\n-----Replace a substring\n"
newtitle = title.replace("tutorial", "book")
print newtitle
