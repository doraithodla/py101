# stripp.py
# - strip punctuation
from string import *

text = open('punct.txt').read()
print text
for word in text.split():
    print word.strip(punctuation+whitespace)
