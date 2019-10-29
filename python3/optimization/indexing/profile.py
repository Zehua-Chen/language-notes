import time
import numpy as np

start_time = time.time()

data = list()
result = 0

for i in range(0, 1000):
    data.append(i)

for i in range(0, 10000):
    for i in range(0, 1000):
        result += 1

print("list time = {}".format(time.time() - start_time))

start_time = time.time()
data = dict()
result = 0

for i in range(0, 1000):
    data[i] = i

for i in range(0, 10000):
    for i in range(0, 1000):
        result += data[i]

print("dict time = {}".format(time.time() - start_time))

start_time = time.time()
data = np.ndarray(1000)
result = 0

for i in range(0, 1000):
    data[i] = i

for i in range(0, 10000):
    for i in range(0, 1000):
        result += data[i]

print("numpy time = {}".format(time.time() - start_time))
