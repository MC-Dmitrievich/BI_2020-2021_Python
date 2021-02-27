import itertools


def generate(n):
    ans = []
    for i in range(1, n + 1):
        comb = itertools.product(['A', 'T', 'G', 'C'], repeat=i)
        for j in comb:
            n = "".join(j)
            ans.append(n)
    return(ans)

print(generate(2))
