import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(0, 5, 32)
plt.hist(x, bins=[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5], facecolor='#FFD700', edgecolor='#696969', linewidth=2)
plt.title('Распределение сьеденных единиц сыра-косички в январе 2021')
plt.xlabel('Сыр-косичка, единицы')
plt.ylabel('Частота числа съеденных единиц')
plt.show()
plt.savefig('kosychka_hist.png')


