'''
stats1.py - some simple statistical functions

Concepts covered:
- random module
- sample function
- min, max, avg statistical functions on lists
'''

import random
list2 = random.sample(range(1, 100), 10)
print(list2)

print("MAX: ",max(list2))
print("MIN: ",min(list2))
print("AVG: ", (sum(list2)/len(list2)))

'''
Practice Exercises:
1. Can you calculate the distance beween min and max 
2. How many item sin the list are between minimum and max value. What are they?
3. How many items are more than max value?
4. Can you find the average of the list from problem 2?
