# recursion.py
# - a simple python program

def factorial(n):
    if n <= 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
    return result

print factorial(5)
print factorial(1)
print factorial(-5)
#print factorial(int(raw_input('Enter Number: ')))
for i in range(10):
    print  'factorial',i,factorial(i)