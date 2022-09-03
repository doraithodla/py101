from  random import randint

# Create a list (aka array) to hold the random numbers

list1 = []

for i in range(10):
    list1.append(randint(0, 100))
print(list1)

list2 = random.sample(range(1, 100), 10)
print(list2)
