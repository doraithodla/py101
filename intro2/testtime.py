import time

s = 1

t1 = time.time()
for i in range(100):
    for j in range(100):
        print(i * j)

t2 = time.time()
print('it took', t2 - t1)
