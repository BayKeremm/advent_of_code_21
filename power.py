import numpy as np
f = open("input", "r")
a = np.loadtxt(f, dtype=str)



def solve(Index):
    ones = 0
    zeros = 0
    for i in range(len(a)):
        if(a[i][Index] == '1'):
            ones += 1
        if(a[i][Index] == '0'):
            zeros += 1
    if(ones > zeros):
        return 1
    else:
        return 0


arr = []
for i in range(len(a[0])):
    rc = solve(i)
    arr.append(rc)
print(arr)
