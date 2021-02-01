import matplotlib.pyplot as plt
import numpy as np
x = np.arange(50)
y = 2.3 * x + 4.7
plt.plot(x, y, color='r', marker='D', linewidth=1, markersize=5, markeredgecolor='c', markerfacecolor='y')
plt.title('Мое счастье в зависимости от числа съеденных единиц сыра-косички')
plt.xlabel('Сыр-косичка, единицы')
plt.ylabel('Мое счастье, единицы счастья')
plt.grid()
plt.show()
plt.savefig('kosychka.png')