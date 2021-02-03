"""
echobot1.py - a bot that echoes whatever you type
- handles quit command
"""
startMsg = "Hi, I am echobot. I shamelessly mimic you"
byeMsg = "Bye for now. Please do comeback. Have a great day"

quit = ["q", "quit", "bye", "end"]

print(startMsg)
while True:
    msg = input("> ")
    if  msg in quit:
        print(byeMsg)
        break
    print(msg)
