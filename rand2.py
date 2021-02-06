import numpy as np
import matplotlib.pyplot as plt
import time
from random import shuffle

def is_sorted(data) -> bool:
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))

def bogosort(data) -> list:
    while not is_sorted(data):
        shuffle(data)
    return data

for i in range(1, 8):
    times = []
    for j in range(1, 5):
        cur_list = np.random.randint(1, 100, i)
        start_time = time.time()
        bogosort(cur_list)
        finish_time = time.time()
        cur_time = finish_time - start_time
        times.append(cur_time)
    plt.bar(i, np.mean(times))
plt.show()
