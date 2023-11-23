
import sys
import spacy
import pytextrank

nlp = spacy.load("en_core_web_sm")

text = open(sys.argv[1]).read()
nlp.add_pipe("textrank")
doc = nlp(text)

for phrase in doc._.phrases[:50]:
    print(phrase.text)

    
