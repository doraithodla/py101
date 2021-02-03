"""
echobot1.py - a bot that echoes whatever you type
- handles quit command
"""
from random import randint


startMsg = ["Hi", "Hello", "Hai", "Vanakkam", "Namaskar"]
byeMsg =  ["Bye", "See you", "Keep cool", "Peace", "Will you come back", "bfn", "ttyl"]
quit = ["q", "quit", "bye", "end"]
startIndex = randint(0,len(startMsg))
byeIndex = randint(0, len(byeMsg))

print(startMsg[startIndex])
while True:
    msg = input("> ")
    if  msg in quit:
        print(byeMsg[byeIndex])
        break
    print(msg)
