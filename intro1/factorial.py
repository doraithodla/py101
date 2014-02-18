# factorialtest.py
# - a simple python program

def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n-1)
    return result

while True:
	n = (int(raw_input('Enter Number: ')))
	if n < 0:
		break
	else:
		print factorial(n)


