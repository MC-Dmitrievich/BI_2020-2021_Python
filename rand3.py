import numpy as np
import matplotlib.pyplot as plt

point = np.array([0, 0], dtype='float')
for i in range(10000):
    plt.scatter(point[0], point[1], c="r")
    point += np.random.randn(2)
plt.show()