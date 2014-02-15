# files.py
# - a simple python program to show essential file operations
# simple file operations

file = open("test.txt")
lineno=1
for line in file.readlines():
  print lineno,line
  lineno += 1

file.close()






