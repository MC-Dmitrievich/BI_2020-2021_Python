import numpy as np
import matplotlib.pyplot as plt

start_points = np.array([[0, 0], [0.5, 0], [1, 0], [1, 0.5], [1, 1], [0.5, 1], [0, 1], [0, 0.5]])
start = [0, 0]
plt.scatter(start_points[:, 0], start_points[:, 1], marker='.', c='r')
for i in range(10000):
    plt.scatter(start[0], start[1], marker='.', c='r')
    cur = np.random.randint(8)
    cur_x = start_points[cur, 0]
    cur_y = start_points[cur, 1]
    start = [(start[0] + 2*cur_x) / 3, (start[1] + 2*cur_y) / 3]
plt.show()