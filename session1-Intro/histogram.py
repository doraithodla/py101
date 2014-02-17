# histogram.py
# - using dictionaries

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

sentence = "This is a test. This is another test"

print histogram(sentence)

print histogram(sentence.split())
