"""
convertbot.py - a bot to perform temperature conversion
"""
from random import randint


startMsg = ["Hi", "Hello", "Hai", "Vanakkam", "Namaskar"]
byeMsg =  ["Bye", "See you", "Keep cool", "Peace", "Will you come back", "bfn", "ttyl"]
quit = ["q", "quit", "bye", "end"]


startIndex = randint(0,len(startMsg))
byeIndex = randint(0, len(byeMsg))

def c2f(c):
    return((c*1.8)+32)

def f2c(f):
    return(((f-32)*5)/9)

print(startMsg[startIndex])
while True:
    msg = input("> ")
    words = msg.split()
    if  words[0] in quit:
        print(byeMsg[byeIndex])
        break
    elif words[0] == "c2f":
        print(c2f(float(words[1])))
    elif words[0] == "f2c":
        print(f2c(float(words[1])))
    else:
        print("I don't understand the command")

