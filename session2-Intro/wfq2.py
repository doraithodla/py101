# wfq2.py
# Generate a word frequency table from the text in a given file

impor sys

import string   # string module defines punctuations
wfqt={}         # word frequencey table an empty dictionary

def addtoD(w, t):
    'add an item to a dictionary'
    if w in t:
        t[w] += 1
    else:
        t[w] =1

text = open(sys.argv[1]).read()
for word in text.split():
    # remove punctuations and whitespace
    if word.strip(string.punctuation+string.whitespace):
        addtoD(word,wfqt)

#for word in wfqtable:
#   print ('%s,%s')% (word, wfqtable[word])

for w in sorted(wfqt, key=wfqt.get, reverse=True):
  print w, wfqt[w]

