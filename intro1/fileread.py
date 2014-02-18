# fileread.py
# - a simple python program to read the contents of a file
import sys


file = open(sys.argv[1])
text = file.read()
print text
