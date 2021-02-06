import numpy as np
import matplotlib.pyplot as plt

start_points = np.array([[0, 0], [0.5, 1], [1, 0]])
plt.scatter(start_points[:, 0], start_points[:, 1])
coord = [0, 0]
cur_point = [0, 0]
for i in range(10000):
    plt.scatter(coord[0], coord[1])
    ind = np.random.randint(0, 3)
    cur_point[0] = start_points[ind, 0]
    cur_point[1] = start_points[ind, 1]
    coord[0] = ((cur_point[0] + coord[0]) / 2)
    coord[1] = ((cur_point[1] + coord[1]) / 2)
plt.show()
