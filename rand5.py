import numpy as np

s = list("Это худший код который был написан в истории человечества")
first = s[0]
last = s[-1]
s = s[1:-1]
pos = s.index(' ')
for i in range(len(s) - 1):
    if s[i] != ' ':
        while s[pos] == ' ':
            pos = np.random.randint(len(s) - 1)
        s[i], s[pos] = s[pos], s[i]
print(first, end='')
for i in s:
    print(i, end='')
print(last, end='')