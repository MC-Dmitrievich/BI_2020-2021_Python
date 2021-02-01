import matplotlib.pyplot as plt
import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'C:/Users/maxim/Desktop/диплом(вопрос)/fasta.txt')
x = []
with open(file_path, 'r') as file:
    for i, line in enumerate(file):
        if i % 2 == 1:
            x.append(len(line))
plt.hist(x, edgecolor='r', linewidth=2)
plt.title('Распределение длин прочтений в fasta')
plt.xlabel('Длина прочтения')
plt.ylabel('Частота встречания')
plt.show()
plt.savefig('fasta_hist.png')