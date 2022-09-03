'''
sum_of_n.py - Calculate the sum of n natural numbers

Concepts covered:
- Numeric input
- while statement
- Addition of numbers
'''

n = int(input("Enter the value:"))
sum = 0
while (n != 0):
    print(n)
    sum += n
    n -= 1
print("The sum is: ", sum)

'''Practice problems:
1. What are some alternate methods of finding the sum of n natural numbers?
2. Rewrite the program using for loop instead of while
3. Rewrite the program using incrementing the number rather than decrementing it
'''

