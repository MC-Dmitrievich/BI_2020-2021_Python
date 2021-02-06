import numpy as np
import random as random
import time
import matplotlib.pyplot as plt

for i in range(1, 1000):
    time_start = time.time()
    np.random.uniform(0, 1, i)
    time_end = time.time()
    cur_time = time_end - time_start
    plt.scatter(i, cur_time)
plt.show()

for j in range(1, 1000):
    time_start = time.time()
    for k in range(1, j + 1):
        random.uniform(0, 1)
    time_end = time.time()
    cur_time = time_end - time_start
    plt.scatter(j, cur_time)
plt.show()